# -*- coding: utf-8 -*-
""" GERDPySim - 'R_th.py'
    
    Module for the thermal resistances in the system
    
    1.) R_th_c - ground-to-backfill thermal contact resistance

        - [VDI-Wärmeatlas 2013 - Wärmeübergangskoeffizient Wand-Schüttung]
        
    2.) R_th_b - borehole thermal resistance

        - [Hellström 1991 - Line source approximation]
        - N heatpipes uniformly arranged around a circle in the borehole

    3.) R_th_hp - thermal resistance of the thermosiphon heatpipes

        - The complex two-phase flow phenomena are not modelled (e. g. the entrainment limit),
          instead, the thermal resistance follows a simple linear power-over-delta-T characteristic:
              - R_th_hp = 1 K / (500 W * N * N_b)
              
              N - number of heatpipes per borehole
              N_b - number of boreholes in the borefield
    
    4.) R_th_he - thermal resistance of the heating element

        - analytical series solution for the heat flow in a pipe register with
          equidistant tubes according to VDI 2055-1 (Dirichlet temperature boundary condition)
        - variable parameters:
            - minimum vertical pipe-to-surface distance x_min [m]
            - thermal conductivities of the heating element material (concrete) and
              heatpipe material (stainless steel) [W/mK]
            - piping sizes inside heating element (diameter, heatpipe distance,
                                             heatpipe length) [m]
             
    Authors: Yannick Apfel, Meike Martin
    
"""
# R_th_c - ground-to-backfill thermal contact resistance
def R_th_c(borefield):

    import math, GERDPySim.boreholes
    from scipy.constants import pi, R, Stefan_Boltzmann
    from .boreholes import length_field

    # 1.) Params

    phi = 0.8               # surface coverage ratio [-]
    lambda_a = 0.025        # thermal conductivity of air [W/mK]
    d = 1e-3                # particle diameter [m]
    delta = 250 * 1e-6      # particle surface roughness [m]
    C = 2.8                 # material constant [-]
    M = 0.02896             # molar mass of gas [kg/mol]
    T = 283                 # contact zone temperature [K]
    c_pa = 1007             # specific heat capacity of gas [J/kgK]
    epsilon_B = 0.2         # emission coefficient of backfill [-]
    epsilon_W = 0.2         # emission coefficient of wall [-]
    p = 100000              # pressure [Pa]

    # 2a.) Auxiliary params

    # accommodation coefficient
    gamma = (10 ** (0.6 - (1000 / T + 1) / C) + 1) ** -1

    # free path length of gas molecules
    l_frei = 2 * (2 - gamma) / gamma * math.sqrt(2 * pi * R * T / M) * \
        lambda_a / (p * (2 * c_pa - R / M))

    # emission coefficient ratio
    C_WS = Stefan_Boltzmann / (1 / epsilon_W + 1 / epsilon_B - 1)

    # 2b.) Heat transfer coefficient wall-to-backfill

    # proportion of heat conduction
    alpha_WP = 4 * lambda_a / d * ((1 + 2 * (l_frei + delta) / d) *
                                   math.log(1 + d / (2 * (l_frei + delta)))
                                   - 1)

    # proportion of radiation
    alpha_rad = 4 * C_WS * T ** 3

    # heat transfer coefficient wall-to-backfill
    alpha_WS = phi * alpha_WP + alpha_rad

    # 3.) thermal contact resistance of the borehole field

    r_b = borefield[0].r_b
    H_field = length_field(borefield)

    R_th_c = (2 * pi * r_b * alpha_WS * H_field) ** -1

    return R_th_c


