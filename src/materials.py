# materials.py

from enum import Enum

class DesignCode(Enum):
    EUROCODE = 'EUROCODE'
    ACI = 'ACI'

# Partial safety factors by design code
DESIGN_CODE_FACTORS = {
    DesignCode.EUROCODE: {'gamma_c': 1.5, 'gamma_s': 1.15},
    DesignCode.ACI: {'gamma_c': 1.0, 'gamma_s': 1.0}  # Placeholder — customize if needed
}

class Material:
    """
    Represents structural material properties for concrete or steel.

    Parameters:
        name (str): Identifier (e.g. 'C30/37', 'B500B')
        fck (float, optional): Concrete compressive strength (MPa)
        fyk (float, optional): Steel yield strength (MPa)
        unit_weight (float, optional): Density in kN/m³
        code (DesignCode): Selected design code standard

    Attributes:
        fcd (float): Design compressive strength (MPa)
        fyd (float): Design yield strength (MPa)
    """

    def __init__(
        self,
        name: str,
        fck: float = None,
        fyk: float = None,
        unit_weight: float = None,
        code: DesignCode = DesignCode.EUROCODE
    ):
        self.name = name
        self.fck = fck
        self.fyk = fyk
        self.unit_weight = unit_weight
        self.code = code

        self._apply_design_factors()

    def _apply_design_factors(self):
        factors = DESIGN_CODE_FACTORS.get(self.code, {})
        self.fcd = self.fck / factors['gamma_c'] if self.fck else None
        self.fyd = self.fyk / factors['gamma_s'] if self.fyk else None

    def to_dict(self) -> dict:
        """Returns a dictionary of material properties."""
        return {
            'name': self.name,
            'fck': self.fck,
            'fcd': self.fcd,
            'fyk': self.fyk,
            'fyd': self.fyd,
            'unit_weight': self.unit_weight,
            'code': self.code.value
        }

    def __repr__(self) -> str:
        summary = [self.name]
        if self.fck:
            summary.append(f"fck={self.fck} MPa → fcd={self.fcd:.2f} MPa ({self.code.value})")
        if self.fyk:
            summary.append(f"fyk={self.fyk} MPa → fyd={self.fyd:.2f} MPa ({self.code.value})")
        return " | ".join(summary)