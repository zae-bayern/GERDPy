# -*- coding: utf-8 -*-
""" GERDPySim - 'load_generator.py'

    Module serves as the load model of the system. The surface load is determined through 
    the steady state coupling of ground, borehole and surface.
    
    The load is determined through a steady-state power balance on the surface for each timestep.
    The thermal load components on the surface:
        
        lat - latent heat of snow/ice
        sen - sensible of snow/ice
        con - convection
        rad - radiation
        eva - evaporation
        
    are in equilibrium with the whole system load and determine the power which is extracted from the ground.
    The load is propagated from surface to ground via the system thermal resistance R_th and equally distributed
    among all boreholes acc. to their respective borehole depths.
    
    System thermal power:

        Q. = (Theta_b - Theta_surf) / R_th_tot 
           = Q._lat + Q._sen + R_f * (Q._con + Q._rad + Q._eva)
   
    Power balance: F_Q = Q._lat + Q._sen + R_f * (Q._con + Q._rad + Q._eva) - Q. = 0
        - includes: {ground, surface, surroundings}
    
    Reduced power balance: F_T = Q._lat + Q._sen + R_f * (Q._con + Q._rad + Q._eva) = 0
        - includes: {surface, surroundings}
        
    Simulation cases:
        
            - Theta_b >= Theta_surf:
                - Q. > 0 (positive extracted power)
                - F_Q = 0 solved for thermal power Q.

            - Theta_b < Theta_surf:
                - Q. = 0 (no power extracted from the ground)
                - F_T = 0 solved for surface temperature Theta_surf
                
    Solver: iterative search for zero crossing
    
    Algorithm is based in part on [Konrad 2009] and [Fuchs 2020]

    Authors: Yannick Apfel, Meike Martin
"""
import math
from scipy.constants import sigma

# import physical model equations
from .load_generator_utils import *
from .heating_element_utils import *


# Q_convection = fct(Q.) - Input for power balance F_Q = 0
def Q_con_Q(Q, con, u_inf, Theta_b_0, R_th, Theta_inf, A_he):  # [W]
    Q_con = 0
    if con:
        Q_con = alpha_con_he_o(u_inf) * (Theta_b_0 - Q * R_th - Theta_inf) * A_he

    return Q_con


# Q_convection = fct(Theta_surf) - Input for reduced power balance F_T = 0
def Q_con_T(Theta_surf, con, u_inf, Theta_inf, A_he):  # [W]
    Q_con = 0
    if con:
        Q_con = alpha_con_he_o(u_inf) * (Theta_surf - Theta_inf) * A_he

    return Q_con


# Q_radiation = fct(Q.) - Input for power balance F_Q = 0
def Q_rad_Q(Q, rad, Theta_b_0, R_th, S_r, Theta_inf, B, Phi, A_he):  # [W]
    Q_rad = 0
    if rad:
        Q_rad = sigma * epsilon_surf('concrete') * ((Theta_b_0 - Q * R_th + 273.15) ** 4 - T_MR(S_r, Theta_inf, B, Phi) ** 4) * A_he

    return Q_rad


# Q_radiation = fct(Theta_surf) - Input for reduced power balance F_T = 0
def Q_rad_T(Theta_surf, rad, S_r, Theta_inf, B, Phi, A_he):  # [W]
    Q_rad = 0
    if rad:
        Q_rad = sigma * epsilon_surf('concrete') * ((Theta_surf + 273.15) ** 4 - T_MR(S_r, Theta_inf, B, Phi) ** 4) * A_he

    return Q_rad


