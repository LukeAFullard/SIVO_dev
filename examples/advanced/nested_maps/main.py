import os
from sivo import Sivo

def main():
    sivo_app = Sivo.from_svg(
        os.path.join(os.path.dirname(__file__), "main.svg"),
        title="Nested Maps Example",
        subtitle="Click Region A to open a detailed map inside the info panel"
    )

    # Read the submap SVG as a string so we can pass it as map_data
    with open(os.path.join(os.path.dirname(__file__), "submap.svg"), "r") as f:
        submap_svg = f.read()

    # Map the nested map chart to Region A
    sivo_app.map_nested_map_chart(
        element_id="regionA",
        title="Region A Districts",
        map_name="regionA_map",
        map_data=submap_svg,
        data=[
            {"name": "district1", "value": 80},
            {"name": "district2", "value": 40},
            {"name": "district3", "value": 100}
        ],
        min_val=0,
        max_val=100,
        color=["#fee2e2", "#991b1b"], # Red scale
        tooltip="Click to view district breakdown",
        panel_position="right"
    )

    sivo_app.map(
        "regionA",
        hover_color="#cbd5e1",
        glow=True
    )

    output_path = os.path.join(os.path.dirname(__file__), "output.html")
    sivo_app.to_html(output_path)
    print(f"Generated nested maps example at {output_path}")

if __name__ == "__main__":
    main()
