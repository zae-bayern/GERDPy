# -*- coding: utf-8 -*-
""" GERDPySim - 'gfunction.py'
    
    Functions to determine the g-function (Dirichlet temperature boundary condition)
    
    based on: Pygfunction by Massimo Cimmino

    Authors: Massimo Cimmino
"""
import time as tim

import numpy as np
from scipy.constants import pi
from scipy.interpolate import interp1d as interp1d

from .boreholes import Borehole
from .heat_transfer import thermal_response_factors


def uniform_temperature(boreholes, time, alpha, self, nSegments=12, method='linear',
                        use_similarities=True, disTol=0.01, tol=1.0e-6,
                        processes=None, disp=True):
    """
    Evaluate the g-function with uniform borehole wall temperature.

    This function superimposes the finite line source (FLS) solution to
    estimate the g-function of a geothermal bore field. Each borehole is
    modeled as a series of finite line source segments, as proposed in
    [#CimminoBernier2014]_.

    Parameters
    ----------
    boreholes : list of Borehole objects
        List of boreholes included in the bore field.
    time : float or array
        Values of time (in seconds) for which the g-function is evaluated.
    alpha : float
        Soil thermal diffusivity (in m2/s).
    nSegments : int, optional
        Number of line segments used per borehole.
        Default is 12.
    method : string, optional
        Interpolation method used for segment-to-segment thermal response
        factors. See documentation for scipy.interpolate.interp1d.
        Default is linear.
    use_similarities : bool, optional
        True if similarities are used to limit the number of FLS evaluations.
        Default is True.
    disTol : float, optional
        Relative tolerance on radial distance. Two distances
        (d1, d2) between two pairs of boreholes are considered equal if the
        difference between the two distances (abs(d1-d2)) is below tolerance.
        Default is 0.01.
    tol : float, optional
        Relative tolerance on length and depth. Two lengths H1, H2
        (or depths D1, D2) are considered equal if abs(H1 - H2)/H2 < tol.
        Default is 1.0e-6.
    processes : int, optional
        Number of processors to use in calculations. If the value is set to
        None, a number of processors equal to cpu_count() is used.
        Default is None.
    disp : bool, optional
        Set to true to print progression messages.
        Default is False.

    Returns
    -------
    gFunction : float or array
        Values of the g-function

    Examples
    --------
    >>> b1 = gt.boreholes.Borehole(H=150., D=4., r_b=0.075, x=0., y=0.)
    >>> b2 = gt.boreholes.Borehole(H=150., D=4., r_b=0.075, x=5., y=0.)
    >>> alpha = 1.0e-6
    >>> time = np.array([1.0*10**i for i in range(4, 12)])
    >>> gt.gfunction.uniform_temperature([b1, b2], time, alpha)
    array([ 0.75978079,  1.84859851,  2.98852756,  4.33406497,  6.27830732,
        8.05746656,  8.93697282,  9.04925079])

    References
    ----------
    .. [#CimminoBernier2014] Cimmino, M., & Bernier, M. (2014). A
       semi-analytical method to generate g-functions for geothermal bore
       fields. International Journal of Heat and Mass Transfer, 70, 641-650.

    """
    if disp:
        print(80*'-')
        print('Calculating g-function for uniform borehole wall temperature')
        print(80*'-')
        self.ui.text_console.insertPlainText(60 * '-' + '\n')
        self.ui.text_console.insertPlainText('Calculating g-function for uniform borehole wall temperature\n')
        self.ui.text_console.insertPlainText(60 * '-' + '\n')
        self.ui.text_console.insertPlainText(60 * '-' + '\n')

    # Initialize chrono
    tic = tim.time()
    # Number of boreholes
    nBoreholes = len(boreholes)
    # Total number of line sources
    nSources = nSegments*nBoreholes
    # Number of time values
    nt = len(np.atleast_1d(time))
    # Initialize g-function
    gFunction = np.zeros(nt)
    # Initialize segment heat extraction rates
    Q = np.zeros((nSources, nt))

    # Split boreholes into segments
    boreSegments = _borehole_segments(boreholes, nSegments)
    # Vector of time values
    t = np.atleast_1d(time).flatten()
    # Calculate segment to segment thermal response factors
    h_ij = thermal_response_factors(
        boreSegments, t, alpha, self, use_similarities=use_similarities,
        splitRealAndImage=True, disTol=disTol, tol=tol, processes=processes,
        disp=disp)
    toc1 = tim.time()

    if disp:
        print('Building and solving system of equations ...')
        self.ui.text_console.insertPlainText('Building and solving system of equations ...\n')
    # -------------------------------------------------------------------------
    # Build a system of equation [A]*[X] = [B] for the evaluation of the
    # g-function. [A] is a coefficient matrix, [X] = [Qb,Tb] is a state
    # space vector of the borehole heat extraction rates and borehole wall
    # temperature (equal for all segments), [B] is a coefficient vector.
    # -------------------------------------------------------------------------

    # Segment lengths
    Hb = np.array([b.H for b in boreSegments])
    # Vector of time steps
    dt = np.hstack((t[0], t[1:] - t[:-1]))
    if not np.isscalar(time) and len(time) > 1:
        # Spline object for thermal response factors
        h_dt = interp1d(np.hstack((0., t)),
                        np.dstack((np.zeros((nSources,nSources)), h_ij)),
                        kind=method, axis=2)
        # Thermal response factors evaluated at t=dt
        h_dt = h_dt(dt)
    else:
        h_dt = h_ij
    # Thermal response factor increments
    dh_ij = np.concatenate((h_ij[:,:,0:1], h_ij[:,:,1:]-h_ij[:,:,:-1]), axis=2)

    # Energy conservation: sum([Qb*Hb]) = sum([Hb])
    A_eq2 = np.hstack((Hb, 0.))
    B_eq2 = np.atleast_1d(np.sum(Hb))

    # Build and solve the system of equations at all times
    for p in range(nt):
        # Current thermal response factor matrix
        h_ij_dt = h_dt[:,:,p]
        # Reconstructed load history
        Q_reconstructed = load_history_reconstruction(t[0:p+1], Q[:,0:p+1])
        # Borehole wall temperature for zero heat extraction at current step
        Tb_0 = _temporal_superposition(dh_ij, Q_reconstructed)
        # Spatial superposition: [Tb] = [Tb0] + [h_ij_dt]*[Qb]
        A_eq1 = np.hstack((h_ij_dt, -np.ones((nSources, 1))))
        B_eq1 = -Tb_0
        # Assemble equations
        A = np.vstack((A_eq1, A_eq2))
        B = np.hstack((B_eq1, B_eq2))
        # Solve the system of equations
        X = np.linalg.solve(A, B)
        # Store calculated heat extraction rates
        Q[:,p] = X[0:nSources]
        # The borehole wall temperatures are equal for all segments
        Tb = X[-1]
        gFunction[p] = Tb

    toc2 = tim.time()
    if disp:
        print('{} sec'.format(toc2 - toc1))
        print('Total time for g-function evaluation: {} sec'.format(
                toc2 - tic))
        print(60*'-')
        self.ui.text_console.insertPlainText('{} sec\n'.format(toc2 - toc1))
        self.ui.text_console.insertPlainText('Total time for g-function evaluation: {} sec\n'.format(toc2 - tic))
        self.ui.text_console.insertPlainText(60 * '-' + '\n')

    # Return float if time is a scalar
    if np.isscalar(time):
        gFunction = np.asscalar(gFunction)

    return gFunction


