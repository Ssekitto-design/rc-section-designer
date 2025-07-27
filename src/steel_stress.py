import numpy as np


def steel_stress(strain, f_yd):
    ε_y = 0.002
    if abs(strain) <= ε_y:
        return strain / ε_y * f_yd
    else:
        return np.sign(strain) * f_yd