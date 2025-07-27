# interaction_diagram.py

from collections import namedtuple
from plot_utils import plot_interaction_diagram

# 📦 Result container
InteractionPoint = namedtuple("InteractionPoint", ["neutral_axis_mm", "axial_force_N", "bending_moment_Nmm"])

# Core generator function
def generate_interaction_diagram(width_mm: float, depth_mm: float, f_cd: float, steps: int = 20) -> list[InteractionPoint]:
    """
    Generates axial-moment interaction points from concrete stress block contribution alone.

    Assumes rectangular EC2 block and linear variation with neutral axis depth.

    Parameters:
        width_mm (float): Section width in mm
        depth_mm (float): Section depth in mm
        f_cd (float): Concrete design compressive strength in MPa
        steps (int): Number of x-depth steps across section (default: 20)

    Returns:
        List[InteractionPoint]: Collection of axial force and bending moment values
    """
    diagram = []
    for i in range(steps + 1):
        x = depth_mm * i / steps  # neutral axis depth from top
        block = compute_concrete_block(x, width_mm, f_cd)
        diagram.append(InteractionPoint(x, block.axial_force_N, block.bending_moment_Nmm))
    return diagram

# Concrete block model
def compute_concrete_block(x: float, width_mm: float, f_cd: float) -> InteractionPoint:
    """
    Computes axial force and moment from EC2 rectangular stress block.

    Parameters:
        x (float): Neutral axis depth (mm)
        width_mm (float): Section width (mm)
        f_cd (float): Design compressive strength (MPa)

    Returns:
        InteractionPoint: Axial force and moment at depth x
    """
    if x <= 0:
        return InteractionPoint(x, 0.0, 0.0)

    alpha = 0.85   # EC2 strength reduction factor
    gamma = 0.8    # EC2 block height ratio

    stress_block_depth = gamma * x
    stress = alpha * f_cd
    area = stress_block_depth * width_mm

    force_N = stress * area
    moment_arm = x * 0.4
    moment_Nmm = force_N * moment_arm

    return InteractionPoint(x, force_N, moment_Nmm)

# Optional test block
if __name__ == "__main__":
    # Sample test values
    width_mm = 300
    depth_mm = 500
    f_cd = 25

    points = generate_interaction_diagram(width_mm, depth_mm, f_cd)

    # Extract P and M axes with unit conversions
    P = [pt.axial_force_N / 1000 for pt in points]     # kN
    M = [pt.bending_moment_Nmm / 1e6 for pt in points] # kNm

    # Plot visuals
    plot_interaction_diagram(P, M, title="EC2 Concrete Block Interaction Diagram")