# -*- coding: utf-8 -*-
""" GERDPySim - 'boreholes.py'
    
    Class for boreholes and associated methods
    
    based on: Pygfunction by Massimo Cimmino

    Authors: Massimo Cimmino, Yannick Apfel, Meike Martin
"""
import numpy as np


class Borehole(object):
    """
    Contains information regarding the dimensions and position of a borehole.
 
    Attributes
    ----------
    H:              float
                    borehole depth [m]
    D:              float
                    borehole buried depth [m]
    r_b:            float
                    borehole radius [m]
    x:              float
                    position of the head of the borehole along the x-axis [m]
    y:              float
                    position of the head of the borehole along the y-axis [m]
    tilt:           float
                    angle from vertical of the axis of the borehole [m]
    orientation:    float
                    direction of the tilt of the borehole [radians]

    """

    def __init__(self, H, D, r_b, x, y, tilt=0., orientation=0.):
        self.H = float(H)
        self.D = float(D)
        self.r_b = float(r_b)
        self.x = float(x)
        self.y = float(y)
        self.tilt = float(tilt)
        self.orientation = float(orientation)

    def __repr__(self):
        s = ('Borehole(H={self.H}, D={self.D}, r_b={self.r_b}, x={self.x},'
             ' y={self.y}, tilt={self.tilt},'
             ' orientation={self.orientation})').format(self=self)
        return s

    def distance(self, target):
        """
        Evaluate the distance between the current borehole and a target
        borehole.

        Parameters
        ----------
        target : Borehole object
            Target borehole for which the distance is evaluated.

        Returns
        -------
        dis : float
            Distance (in meters) between current borehole and target borehole.

        .. Note::
           The smallest distance returned is equal to the borehole radius.
           This means that the distance between a borehole and itself is
           equal to r_b.

        Examples
        --------
        >>> b1 = gt.boreholes.Borehole(H=150., D=4., r_b=0.075, x=0., y=0.)
        >>> b2 = gt.boreholes.Borehole(H=150., D=4., r_b=0.075, x=5., y=0.)
        >>> b1.distance(b2)
        5.0

        """
        dis = max(self.r_b,
                  np.sqrt((self.x - target.x)**2 + (self.y - target.y)**2))
        return dis

    def position(self):
        """
        Returns the position of the borehole.

        Returns
        -------
        pos : tuple
            Position (x, y) (in meters) of the borehole.

        Raises
        ------
        SomeError

        See Also
        --------
        OtherModules

        Examples
        --------
        >>> b1 = gt.boreholes.Borehole(H=150., D=4., r_b=0.075, x=5., y=0.)
        >>> b1.position()
        (5.0, 0.0)

        """
        pos = (self.x, self.y)
        return pos


def field_from_file(self, filename):
    """
    Build a list of boreholes given coordinates and dimensions provided in a
    text file.

    Parameters
    ----------
    filename : str
        Absolute path to text file.

    Returns
    -------
    boreField : list of Borehole objects
        List of boreholes in the bore field.

    Notes
    -----
    The text file should be formatted as follows::

        # x   y     H     D
        0.    0.    100.  2.5
        5.    0.    100.  2.5
        0.    5.    100.  2.5
        0.    10.   100.  2.5
        0.    20.   100.  2.5

    """

    # Load data from file
    data = np.loadtxt(filename)
    # Build the bore field
    borefield = []
    if not self.ui.rb_depth.isChecked(): # equal borehole depth
        if np.size(data, 1) == 4:
            try:
                for line in data:
                    x = line[0]
                    y = line[1]
                    D = line[3]
                    H = self.ui.sb_depth_boreholes.value()
                    r_b = self.ui.sb_r_borehole.value()
                    borefield.append(Borehole(H, D, r_b, x=x, y=y))
            except IndexError:  # raises exception if only one borehole
                x = data[0]
                y = data[1]
                D = data[3]
                H = self.ui.sb_depth_boreholes.value()
                r_b = self.ui.sb_r_borehole.value()
                borefield.append(Borehole(H, D, r_b, x=x, y=y))
        else:
            try:
                for line in data:
                    x = line[0]
                    y = line[1]
                    D = line[2]
                    H = self.ui.sb_depth_boreholes.value()
                    r_b = self.ui.sb_r_borehole.value()
                    borefield.append(Borehole(H, D, r_b, x=x, y=y))
            except IndexError:  # raises exception if only one borehole
                x = data[0]
                y = data[1]
                D = data[2]
                H = self.ui.sb_depth_boreholes.value()
                r_b = self.ui.sb_r_borehole.value()
                borefield.append(Borehole(H, D, r_b, x=x, y=y))
    else: # varying depth
        try:
            for line in data:
                x = line[0]
                y = line[1]
                H = line[2]
                D = line[3]
                r_b = self.ui.sb_r_borehole.value()
                borefield.append(Borehole(H, D, r_b, x=x, y=y))
        except IndexError:  # raises exception if only one borehole
            x = data[0]
            y = data[1]
            H = data[2]
            D = data[3]
            r_b = self.ui.sb_r_borehole.value()
            borefield.append(Borehole(H, D, r_b, x=x, y=y))
    return borefield


