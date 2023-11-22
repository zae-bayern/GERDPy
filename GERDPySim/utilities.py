# -*- coding: utf-8 -*-
""" GERDPySim - 'utilities.py'
    
    Auxiliary Functions

    Authors: Massimo Cimmino, Yannick Apfel, Meike Martin
"""
import numpy as np


def time_ClaessonJaved(dt, tmax, cells_per_level=5):
    """
    Build a time vector of expanding cell width following the method of
    Claesson and Javed [#ClaessonJaved2012]_.

    Parameters
    ----------
    dt : float
        Simulation time step (in seconds).
    tmax : float
        Maximum simulation time (in seconds).
    cells_per_level : int, optional
        Number of time steps cells per level. Cell widths double every
        cells_per_level cells.
        Default is 5.

    Returns
    -------
    time : array
        Time vector.

    Examples
    --------
    >>> time = gt.utilities.time_ClaessonJaved(3600., 12*3600.)
    array([3600.0, 7200.0, 10800.0, 14400.0, 18000.0, 25200.0, 32400.0,
           39600.0, 46800.0])

    References
    ----------
    .. [#ClaessonJaved2012] Claesson, J., & Javed, S. (2012). A
       load-aggregation method to calculate extraction temperatures of
       borehole heat exchangers. ASHRAE Transactions, 118 (1): 530-539.

    """
    # Initialize time (t), time vector (time) and cell count(i)
    t = 0.0
    i = 0
    time = []
    while t < tmax:
        # Increment cell count
        i += 1
        # Cell size doubles every cells_per_level time steps
        v = np.ceil(i / cells_per_level)
        width = 2.0**(v-1)
        t += width*float(dt)
        # Append time vector
        time.append(t)
    time = np.array(time)

    return time


def Q_moving_average(Q):
    h_interv = 25
    Q_ma = np.zeros(len(Q))
    for i in range(0, len(Q)):
        if i < (h_interv / 2):
            Q_ma[i] = np.mean(Q[0 : (2 * i + 1)])
        elif (i >= (h_interv / 2)) and (i <= ((len(Q) - 1) - (h_interv / 2))):
            Q_ma[i] = np.mean(Q[(i - int(np.floor(h_interv / 2))) : (i + int(np.ceil(h_interv / 2)))])
        elif i > ((len(Q) - 1) - (h_interv / 2)):
            Q_ma[i] = np.mean(Q[(i - (len(Q) - 1 - i)) : len(Q)])
        Q_ma[-1] = Q[-1]
        
    return Q_ma
