import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src')))

from sivo import Sivo

def main():
    svg_path = os.path.join(os.path.dirname(__file__), '../sample.svg')

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

    sivo_app.map(
        element_id="mountain1",
        tooltip="Mountain 1",
        color="#a0a0a0",
        hover_color="#c0c0c0"
    )

    sivo_app.map(
        element_id="sun",
        tooltip="The Sun",
        color="gold",
        hover_color="yellow"
    )

    output_file = os.path.join(os.path.dirname(__file__), 'output.html')
    sivo_app.to_html(output_file)
    print(f"Generated {output_file}")

if __name__ == "__main__":
    main()