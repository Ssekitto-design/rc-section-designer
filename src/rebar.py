import math

class RebarLayout:
    def __init__(self):
        self.bars = []  # List of dicts: {"diameter": mm, "count": n, "depth": mm}

    def add_group(self, diameter_mm, count, depth_mm):
        area_per_bar = math.pi * (diameter_mm / 2) ** 2
        total_area = count * area_per_bar

        self.bars.append({
            "diameter": diameter_mm,
            "count": count,
            "depth": depth_mm,
            "area_mm2": total_area
        })

    def total_steel_area(self):
        return sum(bar["area_mm2"] for bar in self.bars)

    def __repr__(self):
        layout_str = "\n".join(
            f"Ø{bar['diameter']} × {bar['count']} @ {bar['depth']}mm → {bar['area_mm2']:.1f} mm²"
            for bar in self.bars
        )
        return f"Rebar Layout:\n{layout_str}\nTotal As = {self.total_steel_area():.1f} mm²"