# Q_evaporation = fct(Q.) - Input for power balance F_Q = 0
def Q_eva_Q(Q, eva, Theta_surf_0, m_w_0, Theta_inf, u_inf, z_asl, Theta_b_0, R_th, Phi, A_he):  # [W]
    ''' Prerequisites:
        - Theta_surf >= 0 °C
        - Surface is wet (m_Rw > 0)
    '''
    Q_eva = 0
    if (eva and Theta_surf_0 >= 0 and m_w_0 > 0):
        Q_eva = rho_a * beta_c(Theta_inf, u_inf, z_asl) * (X_sat_surf(Theta_b_0 - Q * R_th, z_asl) - X_inf(Theta_inf, Phi, z_asl)) * h_Ph_lg * A_he

    if Q_eva < 0:  # evaporative power flux cannot be negative!
        Q_eva = 0

    return Q_eva


# Q_evaporation = fct(Theta_surf) - Input for reduced power balance F_T = 0
def Q_eva_T(Theta_surf, eva, Theta_surf_0, m_w_0, Theta_inf, u_inf, z_asl, Phi, A_he):  # [W]
    ''' Prerequisites:
        - Theta_surf >= 0 °C
        - Surface is wet (m_Rw > 0)
    '''
    Q_eva = 0
    if (eva and Theta_surf_0 >= 0 and m_w_0 > 0):
        Q_eva = rho_a * beta_c(Theta_inf, u_inf, z_asl) * (X_sat_surf(Theta_surf, z_asl) - X_inf(Theta_inf, Phi, z_asl)) * h_Ph_lg * A_he

    if Q_eva < 0:  # evaporative power flux cannot be negative!
        Q_eva = 0

    return Q_eva


# Q_sensible = fct(Q.) - Input for power balance F_Q = 0
def Q_sen_Q(Q, sen, S_r, Theta_inf, Theta_b_0, R_th, A_he):  # [W]
    Q_sen = 0
    if sen:
        Q_sen = rho_w * S_r * (c_p_s * (Theta_mp - Theta_inf) + c_p_w * (Theta_b_0 - Q * R_th - Theta_mp)) * (3.6e6)**-1 * A_he

    return Q_sen


# Q_sensible = fct(Theta_surf) - Input for reduced power balance F_T = 0
def Q_sen_T(Theta_surf, sen, S_r, Theta_inf, A_he):  # [W]
    Q_sen = 0
    if sen:
        Q_sen = rho_w * S_r * (c_p_s * (Theta_mp - Theta_inf) + c_p_w * (Theta_surf - Theta_mp)) * (3.6e6)**-1 * A_he

    return Q_sen


# Q_latent - identical for both non-reduced and reduced power balances F_Q = 0 and F_T = 0
def Q_lat(lat, S_r, A_he):  # [W]
    Q_lat = 0
    if lat:
        Q_lat = rho_w * S_r * h_Ph_sl * (3.6e6)**-1 * A_he

    return Q_lat


