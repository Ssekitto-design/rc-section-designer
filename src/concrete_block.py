def compute_concrete_block(x: float, width: float, f_cd: float,
                           alpha: float = 0.85, gamma: float = 0.8) -> tuple[float, float]:
    """
    Computes the resultant force and moment of the concrete stress block.

    Parameters:
    - x (float): Neutral axis depth [mm]
    - width (float): Section width [mm]
    - f_cd (float): Design compressive strength of concrete [MPa]
    - alpha (float): Stress factor (default = 0.85)
    - gamma (float): Depth factor for equivalent rectangular stress block (default = 0.8)

    Returns:
    - tuple: (Concrete compressive force [kN], Moment about top fiber [kNm])
    """
    a = gamma * x                             # Depth of equivalent block
    force = alpha * f_cd * width * a / 1000   # Convert N to kN
    moment = force * (a / 2) / 1000           # Moment in kNm

    return force, moment