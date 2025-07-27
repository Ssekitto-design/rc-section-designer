# rebar.py

from math import pi


class RebarGroup:
    """
    Represents a group of reinforcement bars at a given depth.

    Attributes:
        diameter_mm (float): Bar diameter in millimeters.
        count (int): Number of bars in the group.
        depth_mm (float): Depth of bars from top fiber (mm).
    """

    def __init__(self, diameter_mm: float, count: int, depth_mm: float):
        if diameter_mm <= 0:
            raise ValueError("Bar diameter must be positive.")
        if count <= 0:
            raise ValueError("Bar count must be a positive integer.")
        if depth_mm <= 0:
            raise ValueError("Bar depth must be positive.")

        self.diameter_mm = diameter_mm
        self.count = count
        self.depth_mm = depth_mm

    @property
    def area_mm2(self) -> float:
        """Returns total area of the group in mm²."""
        single_area = (pi * self.diameter_mm ** 2) / 4
        return single_area * self.count

    def __repr__(self) -> str:
        return f"{self.count}ø{self.diameter_mm} @ {self.depth_mm}mm"


class RebarLayout:
    """
    Manages layout of all rebar groups in a concrete section.

    Methods:
        add_group(diameter_mm, count, depth_mm): Adds a rebar group.
        load_from_list(data): Loads layout from list of dicts.
        total_area(): Returns total steel area (mm²).
        __repr__(): Preview-friendly layout string.
    """

    def __init__(self):
        self.groups = []

    def add_group(self, diameter_mm: float, count: int, depth_mm: float):
        group = RebarGroup(diameter_mm, count, depth_mm)
        self.groups.append(group)

    def load_from_list(self, data: list[dict]):
        """
        Bulk-loads rebar layout from a list of dictionaries.

        Each dict must have keys: 'diameter', 'count', 'depth'
        """
        for entry in data:
            try:
                self.add_group(entry['diameter'], entry['count'], entry['depth'])
            except KeyError as e:
                raise KeyError(f"Missing key in rebar entry: {e}")

    def total_area(self) -> float:
        """Returns total steel area across all groups (mm²)."""
        return sum(group.area_mm2 for group in self.groups)

    def __iter__(self):
        return iter(self.groups)

    def __repr__(self) -> str:
        if not self.groups:
            return "No rebar groups defined"
        return "Rebar Layout:\n  " + "\n  ".join(str(g) for g in self.groups)