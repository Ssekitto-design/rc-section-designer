# Rectangular section.py

from src.materials import Material

class Section:
    """
    Represents a rectangular reinforced concrete section.

    Parameters:
    - b (float): Width of the section in mm
    - h (float): Height of the section in mm
    - cover (float): Concrete cover to reinforcement in mm
    - material (Material): Structural material object

    Attributes:
    - d (float): Effective depth (mm), approximated as h - cover
    """

    def __init__(self, b: float, h: float, cover: float, material: Material):
        self.b = b
        self.h = h
        self.cover = cover
        self.material = material

        # Effective depth approximation (assuming tension reinforcement near bottom face)
        self.d = self.h - self.cover

    def area(self) -> float:
        """
        Computes gross area of the concrete section.

        Returns:
        - float: Area in mm²
        """
        return self.b * self.h

    def to_dict(self) -> dict:
        """
        Converts section properties to dictionary format.

        Returns:
        - dict: Section dimensions and material data
        """
        return {
            'width_mm': self.b,
            'height_mm': self.h,
            'cover_mm': self.cover,
            'effective_depth_mm': self.d,
            'material': self.material.to_dict()
        }

    def __repr__(self) -> str:
        return (
            f"Section: {self.b}mm × {self.h}mm | "
            f"Cover: {self.cover}mm | "
            f"d ≈ {self.d:.1f}mm"
        )