""" Thermal losses on heating element underside and via borehole-to-heating element connections
    Q_V = Q_V_an + Q_V_he

    Q_V_an: thermal losses via borehole-to-heating element connections
        - Modelled by means of Péclet-equation for cylindrical shells (pipe + insulation) with the total length of all heat pipes
          in the area of the connection
        - Determination of the internal pipe temperature via borehole temperature Theta_b and the thermal ground-to-heatpipe resistance R_th_g_hp
        - convective heat transfer on the outer radius of the connection piping

    Q_V_he: thermal losses on the underside of the heating element
        - R_th_he_u: piping inside heating element to heating element underside (without insulation)
        - R_th_he_iso: insulation layer on underside of heating element
"""
def Q_V(Theta_R, Theta_inf, lambda_p, lambda_iso, l_R_An, r_iso, r_pa, r_pi, he):
    
    def Q_V_an(Theta_R, Theta_inf, lambda_p, lambda_iso, l_R_An, r_iso, r_pa, r_pi):  # [W]

        Q_V_an = (Theta_R - Theta_inf) * (2 * math.pi * l_R_An) \
                * (math.log(r_pa / r_pi) / lambda_p + math.log(r_iso / r_pa) / lambda_iso
                    + 1 / (alpha_con_an(Theta_R - Theta_inf) * r_iso)) ** -1
        if Q_V_an < 0:  # wickless thermosiphons don't allow negative heat flux (into the ground)
            Q_V_an = 0

        return Q_V_an
    
    def Q_V_he(he, lambda_iso, Theta_R, Theta_inf):  # [W]
        
        # thermal resistance piping-to-underside (without insulation)
        R_th_he_u = (he.l_p_he * q_l(he.D_he - (he.x_min + 0.5 * he.d_pa), (he.x_min + 0.5 * he.d_pa), he.d_pa, he.d_pi, he.lambda_c, he.lambda_p, he.s_R, 1, 0, state_u_insul=True)) ** -1

        # thermal resistance of insulation layer on underside
        R_th_he_iso = 1 / lambda_iso * he.D_iso_he / he.A_he
        
        # thermal transfer resistance insulation-to-surroundings
        R_th_he_alpha = (alpha_con_he_u() * he.A_he) ** -1
        
        Q_V_he = (Theta_R - Theta_inf) * (R_th_he_u + R_th_he_iso + R_th_he_alpha) ** -1
        if Q_V_he < 0:  # wickless thermosiphons don't allow negative heat flux (into the ground)
            Q_V_he = 0
    
        return Q_V_he
    
    Q_V = Q_V_an(Theta_R, Theta_inf, lambda_p, lambda_iso, l_R_An, r_iso, r_pa, r_pi) + Q_V_he(he, lambda_iso, Theta_R, Theta_inf)
    
    return Q_V


# Power balance F_Q (= 0)
def F_Q(R_f, lat, S_r, Q, sen, Theta_inf, Theta_b_0, R_th, con, u_inf, rad, eva, Theta_surf_0, m_w_0, z_asl, Phi, B, A_he):

    F_Q = Q_lat(lat, S_r, A_he) \
        + Q_sen_Q(Q, sen, S_r, Theta_inf, Theta_b_0, R_th, A_he) \
        + R_f \
        * (Q_con_Q(Q, con, u_inf, Theta_b_0, R_th, Theta_inf, A_he)
        + Q_rad_Q(Q, rad, Theta_b_0, R_th, S_r, Theta_inf, B, Phi, A_he)
        + Q_eva_Q(Q, eva, Theta_surf_0, m_w_0, Theta_inf, u_inf, z_asl, Theta_b_0, R_th, Phi, A_he)) \
        - Q

    return F_Q


# Reduced power balance F_T (= 0)
def F_T(R_f, lat, S_r, Theta_surf, sen, Theta_inf, con, u_inf, rad, eva, Theta_surf_0, m_w_0, z_asl, Phi, B, A_he):
    F_T = Q_lat(lat, S_r, A_he) \
        + Q_sen_T(Theta_surf, sen, S_r, Theta_inf, A_he) \
        + R_f \
        * (Q_con_T(Theta_surf, con, u_inf, Theta_inf, A_he)
        + Q_rad_T(Theta_surf, rad, S_r, Theta_inf, B, Phi, A_he)
        + Q_eva_T(Theta_surf, eva, Theta_surf_0, m_w_0, Theta_inf, u_inf, z_asl, Phi, A_he))

    return F_T


