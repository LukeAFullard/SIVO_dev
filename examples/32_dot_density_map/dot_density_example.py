import os
from sivo import Sivo

def main():
    # SIVO supports Dot Density maps, where a regional count (e.g., population)
    # is represented by randomly placing dots inside the specific boundary of the region.

    # 1. We create an SVG with several irregular shapes (districts/zones)
    svg_data = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200">
        <!-- Zone A (Triangle-ish) -->
        <path id="zoneA" d="M 20 20 L 80 20 L 50 80 Z" fill="#e2e8f0" stroke="#cbd5e1" stroke-width="2" />

        <!-- Zone B (L-Shape) -->
        <path id="zoneB" d="M 100 20 L 180 20 L 180 180 L 140 180 L 140 80 L 100 80 Z" fill="#e2e8f0" stroke="#cbd5e1" stroke-width="2" />

        <!-- Zone C (Circle/Ellipse) -->
        <path id="zoneC" d="M 50 140 A 30 30 0 1 0 50 141 Z" fill="#e2e8f0" stroke="#cbd5e1" stroke-width="2" />
    </svg>"""

    sivo_app = Sivo.from_string(svg_data, title="Population Density", subtitle="1 Dot = 100 People")

    # 2. Add tooltips so we can interact with the zones
    sivo_app.map("zoneA", tooltip="Zone A: 12,000 people")
    sivo_app.map("zoneB", tooltip="Zone B: 35,000 people")
    sivo_app.map("zoneC", tooltip="Zone C: 20,000 people")

    # 3. Define the data mapping (Scalar counts per region)
    data = {
        "zoneA": 12000,
        "zoneB": 35000,
        "zoneC": 20000
    }

    # 4. Apply Dot Density
    # SIVO extracts the exact SVG paths from the file and executes a strict point-in-polygon
    # algorithm in the JS runtime using Canvas Path2D to ensure dots never bleed outside the lines.
    sivo_app.apply_dot_density(
        data_map=data,
        dot_size=3.0,
        dot_color="rgba(37, 99, 235, 0.7)", # Blue dots
        dots_per_value=1 / 100 # 1 dot represents 100 people
    )

    # 5. Export the result
    output_path = os.path.join(os.path.dirname(__file__), "interactive_dot_density.html")
    sivo_app.to_html(output_path)
    print(f"Exported Dot Density Example to {output_path}")

if __name__ == "__main__":
    main()
