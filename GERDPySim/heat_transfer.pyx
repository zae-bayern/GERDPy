# cython: language_level=3

import time as tim
from functools import partial
from multiprocessing import Pool

import numpy as np
from scipy.integrate import quad
from scipy.special import erf

from .boreholes import Borehole

cpdef double finite_line_source(double time, double alpha, Borehole borehole1, Borehole borehole2, bint reaSource=True, bint imgSource=True):
    def _Ils(double s, Borehole b1, Borehole b2, bint reaSource, bint imgSource):
        cdef double r = b1.distance(b2)
        cdef double func = 0.0
        if reaSource:
            func += _erfint((b2.D - b1.D + b2.H) * s)
            func -= _erfint((b2.D - b1.D) * s)
            func += _erfint((b2.D - b1.D - b1.H) * s)
            func -= _erfint((b2.D - b1.D + b2.H - b1.H) * s)
        if imgSource:
            func += _erfint((b2.D + b1.D + b2.H) * s)
            func -= _erfint((b2.D + b1.D) * s)
            func += _erfint((b2.D + b1.D + b1.H) * s)
            func -= _erfint((b2.D + b1.D + b2.H + b1.H) * s)
        return 0.5 / (b2.H * s**2) * func * np.exp(-r**2 * s**2)

    def _erfint(double x):
        return x * erf(x) - 1.0 / np.sqrt(np.pi) * (1.0 - np.exp(-x**2))

    cdef double a = 1.0 / np.sqrt(4.0 * alpha * time)
    cdef double h, err
    h, err = quad(_Ils, a, np.inf, args=(borehole1, borehole2, reaSource, imgSource))
    return h

cpdef np.ndarray thermal_response_factors(list boreSegments, time, double alpha, self, bint use_similarities=True, bint splitRealAndImage=True, double disTol=0.01, double tol=1.0e-6, processes=None, bint disp=True):
    cdef int nSources = len(boreSegments)
    cdef int nt = len(np.atleast_1d(time))
    cdef np.ndarray h_ij = np.zeros((nSources, nSources, nt))
    cdef Pool pool = Pool(processes=processes)
    cdef double tic = tim.time()

    if use_similarities:
        if disp:
            print('Identifying similarities ...')
            self.ui.text_console.insertPlainText('Identifying similarities ...\\n')
        (nSimPos, simPos, disSimPos, HSimPos, DSimPos,
         nSimNeg, simNeg, disSimNeg, HSimNeg, DSimNeg) = \
            similarities(boreSegments,
                         splitRealAndImage=splitRealAndImage,
                         disTol=disTol,
                         tol=tol,
                         processes=processes)
        print('checkpoint final')
        toc1 = tim.time()
        if disp:
            print('{} sec'.format(toc1 - tic))
            print('Calculating segment to segment response factors ...')
            self.ui.text_console.insertPlainText('{} sec\n'.format(toc1 - tic))
            self.ui.text_console.insertPlainText('Calculating segment to segment response factors ...\n')

        # Similarities for real sources
        for s in range(nSimPos):
            n1 = simPos[s][0][0]
            n2 = simPos[s][0][1]
            b1 = boreSegments[n1]
            b2 = boreSegments[n2]
            if splitRealAndImage:
                # FLS solution for real source only
                func = partial(finite_line_source,
                               alpha=alpha, borehole1=b1, borehole2=b2,
                               reaSource=True, imgSource=False)
            else:
                # FLS solution for combined real and image sources
                func = partial(finite_line_source,
                               alpha=alpha, borehole1=b1, borehole2=b2,
                               reaSource=True, imgSource=True)
            # Evaluate the FLS solution at all times in parallel
            hPos = np.array(pool.map(func, np.atleast_1d(time)))
            # Assign thermal response factors to similar segment pairs
            for (i, j) in simPos[s]:
                h_ij[j, i, :] = hPos
                h_ij[i, j, :] = b2.H/b1.H * hPos

        # Similarities for image sources (only if splitRealAndImage=True)
        if splitRealAndImage:
            for s in range(nSimNeg):
                n1 = simNeg[s][0][0]
                n2 = simNeg[s][0][1]
                b1 = boreSegments[n1]
                b2 = boreSegments[n2]
                # FLS solution for image source only
                func = partial(finite_line_source,
                               alpha=alpha, borehole1=b1, borehole2=b2,
                               reaSource=False, imgSource=True)
                # Evaluate the FLS solution at all times in parallel
                hNeg = np.array(pool.map(func, time))
                # Assign thermal response factors to similar segment pairs
                for (i, j) in simNeg[s]:
                    h_ij[j, i, :] = h_ij[j, i, :] + hNeg
                    h_ij[i, j, :] = b2.H/b1.H * h_ij[j, i, :]

    else:
        # Calculations without similarities
        if disp:
            print('Calculating segment to segment response factors ...')
            self.ui.text_console.insertPlainText('Calculating segment to segment response factors ...\n')
        for i in range(nSources):
            # Segment to same-segment thermal response factor
            # FLS solution for combined real and image sources
            b2 = boreSegments[i]
            func = partial(finite_line_source,
                           alpha=alpha, borehole1=b2, borehole2=b2)
            # Evaluate the FLS solution at all times in parallel
            h = np.array(pool.map(func, time))
            h_ij[i, i, :] = h

            # Segment to other segments thermal response factor
            for j in range(i+1, nSources):
                b1 = boreSegments[j]
                # Evaluate the FLS solution at all times in parallel
                func = partial(finite_line_source,
                               alpha=alpha, borehole1=b1, borehole2=b2)
                h = np.array(pool.map(func, time))
                h_ij[i, j, :] = h
                h_ij[j, i, :] = b2.H / b1.H * h_ij[i, j, :]

    toc2 = tim.time()
    if disp:
        print('{} sec'.format(toc2 - tic))
        self.ui.text_console.insertPlainText('{} sec\n'.format(toc2 - tic))

    pool.close()
    pool.join()

    if np.isscalar(time):
        h_ij = h_ij[:, :, 0]

    return h_ij

