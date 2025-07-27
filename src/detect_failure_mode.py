# detect_failure_mode.py

from enum import Enum

class FailureMode(Enum):
    COMPRESSION_CONTROLLED = 'Compression-Controlled'
    TENSION_CONTROLLED = 'Tension-Controlled'
    BALANCED = 'Balanced'
    NO_FAILURE = 'No Failure'

def detect_failure_mode(
    x: float,
    section_depth_mm: float,
    strain_top: float,
    strain_bottom: float,
    eps_cu: float = 0.0035,
    eps_su: float = 0.010
) -> FailureMode:
    """
    Classifies failure mode based on top and bottom fiber strains.

    Parameters:
        x (float): Neutral axis depth from top fiber (mm)
        section_depth_mm (float): Total section depth (mm)
        strain_top (float): Strain at top fiber (positive = compression)
        strain_bottom (float): Strain at bottom fiber (positive = tension)
        eps_cu (float): Ultimate concrete strain (default: EC2 0.0035)
        eps_su (float): Ultimate steel strain (default: EC2 0.010)

    Returns:
        FailureMode: One of [COMPRESSION_CONTROLLED, TENSION_CONTROLLED, BALANCED, NO_FAILURE]
    """
    if strain_top >= eps_cu and strain_bottom < eps_su:
        return FailureMode.COMPRESSION_CONTROLLED
    elif strain_bottom >= eps_su and strain_top < eps_cu:
        return FailureMode.TENSION_CONTROLLED
    elif strain_top >= eps_cu and strain_bottom >= eps_su:
        return FailureMode.BALANCED
    else:
        return FailureMode.NO_FAILURE