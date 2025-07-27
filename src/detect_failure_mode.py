def detect_failure_mode(x, top_depth, bottom_depth, threshold=30):
    """
    Classify failure mode based on neutral axis vs. rebar positions.
    - x: neutral axis depth [mm]
    - top_depth: avg depth of top bars [mm]
    - bottom_depth: avg depth of bottom bars [mm]
    - threshold: sensitivity [mm]
    """
    neutral_to_tension = abs(x - bottom_depth)
    neutral_to_compression = abs(x - top_depth)

    if neutral_to_tension > threshold and x < (top_depth + bottom_depth) / 2:
        return "Tension-Controlled"
    elif neutral_to_compression > threshold and x > (top_depth + bottom_depth) / 2:
        return "Compression-Controlled"
    else:
        return "Balanced"