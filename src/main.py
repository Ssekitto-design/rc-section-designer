# main.py

from cli import parse_cli_args
from materials import Material
from section import Section
from interaction_diagram import generate_interaction_diagram
from interaction_plot import plot_interaction_diagram
from save_utils import save_summary


def run_designer():
    """
    Central routine that initializes objects, generates interaction diagram,
    and optionally visualizes output.
    """
    # Step 1: Parse CLI
    args = parse_cli_args()

    # Step 2: Build material + section
    material = Material(
        name=f"C{args['fck']}",
        fck=args['fck'],
        fyk=args['fyk'],
        code=args['code']
    )

    section = Section(
        width_mm=args['width_mm'],
        depth_mm=args['depth_mm']
    )

    # Preview Summary Block
    from utils import banner, format_summary

    print(banner("Material Summary"))
    print(format_summary(material.to_dict()))

    print(banner("Section Geometry"))
    print(format_summary(section.to_dict()))

    # Step 3: Generate interaction diagram
    points = generate_interaction_diagram(
        width_mm=section.width_mm,
        depth_mm=section.depth_mm,
        f_cd=material.fcd
    )

    # Export summary block
    if args["save_summary"]:
        save_summary(material, section, points)

    # Step 4: Plot diagram
    plot_interaction_diagram(
        points=points,
        title=f"{material.name} | {section.width_mm}×{section.depth_mm} mm"
    )

    # Step 5: Preview key point (optional debug)
    print(f"\n▶ First Point: N={points[0].axial_force_N:.1f} N, M={points[0].bending_moment_Nmm:.1f} N·mm")

    # Step 6: Save plot if requested
    from interaction_plot import save_plot  # Make sure this import exists at the top or right here

    if args["save_diagram"]:
        P = [pt.axial_force_N / 1000 for pt in points]  # kN
        M = [pt.bending_moment_Nmm / 1e6 for pt in points]  # kNm

        filename = f"exports/diagram_{section.width_mm}x{section.depth_mm}.png"
        save_plot(P, M, filename=filename)
        print(f"✅ Diagram saved to {filename}")


if __name__ == "__main__":
    run_designer()