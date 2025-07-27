# interaction.py

from section import Section
from materials import Material
from src.concrete_block import compute_concrete_block
from src.detect_failure_mode import detect_failure_mode
from src.steel_stress import steel_stress
from src.rebar import RebarLayout

import numpy as np

def compute_strain(neutral_axis: float, depth: float) -> float:
    """
    Computes strain at a given depth based on neutral axis.

    Parameters:
    - neutral_axis (float): Position of neutral axis from top (mm)
    - depth (float): Depth of bar from top face (mm)

    Returns:
    - float: Calculated strain
    """
    return (neutral_axis - depth) / neutral_axis


def compute_steel_contribution(
    layout: RebarLayout, h: float, neutral_axis: float, f_yd: float
) -> tuple:
    """
    Computes total force and moment from steel bars.

    Returns:
    - Tuple: (total_force, total_moment, top_depths, bottom_depths)
    """
    total_force = 0
    total_moment = 0
    top_depths = []
    bottom_depths = []

    for bar in layout.bars:
        depth = bar["depth"]
        area = bar["area_mm2"]

        strain = compute_strain(neutral_axis, depth)
        stress = steel_stress(strain, f_yd)
        force = stress * area
        moment = force * (h / 2 - depth)

        total_force += force
        total_moment += moment

        if depth < h / 2:
            top_depths.append(depth)
        else:
            bottom_depths.append(depth)

    return total_force, total_moment, top_depths, bottom_depths


def generate_interaction_diagram_with_modes(
    layout: RebarLayout,
    section: Section,
    concrete: Material,
    steel: Material,
    points: int = 100
) -> list:
    """
    Generates M–N interaction diagram with failure mode tagging.

    Parameters:
    - layout (RebarLayout): Steel layout
    - section (Section): Concrete section geometry
    - concrete (Material): Concrete material object
    - steel (Material): Steel material object
    - points (int): Number of neutral axis divisions

    Returns:
    - list: Diagram data with axial load, moment, and failure mode
    """
    diagram = []
    f_cd = concrete.fcd
    f_yd = steel.fyd
    b = section.b
    h = section.h

    for x in np.linspace(10, h - 10, points):  # neutral axis depth
        c_force, c_moment = compute_concrete_block(x, b, f_cd)

        s_force, s_moment, top_depths, bottom_depths = compute_steel_contribution(
            layout, h, x, f_yd
        )

        axial = c_force + s_force
        moment = c_moment + s_moment

        top_avg = np.mean(top_depths) if top_depths else 0
        bot_avg = np.mean(bottom_depths) if bottom_depths else h
        mode = detect_failure_mode(x, top_avg, bot_avg)

        diagram.append({
            "axial_kN": axial / 1000,
            "moment_kNm": moment / 1000000,
            "failure_mode": mode
        })

    return diagram