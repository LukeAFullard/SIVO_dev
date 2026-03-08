import os
from sivo import Sivo

def main():
    svg_path = os.path.join(os.path.dirname(__file__), "sample.svg")

    # 1. Initialize SIVO with the base SVG
    sivo_app = Sivo.from_svg(svg_path)

    # 2. Provide a dataset mapping SVG IDs to numeric values
    data = {
        "TX": {"sales": 15000},
        "CA": {"sales": 22000},
        "NY": {"sales": 8000},
        "WY": {"sales": 500}
    }

    # 3. Bind data to SVG IDs with a color scale
    sivo_app.bind_data(
        data=data,
        key="sales",                     # The metric to base the color on
        colors=["#e0f3db", "#43a2ca"],   # Gradient from min to max
        min_val=0,
        max_val=25000
    )

    # 4. Optional: add a generic tooltip
    # ECharts will automatically append "sales: {value}" to the tooltip!
    for state in data.keys():
        sivo_app.map(element_id=state, tooltip=f"State: {state}")

    # 5. Export to an interactive HTML bundle
    output_path = os.path.join(os.path.dirname(__file__), "output.html")
    sivo_app.to_html(output_path)
    print(f"Exported data binding HTML to {output_path}")

if __name__ == "__main__":
    main()
