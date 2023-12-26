# cython: language_level=3
import numpy as np
cimport numpy as np
import GERDPySim.utilities

cdef class _LoadAggregation:
    """
    Base class for load aggregation schemes.
    """

    def __init__(self, double dt, double tmax, int nSources=1):
        self.dt = dt                # Simulation time step
        self.tmax = tmax            # Maximum simulation time
        self.nSources = nSources    # Number of heat sources

    def initialize(self, g):
        raise NotImplementedError(
            'initialize class method not implemented, this '
            'method should do the start of simulation operations.')

    def get_times_for_simulation(self):
        raise NotImplementedError(
            'get_times_for_simulation class method not implemented, this '
            'method should return a list of time values at which the '
            'thermal response factors are needed.')

    def next_time_step(self, time):
        raise NotImplementedError(
            'next_time_step class method not implemented, this '
            'method should do the start of time step operations.')

    def set_current_load(self, Q):
        raise NotImplementedError(
            'set_current_load class method not implemented, this '
            'method should do the operations needed when setting current '
            'loads.')

    def temporal_superposition(self):
        raise NotImplementedError(
            'temporal_superposition class method not implemented, this '
            'method should return the borehole wall temperatures at the '
            'current time step.')

cdef class ClaessonJaved(_LoadAggregation):
    """
    Load aggregation algorithm of Claesson and Javed [#ClaessonJaved2012]_.

    Attributes
    ----------
    dt : float
        Simulation time step (in seconds).
    tmax : float
        Maximum simulation time (in seconds).
    nSources : int, optional
        Number of heat sources with independent load histories.
        Default is 1.
    cells_per_level : int, optional
        Number of load aggregation cells per level of aggregation. Cell widths
        double every cells_per_level cells.
        Default is 5.

    References
    ----------
    .. [#ClaessonJaved2012] Claesson, J., & Javed, S. (2012). A
       load-aggregation method to calculate extraction temperatures of
       borehole heat exchangers. ASHRAE Transactions, 118 (1): 530–539.
    """

    def __init__(self, double dt, double tmax, int nSources=1, int cells_per_level=5, **kwargs):
        super(ClaessonJaved, self).__init__(dt, tmax, nSources)
        # Initialize load aggregation cells
        self._build_cells(dt, tmax, nSources, cells_per_level)

    def initialize(self, g_d):
        """
        Initialize the thermal aggregation scheme.

        Creates a matrix of thermal response factor increments
        for later use in temporal superposition.

        Parameters
        ----------
        g_d : array
            Matrix of **dimensional** thermal response factors for temporal
            superposition (:math:`g/(2 \pi k_s)`).
            The expected size is (nSources, nSources, Nt), where Nt is the
            number of time values at which the thermal response factors are
            required. The time values are returned by
            :func:`~load_aggregation.ClaessonJaved.get_times_for_simulation`.
            If nSources=1, g_d can be 1 dimensional.

        """
        if self.nSources==1:
            g_d = g_d.reshape(1, 1, -1)
        # Build matrix of thermal response factor increments
        self.dg = np.zeros_like(g_d)
        self.dg[:,:,0] = g_d[:,:,0]
        for i in range(1, len(self._time)):
            self.dg[:,:,i] = g_d[:,:,i] - g_d[:,:,i-1]

    def next_time_step(self, time):
        """
        Shifts aggregated loads by one time step.

        Parameters
        ----------
        time : float
            Current value of time (in seconds).

        """
        for i in range(len(self._time)-2, -1, -1):
            # If the current time is greater than the time of cell (i+1),
            # remove one unit from cell (i+1) and add one unit of cell (i)
            # into cell (i+1).
            if time > self._time[i+1]:
                self.Q[:,i+1] = ((self._width[i+1] - 1)*self.Q[:,i+1]
                                 + self.Q[:,i])/self._width[i+1]
            # If the current time is greater than the time of cell (i) but less
            # than the time of cell (i+1), add one unit of cell (i) into cell
            # (i+1).
            elif time > self._time[i]:
                self.Q[:,i+1] = (self._width[i+1]*self.Q[:,i+1] + self.Q[:,i])\
                            /self._width[i+1]
        # Set the aggregated load of cell (0) to zero.
        self.Q[:,0:1] = 0.

    def get_thermal_response_factor_increment(self):
        """
        Returns an array of the **dimensional** thermal response factors.

        Returns
        -------
        dg : array
            Array of **dimensional** thermal response factor increments used
            for temporal superposition 
            (:math:`g(t_{i+1})/(2 \pi k_s) - g(t_{i})/(2 \pi k_s)`),
            in correspondance with the intialized values of the thermal
            response factors in 
            :func:`~load_aggregation.ClaessonJaved.initialize`.
            The output size of the array is (nSources, nSources, Nt) if
            nSources>1. If nSources=1, then the method returns a 1d array.

        """
        if self.nSources == 1:
            dg = self.dg.flatten()
        else:
            dg = self.dg
        return dg

    def get_times_for_simulation(self):
        """
        Returns a vector of time values at which the thermal response factors
        are required.

        Returns
        -------
        time_req : array
            Time values at which the thermal response factors are required
            (in seconds).

        """
        return self._time

    def set_current_load(self, Q):
        """
        Set the load at the current time step.

        Parameters
        ----------
        Q : array
            Current value of heat extraction rates per unit borehole length
            (in watts per meter).

        """
        self.Q[:,0:1] = Q

    def temporal_superposition(self):
        """
        Returns the borehole wall temperature variations at the current time
        step from the temporal superposition of past loads.

        Returns
        -------
        deltaT : array
            Values of borehole wall temperature drops at the current time step
            (in degC).

        .. Note::
           *pygfunction* assumes positive values for heat
           **extraction** and for borehole wall temperature **drops**. The
           borehole wall temperature are thus given by :
           :math:`T_b = T_g - \Delta T_b`.

        """
        deltaT = self.dg[:,:,0].dot(self.Q[:,0])
        for i in range(1, len(self._time)):
            deltaT += (self.dg[:,:,i]).dot(self.Q[:,i])
        return np.reshape(deltaT, (self.nSources, 1))

    cdef void _build_cells(self, double dt, double tmax, int nSources, int cells_per_level):
        """
        Initializes load aggregation cells.

        Parameters
        ----------
        dt : float
            Simulation time step (in seconds).
        tmax : float
            Maximum simulation time (in seconds).
        nSources : int
            Number of heat sources with independent load histories.
        cells_per_level : int
            Number of load aggregation cells per level of aggregation. Cell
            widths double every cells_per_level cells.

        """
        self._time = GERDPySim.utilities.time_ClaessonJaved(
                dt, tmax, cells_per_level=cells_per_level)
        self._width = np.hstack((1,
                                 (self._time[1:] - self._time[:-1])/dt))
        # Initialize aggregated loads
        self.Q = np.zeros((nSources, len(self._time)))
