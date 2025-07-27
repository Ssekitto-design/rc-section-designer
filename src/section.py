# defining concrete class with Effective depth and geometry check
from src.materials import Material


class Section:
    def __init__(self, b, h, cover, material: Material):
        self.b = b                  # Width (mm)
        self.h = h                  # Height (mm)
        self.cover = cover          # Cover (mm)
        self.material = material

        # Effective depth approximation (assuming bottom bars)
        self.d = self.h - self.cover

    def area(self):
        """Returns gross concrete area in mm²"""
        return self.b * self.h

    def __repr__(self):
        return f"Section: {self.b}mm × {self.h}mm | Cover: {self.cover}mm | d ≈ {self.d}mm"