cpdef tuple similarities(boreholes, bint splitRealAndImage=True, double disTol=0.01, double tol=1.0e-6, processes=None):
    """
    Find similarities in the FLS solution for groups of boreholes.

    This function identifies pairs of boreholes for which the evaluation of the
    Finite Line Source (FLS) solution is equivalent.

    Parameters
    ----------
    boreholes : list of Borehole objects
        List of boreholes for which similarity pairs are identified.
    splitRealAndImage : boolean, defaults to True
        Set to True if similarities are evaluated separately for real and image
        sources. Set to False if similarities are evaluated for the sum of the
        real and image sources.
    disTol : float, defaults to 0.01
        Relative tolerance on radial distance. Two distances
        (d1, d2) between two pairs of boreholes are considered equal if the
        difference between the two distances (abs(d1-d2)) is below tolerance.
    tol : float, defaults to 1.0e-6
        Relative tolerance on length and depth. Two lengths H1, H2
        (or depths D1, D2) are considered equal if abs(H1 - H2)/H2 < tol

    Returns
    -------
    nSimPos : integer
        Number of similarities in the evaluation of real sources
        (if splitRealAndImage=True) or sum of real and image sources
        (if splitRealAndImage=False).
    simPos : list of list of tuples
        For each similarity, a list of pairs (tuple) of borehole indexes is
        returned.
    disSimPos : list of floats
        List of distances between boreholes for each similarity.
    HSimPos : list of tuples
        List of lengths of the pairs of boreholes in each similarity.
    DSimPos : list of tuples
        List of depth of the pairs of boreholes in each similarity.
    nSimNeg : integer
        Number of similarities in the evaluation of image sources
        (if splitRealAndImage=True), equals 0 if (splitRealAndImage=False).
    simNeg : list of list of tuples
        For each similarity, a list of pairs (tuple) of borehole indexes is
        returned.
    disSimNeg : list of floats
        List of distances between boreholes for each similarity.
    HSimNeg : list of tuples
        List of lengths of the pairs of boreholes in each similarity.
    DSimNeg : list of tuples
        List of depth of the pairs of boreholes in each similarity.
    processes : int, defaults to cpu_count()
        Number of processors to use in calculations.

    Examples
    --------
    >>> b1 = gt.boreholes.Borehole(H=150., D=4., r_b=0.075, x=0., y=0.)
    >>> b2 = gt.boreholes.Borehole(H=150., D=4., r_b=0.075, x=5., y=0.)
    >>> gt.heat_transfer.finite_line_source_similarities([b1, b2])
    2
    [[(0, 0), (1, 1)], [(0, 1)]]
    [0.075, 5.0]
    [(150.0, 150.0), (150.0, 150.0)]
    [(4.0, 4.0), (4.0, 4.0)]
    2
    [[(0, 0), (1, 1)], [(0, 1)]]
    [0.075, 5.0]
    [(150.0, 150.0), (150.0, 150.0)]
    [(4.0, 4.0), (4.0, 4.0)]

    """
    print('checkpoint2')
    # Initialize pool of workers
    pool = Pool(processes=processes)
    print('checkpoint3')

    # Group pairs of boreholes by radial distance
    (nDis, disPairs, nPairs, pairs) = \
        _similarities_group_by_distance(boreholes, disTol=disTol)
    print('checkpoint4')

    # If real and image parts of the FLS are split, evaluate real and image
    # similarities separately:
    if splitRealAndImage:
        print('checkpoint_if')
        func = partial(_similarities_one_distance,
                       boreholes=boreholes,
                       kind='real',
                       tol=tol)
        print('checkpoint_if1')
        # Evaluate similarities for each distance in parallel
        realSims = pool.map(func, pairs)  # .exe steigt hier aus
        print('checkpoint_if2')

        func = partial(_similarities_one_distance,
                       boreholes=boreholes,
                       kind='image',
                       tol=tol)
        print('checkpoint_if3')
        # Evaluate similarities for each distance in parallel
        imageSims = pool.map(func, pairs)
        print('checkpoint_if4')

    # Otherwise, evaluate the combined real+image FLS similarities
    else:
        func = partial(_similarities_one_distance,
                       boreholes=boreholes,
                       kind='realandimage',
                       tol=tol)
        # Evaluate symmetries for each distance in parallel
        realSims = pool.map(func, pairs)

    # Close pool of workers
    pool.close()
    pool.join()

    # Aggregate real similarities for all distances
    nSimPos = 0
    simPos = []
    HSimPos = []
    DSimPos = []
    disSimPos = []
    for i in range(nDis):
        realSim = realSims[i]
        nSim = realSim[0]
        nSimPos += nSim
        disSimPos += [disPairs[i] for _ in range(nSim)]
        simPos += realSim[1]
        HSimPos += realSim[2]
        DSimPos += realSim[3]

    # Aggregate image similarities for all distances
    nSimNeg = 0
    simNeg = []
    HSimNeg = []
    DSimNeg = []
    disSimNeg = []
    if splitRealAndImage:
        for i in range(nDis):
            imageSim = imageSims[i]
            nSim = imageSim[0]
            nSimNeg += nSim
            disSimNeg += [disPairs[i] for _ in range(nSim)]
            simNeg += imageSim[1]
            HSimNeg += imageSim[2]
            DSimNeg += imageSim[3]

    print('Checkpointfinal')

    return nSimPos, simPos, disSimPos, HSimPos, DSimPos, \
            nSimNeg, simNeg, disSimNeg, HSimNeg, DSimNeg


