# cython: language_level=3
""" GERDPySim - 'load_generator_utils.py'
    
    Utility module for 'load_generator.py':
    physical model equations, correlations and base functions for surface load generation
    
    Sources: [Konrad2009], [Fuchs2021], [ASHRAE2015]

    Authors: Yannick Apfel, Meike Martin
"""

import math
import sys
import CoolProp.CoolProp as CP
cimport numpy as np
cimport cython
from libc.math cimport exp, pow, log, sqrt

# Physical parameters (mainly from [VDI2013])
# Water
cdef double rho_w = 999.84  # Density of water (p = 1 bar, T = 0 °C) [kg/m³]
cdef double h_Ph_sl = 333e3  # Phase-change enthalpy solid <-> liquid [J/kg]
cdef double h_Ph_lg = 2500.9e3  # Phase-change enthalpy liquid <-> vapour (T = 0,01 °C) [J/kg]
cdef double c_p_s = 2.106e3  # Specific heat capacity of ice/snow (T = 0 °C) [J/kgK]
cdef double c_p_w = 4219  # Specific heat capacity of water (T = 0 °C) [J/kgK]
cdef double Theta_mp = 0  # Melting point of ice/snow (p = 1 bar) [°C]
# Air
cdef double rho_a = 1.276  # Density of dry air (p = 1 bar, T = 0 °C) [kg/m³]
cdef double c_p_a = 1006  # Specific heat capacity of air (p = 1 bar, T = 0 °C) [J/kgK]
cdef double lambda_a = 0.0244  # Thermal conductivity of air [W/m*K]
cdef double a_a = lambda_a / (rho_a * c_p_a)  # Thermal diffusivity of air [m²/s]
cdef double mu_a = 13.5e-6  # Kinetic viscosity of air (p = 1 bar, T = 0 °C) [m²/s]
# Arbitrary
cdef double H_max = 2  # Maximum allowed water level on heating element without running off [mm]

# Wind-shear-corrected wind speed (logarithmic) [m/s]
cpdef double u_eff(double v):
    cdef double z_1 = 10  # Typical height of meteorological weather stations [m]
    cdef double z_n = 1  # Reference height (:= 1 m)
    cdef double z_0 = 0.005  # Topographic roughness level of the ground
    return v * (math.log10(z_n) - math.log10(z_0)) / (math.log10(z_1) - math.log10(z_0))

# Altitude-corrected ambient pressure [Pa]
cpdef double p_inf(double z_asl):
    return 101325 * (1 - 2.25577e-5 * z_asl) ** 5.2559

# Saturation vapour pressure acc. to ASHRAE2013 [Pa]
cpdef double p_s_ASHRAE(double T):  # Input in [K]
    """
    Saturation vapour pressure acc. to ASHRAE2013 [Pa]

    Parameters
    ----------
    T : double
        Temperature in Kelvin.

    Returns
    -------
    double
        Saturation vapour pressure in Pascals.
    """
    cdef double C1 = -5.6745359e3
    cdef double C2 = 6.3925247
    cdef double C3 = -9.677843e-3
    cdef double C4 = 6.2215701e-7
    cdef double C5 = 2.0747825e-9
    cdef double C6 = -9.484024e-13
    cdef double C7 = 4.1635019
    cdef double C8 = -5.8002206e3
    cdef double C9 = 1.3914993
    cdef double C10 = -4.8640239e-2
    cdef double C11 = 4.1764768e-5
    cdef double C12 = -1.4452093e-8
    cdef double C13 = 6.5459673

    if T <= 273.15:
        return exp(C1 / T + C2 + C3 * T + C4 * T**2 + C5 * T**3 + C6 * T**4 + C7 * log(T))
    else:
        return exp(C8 / T + C9 + C10 * T + C11 * T**2 + C12 * T**3 + C13 * log(T))

