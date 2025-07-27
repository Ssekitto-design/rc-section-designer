from rebar import RebarLayout
from section import Section
from materials import Material
from interaction_diagram import generate_interaction_diagram_with_modes
from plotting import plot_interaction_diagram

# Define materials
concrete = Material("C30/37", fck=30, unit_weight=24)
steel = Material("B500B", fyk=500, unit_weight=78.5)

# Define section
section = Section(b=300, h=500, cover=40, material=concrete)

# Define reinforcement
layout = RebarLayout()
layout.add_group(16, 4, 40)       # top bars
layout.add_group(20, 4, 460)      # bottom bars

# Generate diagram
diagram = generate_interaction_diagram_with_modes(layout, section, concrete, steel)

# Print sample points
for i in range(0, len(diagram), 10):
    pt = diagram[i]
    print(f"Axial: {pt['axial_kN']:.1f} kN | Moment: {pt['moment_kNm']:.1f} kNm | Mode: {pt['failure_mode']}")

# Visualize interaction behavior with failure modes
plot_interaction_diagram(diagram)