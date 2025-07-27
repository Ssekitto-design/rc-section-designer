# section.py

from dataclasses import dataclass
from typing import Optional

@dataclass
class Section:
    width_mm: float
    depth_mm: float

    @property
    def area_mm2(self) -> float:
        """Cross-sectional area (mm²)"""
        return self.width_mm * self.depth_mm

    @property
    def centroid_mm(self) -> float:
        """Centroid from top fiber (mm)"""
        return self.depth_mm / 2

    @property
    def inertia_mm4(self) -> float:
        """Moment of inertia about horizontal axis (mm⁴)"""
        return (self.width_mm * self.depth_mm**3) / 12

    def to_dict(self) -> dict:
        """Export geometric properties to a dictionary."""
        return {
            'width_mm': self.width_mm,
            'depth_mm': self.depth_mm,
            'area_mm2': self.area_mm2,
            'centroid_mm': self.centroid_mm,
            'inertia_mm4': self.inertia_mm4,
        }

    def __repr__(self) -> str:
        return f"Section {self.width_mm}×{self.depth_mm} mm | Area={self.area_mm2:.2f} mm² | Centroid={self.centroid_mm:.1f} mm"