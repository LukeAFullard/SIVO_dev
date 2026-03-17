from sivo import Sivo
import os

def create_example():
    # Base dummy SVG
    svg_str = """
    <svg viewBox="0 0 1000 600" xmlns="http://www.w3.org/2000/svg">
        <!-- Background -->
        <rect id="bg" width="1000" height="600" fill="#f0fdf4" />

        <!-- UI Card -->
        <rect id="card" x="400" y="250" width="200" height="100" rx="10" fill="#ffffff" stroke="#cbd5e1" />
        <text id="card_text" x="500" y="305" font-family="sans-serif" font-size="24" text-anchor="middle" fill="#0f172a">Ambient Effects</text>
    </svg>
    """

    # 1. Wind Example
    app_wind = Sivo.from_string(
        svg_str,
        title="Ambient Effect: Wind",
        ambient_effect="wind",
        ambient_speed=2.5,
        theme="light",
        disable_zoom_controls=True
    )
    with open(os.path.join(os.path.dirname(__file__), "wind_effect.html"), "w") as f:
        f.write(app_wind.to_html())

    # 2. Water Example
    app_water = Sivo.from_string(
        svg_str,
        title="Ambient Effect: Water",
        ambient_effect="water",
        ambient_speed=0.5,
        theme="light",
        disable_zoom_controls=True
    )
    with open(os.path.join(os.path.dirname(__file__), "water_effect.html"), "w") as f:
        f.write(app_water.to_html())

    # 3. Tree Example
    app_tree = Sivo.from_string(
        svg_str,
        title="Ambient Effect: Growing Tree",
        ambient_effect="tree",
        ambient_speed=0.8,
        theme="light",
        disable_zoom_controls=True
    )
    with open(os.path.join(os.path.dirname(__file__), "tree_effect.html"), "w") as f:
        f.write(app_tree.to_html())

if __name__ == "__main__":
    create_example()
    print("Examples generated successfully in examples/55_ambient_effects/")