cdef tuple _similarities_group_by_distance(boreholes, double disTol = 0.01):
    """
    Groups pairs of boreholes by radial distance between borehole.

    Parameters
    ----------
    boreholes : list of Borehole objects
        List of boreholes in the bore field.
    disTol : float, defaults to 0.01
        Relative tolerance on radial distance. Two distances
        (d1, d2) between two pairs of boreholes are considered equal if the
        difference between the two distances (abs(d1-d2)) is below tolerance.

    Returns
    -------
    nDis : int
        Number of unique radial distances between pairs of borehole.
    disPairs : list
        List of radial distances.
    nPairs : list
        List of number of pairs for each radial distance.
    pairs : list
        List of tuples of the borehole indices of borehole pairs at each
        radial distance.

    Raises
    ------
    SomeError

    See Also
    --------
    OtherModules

    Examples
    --------

    """
    # Initialize lists
    nPairs = [1]
    pairs = [[(0, 0)]]
    disPairs = [boreholes[0].r_b]
    nDis = 1

    nb = len(boreholes)
    for i in range(nb):
        b1 = boreholes[i]
        if i == 0:
            i2 = i + 1
        else:
            i2 = i
        for j in range(i2, nb):
            b2 = boreholes[j]
            # Distance between current pair of boreholes
            dis = b1.distance(b2)
            if i == j:
                # The relative tolerance is used for same-borehole
                # distances
                rTol = 1.0e-6 * b1.r_b
            else:
                rTol = disTol*dis
            # Verify if the current pair should be included in the
            # previously identified symmetries
            for k in range(nDis):
                if abs(disPairs[k] - dis) < rTol:
                    pairs[k].append((i, j))
                    nPairs[k] += 1
                    break

            else:
                # Add symmetry to list if no match was found
                nDis += 1
                disPairs.append(dis)
                pairs.append([(i, j)])
                nPairs.append(1)
    return nDis, disPairs, nPairs, pairs

