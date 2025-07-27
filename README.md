# RC Section Designer 📐🧱

This tool computes axial–moment interaction diagrams for reinforced concrete sections based on Eurocode design parameters.

Step 1: Run the Script
python main.py
This executes all core modules — from material definitions to rebar layout, diagram generation, and export.

📁 Step 2: View the Results
After running the script, you'll find:
- exports/mn_diagram.csv – Interaction data points as M vs N pairs.
- exports/mn_diagram.png – A visual plot of the interaction diagram.

📊 Step 3: Interpret the Diagram
The plot shows:
- The safe design envelope under combined axial force N and bending moment M.
- Key curvature zones (tension-controlled, balanced, compression-controlled).
- Helps check if your load combination sits inside the envelope (i.e. structurally safe!).


