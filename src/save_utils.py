# save_utils.py

import json
from datetime import datetime
from os import makedirs
from os.path import join, exists

def save_summary(material, section, points, out_dir="exports", filename=None):
    """
    Saves a JSON summary of material, section, and key interaction stats.

    Parameters:
        material: Material object with .to_dict()
        section: Section object with .to_dict()
        points: List of InteractionPoint
        out_dir (str): Folder to save file
        filename (str): Optional override of filename
    """
    if not exists(out_dir):
        makedirs(out_dir)

    # Extract key metrics
    max_P = max(pt.axial_force_N for pt in points) / 1000     # kN
    max_M = max(pt.bending_moment_Nmm for pt in points) / 1e6 # kNm

    data = {
        "timestamp": datetime.now().isoformat(timespec="seconds"),
        "material": material.to_dict(),
        "section": section.to_dict(),
        "interaction_maxima": {
            "max_axial_kN": round(max_P, 2),
            "max_moment_kNm": round(max_M, 2)
        },
        "point_count": len(points)
    }

    fname = filename or f"summary_{section.width_mm}x{section.depth_mm}.json"
    path = join(out_dir, fname)

    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

    print(f"📁 Summary saved to {path}")