# Solver for F_Q = 0, solved for the system thermal power Q.
def solve_F_Q(R_f, con, rad, eva, sen, lat, S_r, Theta_inf, Theta_b_0, R_th, u_inf, Theta_surf_0, m_w_0, z_asl, Phi, B, A_he):
    step_refine = 0  # auxiliary variable for refining the iteration step size for Q.
    step = 100  # starting value for stepsize
    res = 0.001  # maximum allowed residual of F_Q for the optimization

    Q = 0  # starting value for Q.

    error = abs(F_Q(R_f, lat, S_r, Q, sen, Theta_inf, Theta_b_0, R_th, con, u_inf, rad, eva, Theta_surf_0, m_w_0, z_asl, Phi, B, A_he))

    # solves F_Q = 0 for Q. (iterative search for zero crossing)
    while error > res:
        step_refine += 1
        step = step / (2 * step_refine)  # step size reduction for each zero crossing
        if F_Q(R_f, lat, S_r, Q, sen, Theta_inf, Theta_b_0, R_th, con, u_inf, rad, eva, Theta_surf_0, m_w_0, z_asl, Phi, B, A_he) > 0:
            while F_Q(R_f, lat, S_r, Q, sen, Theta_inf, Theta_b_0, R_th, con, u_inf, rad, eva, Theta_surf_0, m_w_0, z_asl, Phi, B, A_he) > 0:
                Q += step  # increases Q. by stepsize if F_Q > 0
        elif F_Q(R_f, lat, S_r, Q, sen, Theta_inf, Theta_b_0, R_th, con, u_inf, rad, eva, Theta_surf_0, m_w_0, z_asl, Phi, B, A_he) < 0:
            while F_Q(R_f, lat, S_r, Q, sen, Theta_inf, Theta_b_0, R_th, con, u_inf, rad, eva, Theta_surf_0, m_w_0, z_asl, Phi, B, A_he) < 0:
                Q -= step  # decreases Q. by stepsize if F_Q < 0

        # re-evaluate residual
        error = abs(F_Q(R_f, lat, S_r, Q, sen, Theta_inf, Theta_b_0, R_th, con, u_inf, rad, eva, Theta_surf_0, m_w_0, z_asl, Phi, B, A_he))

    # Evaluate the thermal load components for the determined Q.
    Q_lat_sol = Q_lat(lat, S_r, A_he)
    Q_sen_sol = Q_sen_Q(Q, sen, S_r, Theta_inf, Theta_b_0, R_th, A_he)
    Q_eva_sol = Q_eva_Q(Q, eva, Theta_surf_0, m_w_0, Theta_inf, u_inf, z_asl, Theta_b_0, R_th, Phi, A_he)
    Q_sol = Q

    return Q_sol, Q_lat_sol, Q_sen_sol, Q_eva_sol


# Solver for F_T = 0, solved for the surface temperature Theta_surf
def solve_F_T(R_f, con, rad, eva, sen, lat, S_r, Theta_inf, u_inf, Theta_surf_0, m_w_0, z_asl, Phi, B, A_he):
    step_refine = 0  # auxiliary variable for refining the iteration step size for Q.
    step = 100  # starting value for stepsize
    res = 0.001  # maximum allowed residual of F_T for the optimization

    Theta_surf = 0  # starting value for Theta_surf

    error = abs(F_T(R_f, lat, S_r, Theta_surf, sen, Theta_inf, con, u_inf, rad, eva, Theta_surf_0, m_w_0, z_asl, Phi, B, A_he))

    # solves F_T = 0 for Theta_surf (iterative search for zero crossing)
    while error > res:
        step_refine += 1
        step = step / (2 * step_refine)  # step size reduction for each zero crossing
        if F_T(R_f, lat, S_r, Theta_surf, sen, Theta_inf, con, u_inf, rad, eva, Theta_surf_0, m_w_0, z_asl, Phi, B, A_he) > 0:
            while F_T(R_f, lat, S_r, Theta_surf, sen, Theta_inf, con, u_inf, rad, eva, Theta_surf_0, m_w_0, z_asl, Phi, B, A_he) > 0: 
                Theta_surf -= step  # decreases Theta_surf by stepsize if F_T > 0
        elif F_T(R_f, lat, S_r, Theta_surf, sen, Theta_inf, con, u_inf, rad, eva, Theta_surf_0, m_w_0, z_asl, Phi, B, A_he) < 0:
            while F_T(R_f, lat, S_r, Theta_surf, sen, Theta_inf, con, u_inf, rad, eva, Theta_surf_0, m_w_0, z_asl, Phi, B, A_he) < 0:
                Theta_surf += step  # increases Theta_surf by stepsize if F_T < 0

        error = abs(F_T(R_f, lat, S_r, Theta_surf, sen, Theta_inf, con, u_inf, rad, eva, Theta_surf_0, m_w_0, z_asl, Phi, B, A_he))

    # Evaluate the thermal load components for the determined Theta_surf
    Q_lat_sol = Q_lat(lat, S_r, A_he)
    Q_sen_sol = Q_sen_T(Theta_surf, sen, S_r, Theta_inf, A_he)
    Q_eva_sol = Q_eva_T(Theta_surf, eva, Theta_surf_0, m_w_0, Theta_inf, u_inf, z_asl, Phi, A_he)
    Theta_surf_sol = Theta_surf

    return Theta_surf_sol, Q_lat_sol, Q_sen_sol, Q_eva_sol


