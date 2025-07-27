# rebar.py

import math

class RebarLayout:
    """
    Stores and manages groups of reinforcing bars in a concrete section.

    Each group includes:
    - Diameter (mm)
    - Bar count
    - Depth from compression face (mm)
    - Total steel area in mm²

    Methods:
    - add_group(): Adds a rebar group to the layout
    - total_steel_area(): Computes total steel area As
    - compute_bar_area(): Helper for area of a single bar
    - sort_by_depth(): Optional, sorts groups by vertical position
    - to_dict(): Converts layout to list of group dictionaries
    """

    def __init__(self):
        self.bars = []  # Each bar group is a dict

    def add_group(self, diameter_mm: float, count: int, depth_mm: float):
        """
        Adds a group of identical bars to the layout.

        Parameters:
        - diameter_mm (float): Diameter of each bar in mm
        - count (int): Number of bars in the group
        - depth_mm (float): Vertical position from top (compression face) in mm
        """
        area_per_bar = self.compute_bar_area(diameter_mm)
        total_area = count * area_per_bar

        self.bars.append({
            "diameter": diameter_mm,
            "count": count,
            "depth": depth_mm,
            "area_mm2": total_area
        })

    def compute_bar_area(self, diameter_mm: float) -> float:
        """
        Computes area of a single bar.

        Parameters:
        - diameter_mm (float): Diameter in mm

        Returns:
        - float: Cross-sectional area in mm²
        """
        return math.pi * (diameter_mm / 2) ** 2

    def total_steel_area(self) -> float:
        """
        Returns total area of steel reinforcement in the layout.

        Returns:
        - float: Cumulative As in mm²
        """
        return sum(bar["area_mm2"] for bar in self.bars)

    def sort_by_depth(self, reverse: bool = False):
        """
        Sorts rebar groups by depth (vertical position).

        Parameters:
        - reverse (bool): If True, sorts deepest to shallowest
        """
        self.bars.sort(key=lambda bar: bar["depth"], reverse=reverse)

    def to_dict(self) -> list:
        """
        Converts layout to list of rebar group dictionaries.

        Returns:
        - list: Rebar layout metadata
        """
        return self.bars

    def __repr__(self) -> str:
        layout_str = "\n".join(
            f"Ø{bar['diameter']} × {bar['count']} @ {bar['depth']}mm → {bar['area_mm2']:.1f} mm²"
            for bar in self.bars
        )
        return f"Rebar Layout:\n{layout_str}\nTotal As = {self.total_steel_area():.1f} mm²"