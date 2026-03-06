import os
from sivo import Sivo

def main():
    svg_path = os.path.join(os.path.dirname(__file__), "sample.svg")

    sivo_app = Sivo.from_svg(svg_path)

    # 1. Provide numeric data mapped to elements
    # Simulate data on features
    data = {
        "sun": 90,
        "mountain1": 20,
        "mountain2": 30,
        "house": 65,
        "river": 15
    }

    # 2. Automatically generate the heat map
    sivo_app.apply_choropleth(
        data_map=data,
        min_color="#add8e6", # Light blue
        max_color="#ff4500", # OrangeRed
        show_legend=True     # Render a UI legend automatically
    )

    # 3. Add tooltips for context
    for el, val in data.items():
        sivo_app.map(
            element_id=el,
            tooltip=f"{el.capitalize()}: {val}",
            glow=True
        )

    output_path = os.path.join(os.path.dirname(__file__), "output.html")
    sivo_app.to_html(output_path)
    print(f"Exported choropleth HTML to {output_path}")

if __name__ == "__main__":
    main()
