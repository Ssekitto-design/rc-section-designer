# plot_utils.py

import matplotlib.pyplot as plt

def plot_interaction_diagram(P, M, title="Interaction Diagram", label="Interaction Curve"):
    plt.plot(P, M, label=label, color="navy", linewidth=2.5)
    plt.title(title, fontsize=14, weight="bold")
    plt.xlabel("Axial Force P [kN]", fontsize=12)
    plt.ylabel("Bending Moment M [kNm]", fontsize=12)
    plt.grid(True, which="both", linestyle="--", alpha=0.3)
    plt.legend(loc="upper right", fontsize=10)
    plt.tight_layout()
    plt.show()

def save_plot(P, M, filename="interaction_diagram.png", dpi=300):
    import matplotlib.pyplot as plt

    plt.plot(P, M, label="Interaction Curve", color="navy", linewidth=2.5)
    plt.title("Interaction Diagram", fontsize=14, weight="bold")
    plt.xlabel("Axial Force P [kN]")
    plt.ylabel("Bending Moment M [kNm]")
    plt.grid(True, which="both", linestyle="--", alpha=0.3)
    plt.legend()
    plt.tight_layout()
    plt.savefig(filename, dpi=dpi)
    plt.close()

    print(f"🖼️ Diagram saved to {filename}")