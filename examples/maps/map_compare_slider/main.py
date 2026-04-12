import os
from sivo import Sivo

def main():
    # 1. Base Map (e.g. 2020 Data)
    svg_left = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 600">
        <rect id="bg" width="1000" height="600" fill="#f8fafc" />
        <circle id="region1" cx="300" cy="300" r="150" fill="#94a3b8" />
        <circle id="region2" cx="700" cy="300" r="150" fill="#94a3b8" />
        <text x="500" y="50" font-family="sans-serif" font-size="24" fill="#333" text-anchor="middle">2020 Regional Data</text>
    </svg>"""

    sivo_left = Sivo.from_string(
        svg_left,
        title="Regional Growth Comparison",
        subtitle="Swipe to see changes from 2020 to 2024",
        default_panel_position="overlay",
        bounding_coords=[[0, 0], [1000, 600]]
    )
    sivo_left.map("region1", html="<h3>Region 1 - 2020</h3>", color="#cbd5e1")
    sivo_left.map("region2", html="<h3>Region 2 - 2020</h3>", color="#cbd5e1")


    # 2. Secondary Map (e.g. 2024 Data)
    svg_right = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 600">
        <rect id="bg" width="1000" height="600" fill="#f8fafc" />
        <circle id="region1" cx="300" cy="300" r="150" fill="#94a3b8" />
        <circle id="region2" cx="700" cy="300" r="150" fill="#94a3b8" />
        <text x="500" y="50" font-family="sans-serif" font-size="24" fill="#333" text-anchor="middle">2024 Regional Data</text>
    </svg>"""

    # Adding empty title and subtitle to right to ensure both SVGs are scaled to the same size natively
    # Using bounding_coords to ensure they lock into the same native coordinate system projection
    sivo_right = Sivo.from_string(
        svg_right,
        title="Regional Growth Comparison",
        subtitle="Swipe to see changes from 2020 to 2024",
        default_panel_position="overlay",
        bounding_coords=[[0, 0], [1000, 600]]
    )
    sivo_right.map("region1", html="<h3>Region 1 - 2024 (Growth)</h3><p>Significant increase observed.</p>", color="#10b981") # Green
    sivo_right.map("region2", html="<h3>Region 2 - 2024 (Decline)</h3><p>Decrease in region metrics.</p>", color="#ef4444") # Red

    # 3. Export as Compare Slider
    output_file = os.path.join(os.path.dirname(__file__), 'output.html')
    sivo_left.to_html_compare(sivo_right, output_file)
    print(f"Generated Compare Slider Example at {output_file}")

if __name__ == "__main__":
    main()
