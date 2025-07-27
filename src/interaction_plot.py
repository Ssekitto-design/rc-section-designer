import matplotlib.pyplot as plt
from typing import List, Optional
from interaction_diagram import InteractionPoint
from plotting import setup_plot_theme  # Centralized styling

def plot_interaction_diagram(
    points: List[InteractionPoint],
    title: str = "Axial-Moment Interaction Diagram",
    show_plot: bool = True,
    save_path: Optional[str] = None
) -> plt.Figure:
    """
    Generates and returns a Matplotlib figure for an interaction diagram.

    Parameters:
        points (List[InteractionPoint]): Interaction points from stress block
        title (str): Plot title
        show_plot (bool): If True, display the plot window
        save_path (str): If set, saves plot to given path

    Returns:
        fig (plt.Figure): The created matplotlib figure object
    """
    setup_plot_theme()

    axial = [p.axial_force_N / 1e3 for p in points]    # Convert to kN
    moment = [p.bending_moment_Nmm / 1e6 for p in points]  # Convert to kNm

    fig, ax = plt.subplots(figsize=(6, 5))
    ax.plot(axial, moment, label="Interaction Curve", color="darkorange", linewidth=2)

    ax.set_xlabel("Axial Force P [kN]", fontsize=12)
    ax.set_ylabel("Bending Moment M [kNm]", fontsize=12)
    ax.set_title(title, fontsize=14, weight="bold")

    ax.grid(True, which="both", linestyle="--", alpha=0.3)
    ax.legend(loc="upper right", fontsize=10)

    fig.tight_layout()

    if save_path:
        fig.savefig(save_path, dpi=150)
    if show_plot:
        fig.show()

    return fig