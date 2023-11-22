# -*- coding: utf-8 -*-
""" GERDPySim - 'heating_element.py'
    
    Class for the heating element

    Authors: Yannick Apfel, Meike Martin
"""
class HeatingElement(object):
    """
    Contains class for the heating element.

    Attributes
    ----------
    A_he:           float
                    area of the heating element [m²]
    x_min:          float
                    minimum vertical pipe-to-surface distance [m]
    lambda_c:       float
                    thermal conductivity of heating element material [W/mK]
    lambda_p:       float 
                    thermal conductivity of heat pipes [W/mK]
    d_pa:           float 
                    outer radius of heatpipes [m]
    d_pi:           float
                    inner radius of heatpipes [m]
    s_R:            float
                    centre-distance between heatpipes [m]
    l_p_he:            float
                    total heatpipe length inside heating element [m]
    D_he:           float
                    vertical thickness of heating element [m]
    D_iso_he:       float
                    vertical thickness of insulation layer on underside of heating element [m]

    """

    def __init__(self, A_he, x_min, lambda_c, lambda_p, d_pa, d_pi, s_R,
                 l_p_he, D_he, D_iso_he):
        self.A_he = float(A_he)
        self.x_min = float(x_min)
        self.lambda_c = float(lambda_c)
        self.lambda_p = float(lambda_p)
        self.d_pa = float(d_pa)
        self.d_pi = float(d_pi)
        self.s_R = float(s_R)
        self.l_p_he = float(l_p_he)
        self.D_he = float(D_he)
        self.D_iso_he = float(D_iso_he)

    def __repr__(self):
        s = ('HeatingElement(A_he={self.A_he}, x_min={self.x_min}, \
             lambda_c={self.lambda_c}, lambda_p={self.lambda_p},'
             ' d_pa={self.d_pa}, d_pi={self.d_pi}, \
                     s_R={self.s_R}, l_p_he={self.l_p_he}, D_he={self.D_he}, \
                         D_iso_he={self.D_iso_he}').format(self=self)
        return s
