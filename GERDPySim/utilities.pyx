# cython: language_level=3
""" GERDPySim - 'utilities.py'
    
    Auxiliary Functions

    Authors: Massimo Cimmino, Yannick Apfel, Meike Martin
"""

import numpy as np
cimport numpy as np
cimport cython

cpdef np.ndarray time_ClaessonJaved(double dt, double tmax, int cells_per_level=5):
    """
    Build a time vector of expanding cell width following the method of
    Claesson and Javed.

    Parameters
    ----------
    dt : double
        Simulation time step (in seconds).
    tmax : double
        Maximum simulation time (in seconds).
    cells_per_level : int
        Number of time steps cells per level. Cell widths double every
        cells_per_level cells. Default is 5.

    Returns
    -------
    np.ndarray
        Time vector.
    """
    cdef double t = 0.0
    cdef int i = 0
    cdef list time = []
    while t < tmax:
        i += 1
        cdef double v = np.ceil(i / cells_per_level)
        cdef double width = 2.0**(v-1)
        t += width * dt
        time.append(t)
    return np.array(time)

  cpdef np.ndarray Q_moving_average(np.ndarray Q):
    """
    Calculate the moving average of a time series.

    Parameters
    ----------
    Q : np.ndarray
        Time series data.

    Returns
    -------
    np.ndarray
        Moving average of the time series.
    """
    cdef int h_interv = 25
    cdef np.ndarray Q_ma = np.zeros(len(Q))
    cdef int i
    for i in range(len(Q)):
        if i < (h_interv / 2):
            Q_ma[i] = np.mean(Q[0 : (2 * i + 1)])
        elif (i >= (h_interv / 2)) and (i <= ((len(Q) - 1) - (h_interv / 2))):
            Q_ma[i] = np.mean(Q[(i - int(np.floor(h_interv / 2))) : (i + int(np.ceil(h_interv / 2)))])
        elif i > ((len(Q) - 1) - (h_interv / 2)):
            Q_ma[i] = np.mean(Q[(i - (len(Q) - 1 - i)) : len(Q)])
        Q_ma[-1] = Q[-1]
    return Q_ma
  