def load_history_reconstruction(time, Q):
    """
    Reconstructs the load history.

    This function calculates an equivalent load history for an inverted order
    of time step sizes.

    Parameters
    ----------
    time : array
        Values of time (in seconds) in the load history.
    Q : array
        Heat extraction rates (in Watts) of all segments at all times.

    Returns
    -------
    Q_reconstructed : array
        Reconstructed load history.

    """
    # Number of heat sources
    nSources = Q.shape[0]
    # Time step sizes
    dt = np.hstack((time[0], time[1:]-time[:-1]))
    # Time vector
    t = np.hstack((0., time, time[-1] + time[0]))
    # Inverted time step sizes
    dt_reconstructed = dt[::-1]
    # Reconstructed time vector
    t_reconstructed = np.hstack((0., np.cumsum(dt_reconstructed)))
    # Accumulated heat extracted
    f = np.hstack((np.zeros((nSources, 1)), np.cumsum(Q*dt, axis=1)))
    f = np.hstack((f, f[:,-1:]))
    # Create interpolation object for accumulated heat extracted
    sf = interp1d(t, f, kind='linear', axis=1)
    # Reconstructed load history
    Q_reconstructed = (sf(t_reconstructed[1:]) - sf(t_reconstructed[:-1])) \
        / dt_reconstructed

    return Q_reconstructed


def _borehole_segments(boreholes, nSegments):
    """
    Split boreholes into segments.

    This function goes through the list of boreholes and builds a new list,
    with each borehole split into nSegments.

    Parameters
    ----------
    boreholes : list of Borehole objects
        List of boreholes included in the bore field.
    nSegments : int
        Number of line segments used per borehole.

    Returns
    -------
    boreSegments : list
        List of borehole segments.

    """
    boreSegments = []
    for b in boreholes:
        for i in range(nSegments):
            # Divide borehole into segments of equal length
            H = b.H / nSegments
            # Buried depth of the i-th segment
            D = b.D + i * b.H / nSegments
            # Add to list of segments
            boreSegments.append(Borehole(H, D, b.r_b, b.x, b.y))
    return boreSegments


def _temporal_superposition(dh_ij, Q):
    """
    Temporal superposition for inequal time steps.

    Parameters
    ----------
    dh_ij : array
        Values of the segment-to-segment thermal response factor increments at
        the given time step.
    Q : array
        Heat extraction rates of all segments at all times.

    Returns
    -------
    Tb_0 : array
        Current values of borehole wall temperatures assuming no heat
        extraction during current time step.

    """
    # Number of heat sources
    nSources = Q.shape[0]
    # Number of time steps
    nt = Q.shape[1]
    # Borehole wall temperature
    Tb_0 = np.zeros(nSources)
    # Spatial and temporal superpositions
    for it in range(nt):
        Tb_0 += dh_ij[:,:,it].dot(Q[:,nt-it-1])
    return Tb_0
