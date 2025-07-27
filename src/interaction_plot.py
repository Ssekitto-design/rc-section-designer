# interaction_plot.py

import matplotlib.pyplot as plt
from typing import List
from interaction_diagram import InteractionPoint
from plotting import setup_plot_theme  # You’ll define this in plotting.py

def save_plot(P_kN, M_kNm, filename):
    """Save interaction diagram as PNG."""
    plt.figure()
    plt.plot(M_kNm, P_kN, label="Interaction Diagram", color="teal")
    plt.xlabel("Moment [kNm]")
    plt.ylabel("Axial Force [kN]")
    plt.title("P-M Interaction Diagram")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(filename)
    plt.close()


def plot_interaction_diagram(
    points: List[InteractionPoint],
    title: str = "Axial-Moment Interaction Diagram",
    show_plot: bool = True,
    save_path: str = None
):
    """
    Plots the interaction diagram using axial force vs. bending moment.

    Parameters:
        points (List[InteractionPoint]): Interaction points from stress block
        title (str): Plot title
        show_plot (bool): If True, display plot in window
        save_path (str): If set, saves plot to given path
    """
    setup_plot_theme()  # Loads font, grid, background from plotting.py

    axial = [p.axial_force_N / 1e3 for p in points]   # kN
    moment = [p.bending_moment_Nmm / 1e6 for p in points]  # kNm

    plt.figure(figsize=(6, 5))
    plt.plot(axial, moment, label='Concrete Only', color='darkorange', linewidth=2)
    plt.title(title, fontsize=14, weight="bold")
    plt.xlabel("Axial Force P [kN]", fontsize=12)
    plt.ylabel("Bending Moment M [kNm]", fontsize=12)
    plt.grid(True, which="both", linestyle="--", alpha=0.3)
    plt.legend(loc="upper right", fontsize=10)
    plt.tight_layout()

    if save_path:
        plt.savefig(save_path)
    if show_plot:
        plt.show()
    plt.close()