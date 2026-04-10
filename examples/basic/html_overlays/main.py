import os
from sivo import Sivo

def main():
    svg_path = os.path.join(os.path.dirname(__file__), "sample.svg")

    sivo_app = Sivo.from_svg(svg_path)

    # 1. Map typical interactions
    sivo_app.map(
        element_id="mountain1",
        tooltip="A mountain",
        color="#a0a0a0"
    )

    sivo_app.map(
        element_id="house",
        tooltip="A cozy house",
        color="brown"
    )

    # 2. Add HTML overlays over the map coordinates dynamically
    sivo_app.add_overlay(
        element_id="sun",
        html="<div style='background: white; padding: 5px 10px; border-radius: 8px; font-weight: bold; font-size: 18px; box-shadow: 0 4px 6px rgba(0,0,0,0.2); border: 2px solid gold;'>☀️ 30°C</div>",
        offset_x=40, # offset from the center
        offset_y=-40
    )

    sivo_app.add_overlay(
        element_id="house",
        html="<div style='background: #fff; padding: 4px 8px; border: 2px solid brown; font-size: 14px; border-radius: 4px;'>Home</div>",
        offset_x=0,
        offset_y=-40
    )

    output_path = os.path.join(os.path.dirname(__file__), "output.html")
    sivo_app.to_html(output_path)
    print(f"Exported interactive HTML to {output_path}")

if __name__ == "__main__":
    main()
