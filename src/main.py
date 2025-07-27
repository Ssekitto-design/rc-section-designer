# main.py

# Step 1: Setup and Imports
import os
from src.utils import ensure_export_folder
from src.materials import Material, DesignCode
from src.section import Section
from src.rebar import RebarLayout
from src.interaction_diagram import generate_interaction_diagram_with_modes
from src.export import export_interaction_to_csv
from src.plotting import plot_interaction_diagram

# Create exports folder if missing
ensure_export_folder()

# Step 2: Define Materials (Eurocode)
concrete = Material(name="C30/37", fck=30, unit_weight=25, code=DesignCode.EUROCODE)
steel = Material(name="B500B", fyk=500, code=DesignCode.EUROCODE)

# Step 3: Define Section Geometry
section = Section(b=300, h=500, cover=30, material=concrete)

# Step 4: Define Rebar Layout
layout = RebarLayout()
layout.add_group(diameter_mm=16, count=4, depth_mm=50)     # Top layer
layout.add_group(diameter_mm=20, count=4, depth_mm=450)    # Bottom layer

# Step 5: Generate Interaction Diagram
diagram = generate_interaction_diagram_with_modes(
    layout=layout,
    section=section,
    concrete=concrete,
    steel=steel,
    points=100  # Resolution
)

# Step 6: Export to CSV
export_interaction_to_csv(diagram, filename="exports/mn_diagram.csv")

# Step 7: Plot and Save PNG
plot_interaction_diagram(diagram, save_path="exports/mn_diagram.png")

print("✅ Interaction diagram generated and saved to /exports/")