# R_th_b - borehole thermal resistance
def R_th_b(lambda_g, borefield, hp):

    import math
    import numpy as np
    from numpy.linalg import inv
    from scipy.constants import pi
    from .boreholes import length_field

    # 1.) Params

    # Borefield & borehole geometry
    H_field = length_field(borefield) # total borehole depth [m]
    r_b = borefield[0].r_b  # borehole radius [m]

    # Heatpipe geometry
    N = hp.N  # no. of heatpipes per borehole [-]
    r_iso_b = hp.r_iso_b  # outer radius of heatpipe insulation [m]
    r_pa = hp.r_pa  # outer radius of heatpipes [m]
    r_pi = hp.r_pi  # inner radius of heatpipes [m]

    # Thermal conductivities [W/mK]:
    # lambda_g (imported)
    lambda_b = hp.lambda_b  # borehole backfill
    lambda_iso = hp.lambda_iso  # insulation material
    lambda_p = hp.lambda_p  # heatpipe material

    # 2a.) Coordinates of heatpipe centres (borehole centre as origin)

    xy = hp.xy_mat()  # 1. column: x, 2. column: y

    # 2b.) Auxiliary variables

    # Ratio of thermal conductivities
    sigma = (lambda_b - lambda_g) / (lambda_b + lambda_g)

    # Thermal resistance of heat pipe + insulation layer
    r_pm = math.log(r_iso_b / r_pa) / (2 * pi * lambda_iso) + \
        math.log(r_pa / r_pi) / (2 * pi * lambda_p)
    # r_pm = 0 (in case the thermal resistance is supposed to be neglected)

    # Coordinate-dependent coefficients
    b_m = lambda x_m, y_m: math.sqrt(x_m ** 2 + y_m ** 2) / r_b
    b_mn = lambda x_n, x_m, y_n, y_m: math.sqrt((x_n - x_m) ** 2 + (y_n - y_m) ** 2) / r_b
    b_mn_ = lambda b_m, b_n, b_mn: math.sqrt((1 - b_m ** 2) * (1 - b_n ** 2) + b_mn ** 2)

    # Borehole coefficient matrix

    R_mn_0 = np.zeros([N, N])

    # Populate borehole coefficient matrix
    for i in range(N):          # iterate for m
        for j in range(N):      # iterate for n
            if i == j:
                R_mn_0[i, j] = \
                    (2 * pi * lambda_b) ** -1 * (math.log(r_b / r_pa)
                    - sigma * math.log(1 - b_m(xy[i, 0], xy[i, 1]) ** 2)) + r_pm
            else:
                R_mn_0[i, j] = \
                    - (2 * pi * lambda_b) ** -1 * (math.log(b_mn(xy[j, 0], xy[i, 0], xy[j, 1], xy[i, 1]))
                    - sigma * math.log(b_mn_(b_m(xy[i, 0], xy[i, 1]), b_m(xy[j, 0], xy[j, 1]), b_mn(xy[j, 0], xy[i, 0], xy[j, 1], xy[i, 1]))))

    # 3.) Calculation of borehole thermal resistance

    R_th_b = (sum(sum(inv(R_mn_0))) * H_field) ** -1

    return R_th_b


# R_th_hp - thermal resistance of the thermosiphon heatpipes
def R_th_hp(borefield, hp):

    # 1.) Params

    N = hp.N  # number of heatpipes per borehole [-]
    N_b = len(borefield)  # number of boreholes in the borefield [-]

    # linear slope of the characteristic (delta_y / delta_x)
    delta_y = 500       # thermal power per heatpipe [W]
    delta_x = 1         # delta_T [K]

    # 2.) thermal resistance of the thermosiphon heatpipes

    R_th_hp = delta_x / (delta_y * N * N_b)

    return R_th_hp


# R_th_he - thermal resistance of the heating element
def R_th_he(he):  # heating element thermal resistance [K/W]

    from .heating_element_utils import q_l

    # 1.) auxiliary params
    x_o = he.x_min + 0.5 * he.d_pa  # vertical pipe-centre-to-surface distance [m]
    x_u = he.D_he - x_o  # vertical pipe-centre-to-underside distance [m]

    # 2.) delta-T between pipe wall and surface set to delta-T := 1 K
    Theta_R = 1
    Theta_inf_o = 0

    # 3.) thermal resistance [K/W] --> R_th = 1 K / (q_l * l_p_he)
    ''' heating element underside is parametrized as perfectly insulated: state_u_insul=True
    '''
    R_th_he = (he.l_p_he * q_l(x_o, x_u, he.d_pa, he.d_pi, he.lambda_c, he.lambda_p, he.s_R, Theta_R, Theta_inf_o,
                            state_u_insul=True)) ** -1

    return R_th_he
