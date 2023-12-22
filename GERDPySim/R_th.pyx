# cython: language_level=3

from libc.math cimport sqrt, log, pi
from scipy.constants import Stefan_Boltzmann, R
import numpy as np
cimport numpy as np
from .boreholes import length_field

cpdef double R_th_c(list borefield):
    cdef:
        double phi = 0.8
        double lambda_a = 0.025
        double d = 1e-3
        double delta = 250 * 1e-6
        double C = 2.8
        double M = 0.02896
        double T = 283
        double c_pa = 1007
        double epsilon_B = 0.2
        double epsilon_W = 0.2
        double p = 100000
        double gamma, l_frei, C_WS, alpha_WP, alpha_rad, alpha_WS
        double r_b, H_field, R_th_c

    # Accommodation coefficient
    gamma = (10 ** (0.6 - (1000 / T + 1) / C) + 1) ** -1

    # Free path length of gas molecules
    l_frei = 2 * (2 - gamma) / gamma * sqrt(2 * pi * R * T / M) * \
        lambda_a / (p * (2 * c_pa - R / M))

    # Emission coefficient ratio
    C_WS = Stefan_Boltzmann / (1 / epsilon_W + 1 / epsilon_B - 1)

    # Proportion of heat conduction
    alpha_WP = 4 * lambda_a / d * ((1 + 2 * (l_frei + delta) / d) *
                                   log(1 + d / (2 * (l_frei + delta)))
                                   - 1)

    # Proportion of radiation
    alpha_rad = 4 * C_WS * T ** 3

    # Heat transfer coefficient wall-to-backfill
    alpha_WS = phi * alpha_WP + alpha_rad

    # Thermal contact resistance of the borehole field
    r_b = borefield[0].r_b
    H_field = length_field(borefield)

    R_th_c = (2 * pi * r_b * alpha_WS * H_field) ** -1

    return R_th_c

cpdef double R_th_b(double lambda_g, list borefield, object hp):
    cdef:
        int N = hp.N
        double r_b = borefield[0].r_b
        double r_iso_b = hp.r_iso_b
        double r_pa = hp.r_pa
        double r_pi = hp.r_pi
        double lambda_b = hp.lambda_b
        double lambda_iso = hp.lambda_iso
        double lambda_p = hp.lambda_p
        double sigma, r_pm, b_m, b_mn, b_mn_
        double R_th_b
        np.ndarray R_mn_0 = np.zeros([N, N])
        int i, j
        double x_m, y_m, x_n, y_n

    # Borefield & borehole geometry
    H_field = length_field(borefield) # total borehole depth [m]

    # Ratio of thermal conductivities
    sigma = (lambda_b - lambda_g) / (lambda_b + lambda_g)

    # Thermal resistance of heat pipe + insulation layer
    r_pm = log(r_iso_b / r_pa) / (2 * pi * lambda_iso) + \
           log(r_pa / r_pi) / (2 * pi * lambda_p)

    # Coordinate-dependent coefficients
    for i in range(N):
        for j in range(N):
            x_m = hp.xy_mat[i, 0]
            y_m = hp.xy_mat[i, 1]
            x_n = hp.xy_mat[j, 0]
            y_n = hp.xy_mat[j, 1]
            if i == j:
                R_mn_0[i, j] = (2 * pi * lambda_b) ** -1 * (log(r_b / r_pa) - sigma * log(1 - (sqrt(x_m ** 2 + y_m ** 2) / r_b) ** 2)) + r_pm
            else:
                R_mn_0[i, j] = - (2 * pi * lambda_b) ** -1 * (log(sqrt((x_n - x_m) ** 2 + (y_n - y_m) ** 2) / r_b) - sigma * log(sqrt((1 - (sqrt(x_m ** 2 + y_m ** 2) / r_b) ** 2) * (1 - (sqrt(x_n ** 2 + y_n ** 2) / r_b) ** 2) + (sqrt((x_n - x_m) ** 2 + (y_n - y_m) ** 2) / r_b) ** 2)))

    # Calculation of borehole thermal resistance
    R_th_b = (sum(sum(np.linalg.inv(R_mn_0))) * H_field) ** -1

    return R_th_b

cpdef double R_th_hp(list borefield, object hp):
    cdef:
        int N = hp.N
        int N_b = len(borefield)
        double delta_y = 500
        double delta_x = 1
        double R_th_hp

    R_th_hp = delta_x / (delta_y * N * N_b)

    return R_th_hp

cpdef double R_th_he(object he):
    cdef:
        double x_o, x_u, Theta_R = 1, Theta_inf_o = 0, R_th_he
        double l_p_he, q_l

    # Auxiliary params
    x_o = he.x_min + 0.5 * he.d_pa  # vertical pipe-centre-to-surface distance [m]
    x_u = he.D_he - x_o  # vertical pipe-centre-to-underside distance [m]

    # Thermal resistance [K/W] --> R_th = 1 K / (q_l * l_p_he)
    l_p_he = he.l_p_he
    q_l = he.q_l(x_o, x_u, he.d_pa, he.d_pi, he.lambda_c, he.lambda_p, he.s_R, Theta_R, Theta_inf_o, state_u_insul=True)
    R_th_he = (l_p_he * q_l) ** -1

    return R_th_he
