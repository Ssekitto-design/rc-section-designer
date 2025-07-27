def detect_failure_mode(neutral_axis_depth: float, top_bar_depth: float,
                        bottom_bar_depth: float, threshold: float = 30.0) -> str:
    """
    Classifies section failure mode using neutral axis position relative to rebar zones.

    Parameters:
    - neutral_axis_depth (float): Depth of neutral axis from extreme compression fiber (mm)
    - top_bar_depth (float): Average depth of top (compression zone) rebars (mm)
    - bottom_bar_depth (float): Average depth of bottom (tension zone) rebars (mm)
    - threshold (float): Sensitivity margin for determining dominance (mm)

    Returns:
    - str: 'Tension-Controlled', 'Compression-Controlled', or 'Balanced'
    """
    dist_to_tension = abs(neutral_axis_depth - bottom_bar_depth)
    dist_to_compression = abs(neutral_axis_depth - top_bar_depth)
    mid_depth = (top_bar_depth + bottom_bar_depth) / 2

    if dist_to_tension > threshold and neutral_axis_depth < mid_depth:
        return "Tension-Controlled"
    elif dist_to_compression > threshold and neutral_axis_depth > mid_depth:
        return "Compression-Controlled"
    else:
        return "Balanced"