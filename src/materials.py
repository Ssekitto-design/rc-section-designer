#defining the concrete and steel material properties using Eurocode 2

class Material:
    def __init__(self, name, fck=None, fyk=None, unit_weight=None):
        self.name = name
        self.fck = fck       # concrete strength (MPa)
        self.fyk = fyk       # steel yield strength (MPa)
        self.unit_weight = unit_weight  # kN/m³

        # Design strengths (Eurocode partial safety factors)
        if fck:
            self.fcd = self.fck / 1.5
        if fyk:
            self.fyd = self.fyk / 1.15

    def __repr__(self):
        props = [f"{self.name}"]
        if self.fck: props.append(f"fck={self.fck} MPa → fcd={self.fcd:.2f} MPa")
        if self.fyk: props.append(f"fyk={self.fyk} MPa → fyd={self.fyd:.2f} MPa")
        return " | ".join(props)

