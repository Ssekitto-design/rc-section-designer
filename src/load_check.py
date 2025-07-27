# check_load.py

from collections import namedtuple
from detect_failure_mode import detect_failure_mode, FailureMode

# Output container
LoadCheckResult = namedtuple("LoadCheckResult", [
    "is_safe",
    "applied_N",
    "applied_M",
    "resisting_N",
    "resisting_M",
    "failure_mode"
])

def validate_section(fc, fy, b, h, rebar_layout, design_N, design_M):
    # Simplified placeholder logic
    capacity_N = fc * b * h * 0.4
    capacity_M = fy * sum(rebar_layout) * h * 0.5

    passes_N = design_N <= capacity_N
    passes_M = design_M <= capacity_M

    return {
        "passes_N": passes_N,
        "passes_M": passes_M,
        "capacity_N": capacity_N,
        "capacity_M": capacity_M
    }

def check_load(
    applied_N: float,
    applied_M: float,
    resisting_N: float,
    resisting_M: float,
    strain_top: float,
    strain_bottom: float,
    x: float,
    section_depth_mm: float,
    eps_cu: float = 0.0035,
    eps_su: float = 0.010
) -> LoadCheckResult:
    """
    Evaluates whether applied loads exceed section capacity.

    Parameters:
        applied_N (float): Applied axial load (N)
        applied_M (float): Applied moment (N·mm)
        resisting_N (float): Capacity axial force (N)
        resisting_M (float): Capacity moment (N·mm)
        strain_top (float): Top fiber strain
        strain_bottom (float): Bottom fiber strain
        x (float): Neutral axis depth (mm)
        section_depth_mm (float): Section total depth (mm)
        eps_cu (float): Ultimate concrete strain
        eps_su (float): Ultimate steel strain

    Returns:
        LoadCheckResult: Named tuple with:
            - is_safe (bool): True if within capacity
            - applied/resisting loads (N, N·mm)
            - failure_mode (FailureMode): Failure type
    """
    safe = (applied_N <= resisting_N) and (applied_M <= resisting_M)

    failure = detect_failure_mode(
        x=x,
        section_depth_mm=section_depth_mm,
        strain_top=strain_top,
        strain_bottom=strain_bottom,
        eps_cu=eps_cu,
        eps_su=eps_su
    )

    return LoadCheckResult(
        is_safe=safe,
        applied_N=applied_N,
        applied_M=applied_M,
        resisting_N=resisting_N,
        resisting_M=resisting_M,
        failure_mode=failure
    )