# Heat transfer coefficient [W/m²K] acc. to [Bentz D. P. 2000]
cpdef double alpha_con_he_o(double u):  # Heating element surface
    """
    Heat transfer coefficient [W/m²K] acc. to [Bentz D. P. 2000]
    for the heating element surface.

    Parameters
    ----------
    u : double
        Wind-shear-corrected wind speed [m/s].

    Returns
    -------
    double
        Heat transfer coefficient in W/m²K.
    """
    cdef double Nu, Re, Pr, lambda_a = 0.0244

    # Prandtl number for air
    Pr = 0.71

    # Reynolds number
    Re = u * 0.1 / 13.5e-6

    # Nusselt number calculation
    if Re < 5e5:
        # Laminar flow
        Nu = 0.664 * pow(Re, 0.5) * pow(Pr, 1/3)
    else:
        # Turbulent flow
        Nu = 0.037 * pow(Re, 0.8) * pow(Pr, 1/3)

    # Heat transfer coefficient
    return Nu * lambda_a / 0.1

# Heat transfer coefficient [W/m²K] acc. to [Löser: Technische Thermodynamik]
cpdef double alpha_con_he_u():
    return 10

# Heat transfer coefficient [W/m²K] acc. to [Löser: Technische Thermodynamik]
cpdef double alpha_con_an(double deltaT):
    return 9.4 + 0.052 * deltaT

# Mass balance for water on heating element surface
cpdef double m_water(double m_w_0, double RR, double A_he, double Q_eva):
    """
    Mass balance for water on heating element surface.

    Parameters
    ----------
    m_w_0 : double
        Initial mass of water on the heating element surface [kg].
    RR : double
        Rain rate [mm/h].
    A_he : double
        Area of the heating element [m²].
    Q_eva : double
        Heat flux due to evaporation [W].

    Returns
    -------
    double
        Mass of water on the heating element surface [kg].
    """
    cdef double h_Ph_lg = 2500.9e3  # Phase-change enthalpy liquid <-> vapour (T = 0,01 °C) [J/kg]
    cdef double delta_t = 3600  # Time step [s] (1 hour)

    # Convert rain rate from mm/h to kg/s
    cdef double rain_rate_kg_s = RR * A_he / 1000 / 3600

    # Mass balance calculation
    cdef double m_water = m_w_0 + rain_rate_kg_s * delta_t - Q_eva / h_Ph_lg * delta_t

    # Ensure mass does not become negative
    if m_water < 0:
        m_water = 0

    return m_water

# Mass balance for ice/snow on heating element surface
cpdef double m_snow(double m_s_0, double S_r, double A_he, double Q_lat, bint sb_active):
    """
    Mass balance for ice/snow on heating element surface.

    Parameters
    ----------
    m_s_0 : double
        Initial mass of snow on the heating element surface [kg].
    S_r : double
        Snow rate [mm/h].
    A_he : double
        Area of the heating element [m²].
    Q_lat : double
        Latent heat flux [W].
    sb_active : bint
        Flag indicating whether snowblower is active (1) or not (0).

    Returns
    -------
    double
        Mass of snow on the heating element surface [kg].
    """
    cdef double h_Ph_sl = 333e3  # Phase-change enthalpy solid <-> liquid [J/kg]
    cdef double delta_t = 3600  # Time step [s] (1 hour)

    # Convert snow rate from mm/h to kg/s
    cdef double snow_rate_kg_s = S_r * A_he / 1000 / 3600

    # Mass balance calculation
    cdef double m_snow = m_s_0 + snow_rate_kg_s * delta_t - Q_lat / h_Ph_sl * delta_t

    # Snowblower effect
    if sb_active:
        m_snow = 0

    # Ensure mass does not become negative
    if m_snow < 0:
        m_snow = 0

    return m_snow

# Emission coefficient of the heating element surface (radiation) [-]
cpdef double epsilon_surf(str material):
    if material == 'concrete':
        return 0.94
    else:
        return 0.94

# Average ambient radiation temperature [K]
cpdef double T_MR(double S_r, double Theta_inf, double B, double Phi):
    """
    Average ambient radiation temperature [K].

    Parameters
    ----------
    S_r : double
        Solar radiation [W/m²].
    Theta_inf : double
        Ambient air temperature [°C].
    B : double
        Fraction of sky dome covered by clouds [-].
    Phi : double
        Latitude [degrees].

    Returns
    -------
    double
        Average ambient radiation temperature in Kelvin.
    """
    cdef double sigma = 5.67e-8  # Stefan-Boltzmann constant [W/m²K⁴]
    cdef double T_inf_K = Theta_inf + 273.15  # Convert to Kelvin

    # Calculate the average ambient radiation temperature
    cdef double T_MR = pow((S_r * (1 - B) / sigma + pow(T_inf_K, 4) * (1 + B * (0.552 - 0.528 * pow(B, 0.25)))), 0.25)
    return T_MR