def visualize_field(borefield):
    """
    Plot the top view and 3D view of borehole positions.

    Parameters
    ----------
    borefield : list
        List of boreholes in the bore field.

    Returns
    -------
    fig : figure
        Figure object (matplotlib).

    """
    import matplotlib.pyplot as plt
    from matplotlib.ticker import AutoMinorLocator
    from mpl_toolkits.mplot3d import Axes3D
    # -------------------------------------------------------------------------
    # Initialize figure
    # -------------------------------------------------------------------------
    LW = 1.5    # Line width
    bbox_props = dict(boxstyle="circle,pad=0.3", fc="white", ec="b", lw=LW)

    plt.rc('figure', figsize=(160.0/25.4, 80.0*4.0/4.0/25.4))
    fig = plt.figure()
    fig.suptitle('Boreholes')

    # -------------------------------------------------------------------------
    # Top view
    # -------------------------------------------------------------------------
    i = 0   # Initialize borehole index
    ax0 = fig.add_subplot(121)

    for borehole in borefield:
        i += 1  # Increment borehole index
        (x, y) = borehole.position()    # Extract borehole position
        # Add current borehole to the figure
        ax0.plot(x, y, 'k.')
        ax0.text(x, y, i, ha="center", va="center", size=9, bbox=bbox_props)

    # Configure figure axes
    ax0.set_xlabel('x (m)')
    ax0.set_ylabel('y (m)')
    ax0.set_title('Top view')
    plt.axis('equal')
    ax0.xaxis.set_minor_locator(AutoMinorLocator())
    ax0.yaxis.set_minor_locator(AutoMinorLocator())

    # -------------------------------------------------------------------------
    # 3D view
    # -------------------------------------------------------------------------
    i = 0   # Initialize borehole index
    ax1 = fig.add_subplot(122, projection='3d')

    for borehole in borefield:
        i += 1  # Increment borehole index
        # Position of head of borehole
        (x, y) = borehole.position()
        # Position of bottom of borehole
        x_H = x + borehole.H*np.sin(borehole.tilt)*np.cos(borehole.orientation)
        y_H = y + borehole.H*np.sin(borehole.tilt)*np.sin(borehole.orientation)
        z_H = borehole.D + borehole.H*np.cos(borehole.tilt)
        # Add current borehole to the figure
        ax1.plot(np.atleast_1d(x), np.atleast_1d(y), np.atleast_1d(borehole.D),
                 'ko')
        ax1.plot(np.array([x, x_H]),
                 np.array([y, y_H]),
                 -np.array([borehole.D, z_H]), 'k-')

    # Configure figure axes
    ax1.set_xlabel('x (m)')
    ax1.set_ylabel('y (m)')
    ax1.set_zlabel('z (m)')
    ax1.set_title('3D view')
    ax1.xaxis.set_minor_locator(AutoMinorLocator())
    ax1.yaxis.set_minor_locator(AutoMinorLocator())
    ax1.zaxis.set_minor_locator(AutoMinorLocator())

    # plt.tight_layout(rect=[0, 0.0, 0.95, 1.0])

    return fig


def length_field(borefield):
    '''
    Parameters
    ----------
    borefield: argument of class Borefield.

    Returns: total borehole metres of borefield.
    -------

    '''
    H_field = 0
    for i in range(len(borefield)):
        H_field += borefield[i].H
    return H_field