cdef tuple _similarities_one_distance(pairs, boreholes, str kind, double tol = 1.0e-6):
    """
    Evaluates similarities for all pairs of boreholes separated by the same
    radial distance.

    Parameters
    ----------
    pairs : list
        List of tuples of the borehole indices of borehole pairs at each
        radial distance.
    boreholes : list of Borehole objects
        List of boreholes in the bore field.
    kind : string
        Type of similarity to be evaluated
            - 'real' : similarity in real sources
            - 'image' : similarity in image sources
            - 'realandimage' : similarity for combined real and image sources.
    tol : float, defaults to 1.0e-6
        Relative tolerance on length and depth. Two lenths H1, H2
        (or depths D1, D2) are considered equal if abs(H1 - H2)/H2 < tol

    Returns
    -------
    nSim : int
        Number of similarities.
    sim : list
        For each similarity, a list of pairs (tuple) of borehole indexes is
        returned.
    HSim : list
        List of lengths (tuple) of the pairs of boreholes in each similarity.
    DSim : list
        List of depths (tuple) of the pairs of boreholes in each similarity.

    Raises
    ------
    SomeError

    See Also
    --------
    OtherModules

    Examples
    --------

    """
    # Condition for equivalence of the real part of the FLS solution
    def compare_real_segments(H1a, H1b, H2a, H2b, D1a,
                              D1b, D2a, D2b, tol):
        if (abs((H1a-H1b)/H1a) < tol and
            abs((H2a-H2b)/H2a) < tol and
            abs(((D2a-D1a)-(D2b-D1b))/(D2a-D1a+1e-30)) < tol):
            similarity = True
        else:
            similarity = False
        return similarity

    # Condition for equivalence of the image part of the FLS solution
    def compare_image_segments(H1a, H1b, H2a, H2b,
                               D1a, D1b, D2a, D2b, tol):
        if (abs((H1a-H1b)/H1a) < tol and
            abs((H2a-H2b)/H2a) < tol and
            abs(((D2a+D1a)-(D2b+D1b))/(D2a+D1a+1e-30)) < tol):
            similarity = True
        else:
            similarity = False
        return similarity

    # Condition for equivalence of the full FLS solution
    def compare_realandimage_segments(H1a, H1b, H2a, H2b,
                                      D1a, D1b, D2a, D2b,
                                      tol):
        if (abs((H1a-H1b)/H1a) < tol and
            abs((H2a-H2b)/H2a) < tol and
            abs((D1a-D1b)/(D1a+1e-30)) < tol and
            abs((D2a-D2b)/(D2a+1e-30)) < tol):
            similarity = True
        else:
            similarity = False
        return similarity

    # Initialize comparison function based on input argument
    if kind.lower() == 'real':
        # Check real part of FLS
        compare_segments = compare_real_segments
    elif kind.lower() == 'image':
        # Check image part of FLS
        compare_segments = compare_image_segments
    elif kind.lower() == 'realandimage':
        # Check full real+image FLS
        compare_segments = compare_realandimage_segments
    else:
        raise NotImplementedError("Error: '{}' not implemented.".format(kind.lower()))

    # Initialize symmetries
    nSim = 1
    pair0 = pairs[0]
    i0 = pair0[0]
    j0 = pair0[1]
    sim = [[pair0]]
    HSim = [(boreholes[i0].H, boreholes[j0].H)]
    DSim = [(boreholes[i0].D, boreholes[j0].D)]

    # Cycle through all pairs of boreholes for the given distance
    for pair in pairs[1:]:
        ibor = pair[0]
        jbor = pair[1]
        b1 = boreholes[ibor]
        b2 = boreholes[jbor]
        # Verify if the current pair should be included in the
        # previously identified symmetries
        for k in range(nSim):
            H1 = HSim[k][0]
            H2 = HSim[k][1]
            D1 = DSim[k][0]
            D2 = DSim[k][1]
            if compare_segments(H1, b1.H, H2, b2.H,
                                D1, b1.D, D2, b2.D, tol):
                sim[k].append((ibor, jbor))
                break
            elif compare_segments(H1, b2.H, H2, b1.H,
                                  D1, b2.D, D2, b1.D, tol):
                sim[k].append((jbor, ibor))
                break

        else:
            # Add symmetry to list if no match was found
            nSim += 1
            sim.append([pair])
            HSim.append((b1.H, b2.H))
            DSim.append((b1.D, b2.D))

    return nSim, sim, HSim, DSim