# Binary diffusion coefficient [-]
cpdef double delta(double Theta_inf, double z_asl):
    """
    Binary diffusion coefficient [-].

    Parameters
    ----------
    Theta_inf : double
        Ambient air temperature [°C].
    z_asl : double
        Altitude above sea level [m].

    Returns
    -------
    double
        Binary diffusion coefficient.
    """
    cdef double T_inf_K = Theta_inf + 273.15  # Convert to Kelvin
    cdef double p_inf = 101325 * pow(1 - 2.25577e-5 * z_asl, 5.2559)  # Ambient pressure [Pa]

    # Calculate the binary diffusion coefficient
    cdef double delta = 0.211 * pow(T_inf_K / 273.15, 1.94) / (p_inf / 101325)
    return delta

# Mass transfer coefficient [m/s]
cpdef double beta_c(double Theta_inf, double u, double z_asl):
    """
    Mass transfer coefficient [m/s].

    Parameters
    ----------
    Theta_inf : double
        Ambient air temperature [°C].
    u : double
        Wind-shear-corrected wind speed [m/s].
    z_asl : double
        Altitude above sea level [m].

    Returns
    -------
    double
        Mass transfer coefficient.
    """
    cdef double T_inf_K = Theta_inf + 273.15  # Convert to Kelvin
    cdef double p_inf = 101325 * pow(1 - 2.25577e-5 * z_asl, 5.2559)  # Ambient pressure [Pa]
    cdef double Sc = 0.6  # Schmidt number for water vapour in air

    # Calculate the mass transfer coefficient
    cdef double Re = u * 0.1 / 13.5e-6  # Reynolds number
    cdef double Nu = 0.664 * pow(Re, 0.5) * pow(Sc, 1/3)  # Nusselt number
    cdef double beta_c = Nu * 0.211 * pow(T_inf_K / 273.15, 1.94) / (0.1 * p_inf / 101325)
    return beta_c

# Water vapour loading of saturated air at ambient conditions [vapour-kg / air-kg]
cpdef double X_inf(double Theta_inf, double Phi, double z_asl):
    """
    Water vapour loading of saturated air at ambient conditions [vapour-kg / air-kg].

    Parameters
    ----------
    Theta_inf : double
        Ambient air temperature [°C].
    Phi : double
        Relative humidity [%].
    z_asl : double
        Altitude above sea level [m].

    Returns
    -------
    double
        Water vapour loading of saturated air.
    """
    cdef double T_inf_K = Theta_inf + 273.15  # Convert to Kelvin
    cdef double p_inf = 101325 * pow(1 - 2.25577e-5 * z_asl, 5.2559)  # Ambient pressure [Pa]
    cdef double R_v = 461.5  # Specific gas constant for water vapour [J/kgK]

    # Saturation vapour pressure
    cdef double p_s = p_s_ASHRAE(T_inf_K)

    # Water vapour loading
    cdef double X_inf = 0.622 * Phi * p_s / (p_inf - Phi * p_s)
    return X_inf

# Water vapour loading of saturated air at heating element surface [vapour-kg / air-kg]
cpdef double X_sat_surf(double Theta_surf, double z_asl):
    """
    Water vapour loading of saturated air at heating element surface [vapour-kg / air-kg].

    Parameters
    ----------
    Theta_surf : double
        Surface temperature [°C].
    z_asl : double
        Altitude above sea level [m].

    Returns
    -------
    double
        Water vapour loading of saturated air at the surface.
    """
    cdef double T_surf_K = Theta_surf + 273.15  # Convert to Kelvin
    cdef double p_inf = 101325 * pow(1 - 2.25577e-5 * z_asl, 5.2559)  # Ambient pressure [Pa]
    cdef double R_v = 461.5  # Specific gas constant for water vapour [J/kgK]

    # Saturation vapour pressure at the surface
    cdef double p_s_surf = p_s_ASHRAE(T_surf_K)

    # Water vapour loading at the surface
    cdef double X_sat_surf = 0.622 * p_s_surf / (p_inf - p_s_surf)
    return X_sat_surf
