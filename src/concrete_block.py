# concrete_block.py

from collections import namedtuple

# Define a lightweight result container
ConcreteBlockResult = namedtuple("ConcreteBlockResult", ["force_N", "moment_Nmm"])

def compute_concrete_block(x: float, width_mm: float, f_cd: float) -> ConcreteBlockResult:
    """
    Computes axial force and moment contribution from concrete stress block.

    Assumes a rectangular stress block as per Eurocode EC2.

    Parameters:
        x (float): Neutral axis depth from top fiber (mm)
        width_mm (float): Section width (b) in mm
        f_cd (float): Design compressive strength of concrete (MPa)

    Returns:
        ConcreteBlockResult: Named tuple with:
            - force_N (float): Axial compressive force from block (N)
            - moment_Nmm (float): Moment contribution about centroid (N·mm)

    Notes:
        Uses Eurocode α = 0.85 and γ = 0.8 parameters for rectangular block.
        Stress block centroid is at 0.4x from top.
    """
    # Input checks (optional but good practice)
    if x <= 0:
        return ConcreteBlockResult(0.0, 0.0)

    # Eurocode parameters
    alpha = 0.85
    gamma = 0.8

    # Effective block height
    stress_block_depth = gamma * x
    stress = alpha * f_cd  # in MPa
    area = stress_block_depth * width_mm  # mm²

    # Convert MPa × mm² → N
    force_N = stress * area  # N
    moment_arm = x * 0.4  # mm
    moment_Nmm = force_N * moment_arm

    return ConcreteBlockResult(force_N, moment_Nmm)