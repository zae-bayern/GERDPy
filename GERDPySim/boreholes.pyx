# cython: language_level=3

import numpy as np
cimport numpy as np
from libc.math cimport sqrt

cdef class Borehole:
    cdef public:
        double H, D, r_b, x, y, tilt, orientation

    def __init__(self, double H, double D, double r_b, double x, double y, double tilt=0., double orientation=0.):
        self.H = H
        self.D = D
        self.r_b = r_b
        self.x = x
        self.y = y
        self.tilt = tilt
        self.orientation = orientation

    def __repr__(self):
        return (f'Borehole(H={self.H}, D={self.D}, r_b={self.r_b}, x={self.x}, '
                f'y={self.y}, tilt={self.tilt}, orientation={self.orientation})')

    cpdef double distance(self, Borehole target):
        return max(self.r_b, sqrt((self.x - target.x) ** 2 + (self.y - target.y) ** 2))

    cpdef tuple position(self):
        return (self.x, self.y)

cpdef list field_from_file(str filename):
    cdef list borefield = []
    cdef np.ndarray data = np.loadtxt(filename)
    cdef double x, y, D, H, r_b
    cdef int i

    for i in range(data.shape[0]):
        x = data[i, 0]
        y = data[i, 1]
        D = data[i, 3]
        H = data[i, 2]  # Assuming H is at index 2
        r_b = data[i, 4]  # Assuming r_b is at index 4
        borefield.append(Borehole(H, D, r_b, x, y))

    return borefield

cpdef visualize_field(list borefield):
    import matplotlib.pyplot as plt
    from matplotlib.ticker import AutoMinorLocator
    from mpl_toolkits.mplot3d import Axes3D

    LW = 1.5  # Line width
    bbox_props = dict(boxstyle="circle,pad=0.3", fc="white", ec="b", lw=LW)

    plt.rc('figure', figsize=(160.0/25.4, 80.0*4.0/4.0/25.4))
    fig = plt.figure()
    fig.suptitle('Boreholes')

    # Top view
    ax0 = fig.add_subplot(121)
    for borehole in borefield:
        (x, y) = borehole.position()
        ax0.plot(x, y, 'k.')
        ax0.text(x, y, str(borehole), ha="center", va="center", size=9, bbox=bbox_props)
    ax0.set_xlabel('x (m)')
    ax0.set_ylabel('y (m)')
    ax0.set_title('Top view')
    plt.axis('equal')
    ax0.xaxis.set_minor_locator(AutoMinorLocator())
    ax0.yaxis.set_minor_locator(AutoMinorLocator())

    # 3D view
    ax1 = fig.add_subplot(122, projection='3d')
    for borehole in borefield:
        (x, y) = borehole.position()
        x_H = x + borehole.H * np.sin(borehole.tilt) * np.cos(borehole.orientation)
        y_H = y + borehole.H * np.sin(borehole.tilt) * np.sin(borehole.orientation)
        z_H = borehole.D + borehole.H * np.cos(borehole.tilt)
        ax1.plot([x], [y], [borehole.D], 'ko')
        ax1.plot([x, x_H], [y, y_H], [-borehole.D, -z_H], 'k-')
    ax1.set_xlabel('x (m)')
    ax1.set_ylabel('y (m)')
    ax1.set_zlabel('z (m)')
    ax1.set_title('3D view')
    ax1.xaxis.set_minor_locator(AutoMinorLocator())
    ax1.yaxis.set_minor_locator(AutoMinorLocator())
    ax1.zaxis.set_minor_locator(AutoMinorLocator())

    return fig

cpdef double length_field(list borefield):
    cdef double H_field = 0
    cdef int i

    for i in range(len(borefield)):
        H_field += borefield[i].H

    return H_field
