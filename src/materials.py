# material.py

from enum import Enum

class DesignCode(Enum):
    EUROCODE = 'EUROCODE'
    ACI = 'ACI'

DESIGN_CODE_FACTORS = {
    DesignCode.EUROCODE: {'gamma_c': 1.5, 'gamma_s': 1.15},
    DesignCode.ACI: {'gamma_c': 1.0, 'gamma_s': 1.0}  # Placeholder — adjust as needed
}

class Material:
    """
    Represents structural material properties for concrete or steel.

    Parameters:
    - name (str): Identifier for material (e.g. 'C30/37' or 'B500B')
    - fck (float, optional): Characteristic compressive strength of concrete in MPa
    - fyk (float, optional): Characteristic yield strength of steel in MPa
    - unit_weight (float, optional): Material density in kN/m³
    - code (DesignCode): Selected design code standard (Eurocode or ACI)

    Attributes:
    - fcd (float): Design compressive strength (depends on code)
    - fyd (float): Design yield strength (depends on code)
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

        factors = DESIGN_CODE_FACTORS[self.code]
        self.fcd = self.fck / factors['gamma_c'] if self.fck else None
        self.fyd = self.fyk / factors['gamma_s'] if self.fyk else None

    def __repr__(self) -> str:
        props = [f"{self.name}"]
        if self.fck:
            props.append(f"fck={self.fck} MPa → fcd={self.fcd:.2f} MPa ({self.code.value})")
        if self.fyk:
            props.append(f"fyk={self.fyk} MPa → fyd={self.fyd:.2f} MPa ({self.code.value})")
        return " | ".join(props)

    def to_dict(self) -> dict:
        """
        Converts material properties to a dictionary format.

        Returns:
        - dict: Material data including design code and strengths
        """
        return {
            'name': self.name,
            'fck': self.fck,
            'fcd': self.fcd,
            'fyk': self.fyk,
            'fyd': self.fyd,
            'unit_weight': self.unit_weight,
            'code': self.code.value
        }