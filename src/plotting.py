import matplotlib.pyplot as plt
from matplotlib.patches import Patch

def plot_interaction_diagram(diagram_data, title="Interaction Diagram with Failure Modes"):
    """
    Plots axial-moment points with colors based on failure mode.
    Parameters:
    - diagram_data: list of tuples (axial, moment, mode)
    - title: chart title (optional)
    """

    colors = {
        "Compression-Controlled": "red",
        "Balanced": "orange",
        "Tension-Controlled": "blue"
    }

    plt.figure(figsize=(8, 6))
    for pt in diagram_data:
        axial = pt["axial_kN"]
        moment = pt["moment_kNm"]
        mode = pt["failure_mode"]
        plt.scatter(moment, axial, color=colors.get(mode, "gray"), s=25)

    legend_elements = [
        Patch(facecolor='red', label='Compression-Controlled'),
        Patch(facecolor='orange', label='Balanced'),
        Patch(facecolor='blue', label='Tension-Controlled')
    ]
    plt.legend(handles=legend_elements, loc='best')

    plt.xlabel("Moment (kNm)")
    plt.ylabel("Axial Force (kN)")
    plt.title(title)
    plt.grid(True)
    plt.tight_layout()
    plt.show()