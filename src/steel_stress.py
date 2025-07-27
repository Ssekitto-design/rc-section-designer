import numpy as np

def steel_stress(strain: float, f_yd: float, ε_y: float = 0.002) -> float:
    """
    Computes design steel stress based on strain and yield strain threshold.

    Parameters:
    - strain (float): Actual strain at the bar location
    - f_yd (float): Design yield strength of steel (MPa)
    - ε_y (float, optional): Yield strain threshold (default = 0.002)

    Returns:
    - float: Stress in steel (MPa), with sign based on tension/compression
    """
    if abs(strain) <= ε_y:
        return (strain / ε_y) * f_yd
    else:
        return np.sign(strain) * f_yd