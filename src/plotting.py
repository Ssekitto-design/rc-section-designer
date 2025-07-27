# plotting.py

import matplotlib.pyplot as plt

def plot_interaction_diagram(diagram: list, save_path: str = None):
    """
    Plots the interaction diagram with failure modes.

    Parameters:
    - diagram (list): Output from generate_interaction_diagram_with_modes()
    - save_path (str, optional): If given, saves the plot to file
    """
    colors = {
        "compression": "red",
        "tension": "blue",
        "balanced": "green",
        "other": "gray"
    }

    for pt in diagram:
        axial = pt['axial_kN']
        moment = pt['moment_kNm']
        mode = pt['failure_mode']
        plt.scatter(moment, axial, color=colors.get(mode, "gray"), s=20)

    plt.xlabel("Moment (kNm)")
    plt.ylabel("Axial Load (kN)")
    plt.title("M–N Interaction Diagram")
    plt.grid(True)

    if save_path:
        plt.savefig(save_path, dpi=300)
    else:
        plt.show()