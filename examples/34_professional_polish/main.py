import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src')))

from sivo import Sivo

def main():
    # Load sample SVG from the root examples folder (or create one on the fly)
    svg_path = os.path.join(os.path.dirname(__file__), '../sample.svg')

    # We will initialize the sivo instance directly to enable the new parameters
    sivo_app = Sivo.from_svg(
        svg_path,
        title="Global Demographic Insights",
        subtitle="An interactive exploration of 2024 population density.",
        attribution="Data Source: World Bank | Powered by SIVO",
        enable_fullscreen=True,
        enable_share=True,
        enable_data_download=True,
        enable_export=True,
        enable_search=True
    )

    # Some mock data binding
    data = {
        "region_a": {"Population": 50000},
        "region_b": {"Population": 120000},
        "region_c": {"Population": 35000}
    }

    sivo_app.bind_data(
        data=data,
        key="Population",
        colors=["#e0f2fe", "#0284c7"],
        min_val=0,
        max_val=150000
    )

    output_file = os.path.join(os.path.dirname(__file__), 'output.html')
    sivo_app.to_html(output_file)
    print(f"Generated {output_file}")

if __name__ == "__main__":
    main()
