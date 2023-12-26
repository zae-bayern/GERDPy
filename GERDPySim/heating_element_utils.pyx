# cython: language_level=3
import math
cimport cython

cpdef double sum_fct(double kappa_o, double kappa_u, double s_R, double s_c, double x_o, double x_u, double lambda_c):
    cdef double beta_o = kappa_o * s_R / lambda_c
    cdef double beta_u = kappa_u * s_R / lambda_c
    cdef double ssum_temp = 0
    cdef int j = 0
    cdef double error = 1e-6
    cdef double N_1, N_2, gamma, e_o, e_u, ssum

    while True:  # infinite loop until "break"
        j += 1

        N_1 = 1 - (beta_u + 2 * math.pi * j) / (beta_u - 2 * math.pi * j) * math.exp(4 * math.pi * j * s_c / s_R)
        N_2 = 1 - (beta_u - 2 * math.pi * j) / (beta_u + 2 * math.pi * j) * math.exp(-4 * math.pi * j * s_c / s_R)

        gamma = (beta_o - 2 * math.pi * j) / (beta_o + 2 * math.pi * j) * math.exp(-4 * math.pi * j * (x_u + x_o) / s_R)

        e_o = ((lambda_c + lambda_c / N_1 - lambda_c / N_2) * (math.exp(-4 * math.pi * j * x_u / s_R) - gamma)) /\
              (lambda_c * (1 + gamma) + (lambda_c / N_2 - lambda_c / N_1) * (1 - gamma))

        e_u = - (beta_o - 2 * math.pi * j) / (beta_o + 2 * math.pi * j) * math.exp(-4 * math.pi * j * x_o / s_R) * (1 + e_o)

        ssum = ssum_temp + (e_o + e_u) / j

        if abs(ssum - ssum_temp) < error:
            break

        ssum_temp = ssum

    return ssum

cpdef double q_l(double x_o, double x_u, double d_pa, double d_pi, double lambda_c, double lambda_p, double s_R, double Theta_R, double Theta_inf_o, bint state_u_insul):
    cdef double s_c = 0.0  # [m] -> set to 0, because of no additional layers in heating element
    cdef double d_insul_a = d_pa + 0.0002  # thermal contact resistance modelled as layer of air of 1/10 mm
    cdef double Theta_inf_u = Theta_inf_o
    cdef double lambda_insul = 0.0262  # air
    cdef double alpha_o = 1e10  # surface heat transfer coefficient --> infinite (Dirichlet temperature boundary condition)
    cdef double alpha_u = alpha_o

    if state_u_insul:
        alpha_u = 1e-10  # surface heat transfer coefficient --> 0 (modelled as insulated, because only heat transfer to surface considered)
        x_u = 1e10  # x_u equals semi-infinite space

    cdef double kappa_o = (1 / alpha_o + s_c / lambda_c) ** -1
    cdef double kappa_u = (1 / alpha_u + s_c / lambda_c) ** -1
    cdef double kappa_o_ = (kappa_o ** -1 + x_o / lambda_c) ** -1
    cdef double kappa_u_ = (kappa_u ** -1 + x_u / lambda_c) ** -1

    cdef double ssum = sum_fct(kappa_o, kappa_u, s_R, s_c, x_o, x_u, lambda_c)  # determination of ssum-term

    cdef double q_l = 2 * math.pi * lambda_c * (Theta_R - (Theta_inf_o * kappa_o_ + Theta_inf_u * kappa_u_) / (kappa_o_ + kappa_u_)) \
          / (lambda_c / lambda_p * math.log(d_pa / d_pi)
          + lambda_c / lambda_insul * math.log(d_insul_a / d_pa) + math.log(s_R / (math.pi * d_insul_a))
          + (2 * math.pi * lambda_c) / (s_R * (kappa_o_ + kappa_u_)) + ssum)  # [W/m]

    return q_l