def load(z_asl, v, Theta_inf, S_r, he, Theta_b_0, R_th, R_th_ghp, Theta_surf_0, B, Phi, RR, m_w_0, m_s_0, start_sb, 
         l_R_An, lambda_p, lambda_iso, r_iso, r_pa, r_pi, R_f):
    ''' Main algorithm for surface load calculation
                    
        Simulation modes 1-5:
            - ~ 1-3: a layer of snow/ice forms on the heating element surface 
                     (melting process is delayed and takes longer than one timestep)
            - ~ 4-5: the heating surface is free of snow/ice
                     (snow/ice is melted "instantaneously", within the timestep)
            
        Legend: (* - placeholder for variable)
            - *_sol: evaluated parameters generated e.g. from the steady state power balances on the heating element surface
            - *_0: parameter containing value from preceding timestep is used for calculation, as the current value is yet tbd
            - Q_N: net used power (power used for melting snow & ice)
            - Q_V: thermal power losses via connection & heating element underside
    '''

    # 0.) Preprocessing
    u_inf = u_eff(v)  # wind-shear-corrected wind speed (logarithmic)

    # Auxiliary variables
    ''' calc_T:
        "False": - surface temperature Theta_surf is calculated in 'main.py'
                 - utilizes Q_sol from evaluation of power balance F_Q = 0 (above)
                 - applies to simulation modes 2 & 4
        "True":  - surface temperature is calculated in this module
                 - applies to simulation modes 1, 3 & 5
                     - in case 1 & 5: Theta_surf_sol from evaluation of reduced power balance F_T = 0 is utilized (Q. = 0)
                     - in case 3: Theta_surf is set to melting point of water: Theta_surf := Theta_mp
    '''
    calc_T = False
    Theta_surf_sol = None

    # Identify simulation mode of current timestep
    ''' sb_active:
        "True": snow balancing is activated: a layer of snow/ice may form on the surface
        "False": snow balancing is deactivated: any snow/ice is melted from the surface instantaneously (within the current timestep)
    '''
    if (m_s_0 > 0 or start_sb is True):  # activate snow balancing
        sb_active = 1
    else:  # deactivate snow balancing
        sb_active = 0

    # 1.) Thermal load components
    con = True  # activate or deactivate (for unit-testing)
    rad = True
    eva = True
    sen = True
    lat = True

    # 2.) Calculate Q_sol and Theta_surf_sol (for each simulation mode)
    ''' Simulation modes 1-3'''
    if (sb_active == 1):

        ''' Simulation modes 1-3 encompass all modes of snow/ice layer forming on the surface
            
            1.) Q._0 encompasses the available power inside the ground (corresponds to the available temperature spread delta-T):
                
                Q._0 = (Theta_b - Theta_surf) / R_th_tot
            
            2.) Q._R encompasses the part of Q._0, that is available for melting snow/ice (latent & sensible)
                after subtracting surface losses (convection, radiation & evaporation)
                
                Q._R = Q._0 - (Q._con + Q._rad + Q._eva)
                
            Simulation mode 1: Q._0 < 0
            - no temperature spread available inside the ground (Sibirian conditions, ground is frozen or cooled down too much)
            - F_T = 0 solved for Theta_surf

            Simulation mode 2: Q._0 >= 0, Q._R < 0
            - temperature spread is not sufficient to melt snow/ice, the available power is used up for 
              surface losses (convection, radiation, evaporation)
            - F_Q = 0 solved for Q.
            
            Simulation mode 3: Q._0 >= 0, Q._R >= 0
            - temperature spread is sufficient to melt snow/ice
            - only simulation mode where snow/ice are melted!
            - no power balancing, instead, the melted snow/ice volume flux is estimated using Q._R:
                V._s = V._s(Q._R)
            - Theta_surf := Theta_mp (melting point of water, 0 °C), because the snow/ice
              layer is "waterized" in the contact zone.
        '''

        # 2.1) pre-processing
        # R_f = self.ui.sb_rf.value()  # free-area ratio (default: 0.2)

        # 2.2) available power inside ground (corresponds to temperature spread)
        Q_0 = (Theta_b_0 - Theta_surf_0) * R_th ** -1

        # 2.3) Simulation modes 1-3
        ''' Simulation mode 1'''
        if Q_0 < 0:  # no temperature spread available (Sibirian conditions)

            sim_mod = 1

            calc_T = True

            # Q_sensible, Q_latent := 0 
            ''' thermal energy is modelled as coming from the ground only,
                although thermal influx from surroundings possible in reality
            '''
            sen, lat = False, False

            # 2.4) iterative solution of reduced power balance F_T = 0, solved for Theta_surf
            Theta_surf_sol, Q_lat, Q_sen, Q_eva = solve_F_T(R_f, con, rad, eva, sen, lat, S_r, Theta_inf, u_inf, Theta_surf_0, m_w_0, z_asl, Phi, B, he.A_he)

            Q_sol = -1  # extracted power set to zero

        else:  # temperature spread in ground available (usual case)
            ''' Simulation modes 2 & 3'''
            # 2.4) new evaluation of Q_0 and surface losses
            ''' Q_0 and surface losses are now calculated utilizing Theta_surf_0 := Theta_mp (explicit evaluation)
            '''
            # Q_0
            Q_0 = (Theta_b_0 - Theta_mp) * R_th ** -1

            # Q_convection
            Q_con = Q_con_T(Theta_mp, con, u_inf, Theta_inf, he.A_he)

            # Q_radiation
            Q_rad = Q_rad_T(Theta_mp, rad, S_r, Theta_inf, B, Phi, he.A_he)

            # Q_evaporation
            Q_eva = Q_eva_T(Theta_mp, eva, Theta_mp, m_w_0, Theta_inf, u_inf, z_asl, Phi, he.A_he)

            # 2.5) power available for melting of snow/ice
            Q_R = Q_0 - R_f * (Q_con + Q_rad + Q_eva)

            # 2.6) Simulation modes 2 & 3
            if Q_R < 0:  # temperature spread not suffient to melt snow/ice
                ''' Simulation mode 2'''
                sim_mod = 2

                # Q_sensible, Q_latent := 0 
                ''' thermal energy is modelled as coming from the ground only,
                    although thermal influx from surroundings possible in reality
                '''
                sen, lat = False, False

                # 2.7) iterative solution of power balance F_Q = 0, solved for Q.
                Q_sol, Q_lat, Q_sen, Q_eva = solve_F_Q(R_f, con, rad, eva, sen, lat, S_r, Theta_inf, Theta_b_0, R_th, u_inf, Theta_surf_0, m_w_0, z_asl, Phi, B, he.A_he)

            else:  # temperature spread sufficient to melt snow/ice
                ''' Simulation mode 3'''
                sim_mod = 3

                calc_T = True

                # 2.7) volume flux of melted snow/ice: V._s = V._s(Q._R)
                V_s = Q_R / (rho_w * (h_Ph_sl + c_p_s * (Theta_mp - Theta_inf)))
                if V_s < 0:  # only positive values allowed
                    V_s = 0

                # 2.8) explicit evaluation of snow/ice melting loads using V._s

                # Q_sensible
                Q_sen = 0
                if sen:
                    Q_sen = rho_w * c_p_s * (Theta_mp - Theta_inf) * V_s

                # Q_latent
                Q_lat = 0
                if lat:
                    Q_lat = rho_w * h_Ph_sl * V_s

                Theta_surf_sol = Theta_mp
                Q_sol = Q_lat + Q_sen + R_f * (Q_con + Q_rad + Q_eva)

    else:  # snow/ice is melted instantaneously (within current timestep), no forming of snow/ice layers
        ''' Simulation modes 4 & 5'''
        ''' Simulation modes 4 & 5 encompass all modes of snow-/ice-free operation of the surface heating element
            
            Simulation mode 4: most common simulation mode for reasonably sized systems
            - Q. >= 0 (positive heat extraction from ground)
            - F_Q = 0 solved for Q.
            
            Simulation mode 5: "summer mode"
            - Q. = 0 (no heat extraction from ground, heat influx from surroundings lifts surface element temperature above borehole wall temperature)
            - F_T = 0 solved for Theta_surf
        '''

        ''' Simulation mode 4'''
        sim_mod = 4

        # 2.1) pre-Processing
        R_f = 1  # free-area ratio

        # 2.2) iterative solution of power balance F_Q = 0, solved for Q.
        Q_sol, Q_lat, Q_sen, Q_eva = solve_F_Q(R_f, con, rad, eva, sen, lat, S_r, Theta_inf, Theta_b_0, R_th, u_inf, Theta_surf_0, m_w_0, z_asl, Phi, B, he.A_he)

        # 2.3) Simulation mode 5: "summer mode"
        ''' Simulationsmodus 5'''
        if Q_sol < 0:

            sim_mod = 5

            calc_T = True

            # Q_sensible, Q_latent := 0
            ''' thermal energy is modelled as coming from the ground only,
                although thermal influx from surroundings possible in reality
            '''
            sen, lat = False, False

            # 2.4) iterative solution of reduced power balance F_T = 0, solved for Theta_surf
            Theta_surf_sol, Q_lat, Q_sen, Q_eva = solve_F_T(R_f, con, rad, eva, sen, lat, S_r, Theta_inf, u_inf, Theta_surf_0, m_w_0, z_asl, Phi, B, he.A_he)

    # 3.) Mass balances of water and snow on the heating element surface

    # mass balance water [kg]
    m_w_1 = m_water(m_w_0, RR, he.A_he, Q_eva)

    # mass balance snow [kg]
    m_s_1 = m_snow(m_s_0, S_r, he.A_he, Q_lat, sb_active)

    # 4.) Q_sol, Q_N & Q_V [W]
    ''' Evaluation of the extraction power Q_sol, net used power Q_N and 
        thermal losses Q_V (borehole-to-heating element connection & heating element underside)
    '''

    # 4.1) Q_sol [W]
    if Q_sol < 0:  # wickless thermosiphons don't allow negative heat flux (into the ground)
        Q_sol = 0

    # 4.2) Q_N [W]
    Q_N = Q_lat + Q_sen

    # 4.3) Q_V [W]
    Q_V_sol = Q_V(Theta_b_0 - Q_sol * R_th_ghp, Theta_inf, lambda_p, lambda_iso, l_R_An, r_iso, r_pa, r_pi, he)

    return Q_sol, Q_N, Q_V_sol, calc_T, Theta_surf_sol, m_w_1, m_s_1, sb_active, sim_mod
