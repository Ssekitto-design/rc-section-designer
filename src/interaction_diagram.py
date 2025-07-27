from section import Section
from materials import Material
import numpy as np

from src.concrete_block import concrete_block
from src.detect_failure_mode import detect_failure_mode
from src.steel_stress import steel_stress


def generate_interaction_diagram_with_modes(layout, section: Section, concrete: Material, steel: Material):
    diagram = []
    f_cd = concrete.fcd
    f_yd = steel.fyd
    b = section.b
    h = section.h

    for x in np.linspace(10, h - 10, 100):  # neutral axis depth
        c_force, c_moment = concrete_block(x, b, f_cd)

        total_steel_force = 0
        total_steel_moment = 0
        top_bar_depths = []
        bottom_bar_depths = []

        for bar in layout.bars:
            depth = bar["depth"]
            area = bar["area_mm2"]

            strain = (x - depth) / x
            stress = steel_stress(strain, f_yd)
            force = stress * area
            moment = force * (h / 2 - depth)

            total_steel_force += force
            total_steel_moment += moment

            # Save depths for failure mode tagging
            if depth < h / 2:
                top_bar_depths.append(depth)
            else:
                bottom_bar_depths.append(depth)

        axial = c_force + total_steel_force
        moment = c_moment + total_steel_moment

        # Use average depth of top and bottom bar groups
        top_depth = np.mean(top_bar_depths) if top_bar_depths else 0
        bottom_depth = np.mean(bottom_bar_depths) if bottom_bar_depths else h
        mode = detect_failure_mode(x, top_depth, bottom_depth)

        diagram.append({
            "axial_kN": axial / 1000,
            "moment_kNm": moment / 1000000,
            "failure_mode": mode
        })

    return diagram