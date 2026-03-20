import os
import random
from sivo import Sivo

def main():
    # SIVO enables hexagonal binning, taking a dense list of raw [x, y] coordinates
    # and automatically grouping them into an interactive hexagonal grid map.

    # 1. We create a simple geographic area
    svg_data = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100">
        <!-- A subtle background area -->
        <rect width="100" height="100" fill="#f8fafc" />
    </svg>"""

    sivo_app = Sivo.from_string(svg_data, title="City Traffic Incidents", subtitle="Hexagonal Binning Map")

    # 2. Simulate raw point data (e.g., traffic incidents or check-ins)
    # We'll create two clusters of dense points
    points = []

    # Cluster 1 (Center around 30, 30)
    for _ in range(500):
        points.append([random.gauss(30, 10), random.gauss(30, 10)])

    # Cluster 2 (Center around 70, 70)
    for _ in range(300):
        points.append([random.gauss(70, 15), random.gauss(70, 15)])

    # Noise
    for _ in range(200):
        points.append([random.uniform(0, 100), random.uniform(0, 100)])

    # 3. Apply the hexbin overlay
    # SIVO will automatically calculate the hex grid and aggregate the points into bins.
    sivo_app.apply_hexbin(
        points=points,
        hex_size=4.0, # The radius of each hexagon
        color_palette=["#fee0d2", "#de2d26", "#a50f15"], # Color gradient (low -> high)
        min_opacity=0.6,
        max_opacity=0.9,
        stroke_color="#ffffff",
        stroke_width=0.5
    )

    # 4. Export the result
    output_path = os.path.join(os.path.dirname(__file__), "interactive_hexbin.html")
    sivo_app.to_html(output_path)
    print(f"Exported Hexbin Example to {output_path}")

if __name__ == "__main__":
    main()
