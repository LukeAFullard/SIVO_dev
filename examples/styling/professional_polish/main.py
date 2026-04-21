import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src')))

from sivo import Sivo

def main():
    svg_path = os.path.join(os.path.dirname(__file__), 'sample.svg')

    sivo_app = Sivo.from_svg(
        svg_path,
        title="Global Demographic Insights",
        subtitle="An interactive exploration of 2024 population density.",
        attribution="Data Source: World Bank | Powered by SIVO",
        watermark="Confidential & Proprietary",
        enable_fullscreen=True,
        enable_share=True,
        enable_data_download=True,
        enable_export=True,
        enable_search=True,
        default_panel_position="right",
        theme="dark"
    )

    sivo_app.map(
        element_id="mountain1",
        tooltip="Mountain Peak",
        color="#a0a0a0",
        hover_color="#c0c0c0",
        html="""
        <div style='padding:15px; font-family:sans-serif;'>
            <h3 style='color:#333; border-bottom:1px solid #ccc; padding-bottom:5px;'>Mountain Peak Insights</h3>
            <p style='color:#555;'>This section provides a detailed look at the demographic spread across the mountainous region. Notice the sparseness in higher altitudes.</p>
        </div>
        """,
        panel_position="right"
    )

    sivo_app.map(
        element_id="sun",
        tooltip="The Sun",
        color="gold",
        hover_color="yellow",
        html="""
        <div style='padding:15px; font-family:sans-serif;'>
            <h3 style='color:#333; border-bottom:1px solid #ccc; padding-bottom:5px;'>Solar Impact</h3>
            <p style='color:#555;'>Solar energy is a key factor in the demographic growth of this region.</p>
        </div>
        """,
        panel_position="left"
    )

    sivo_app.map(
        element_id="house",
        tooltip="Settlement",
        color="brown",
        hover_color="red",
        html="""
        <div style='padding:15px; font-family:sans-serif;'>
            <h3 style='color:#333; border-bottom:1px solid #ccc; padding-bottom:5px;'>Local Settlement</h3>
            <p style='color:#555;'>A primary settlement located near the river and mountains.</p>
        </div>
        """,
        panel_position="bottom"
    )

    output_file = os.path.join(os.path.dirname(__file__), 'output.html')
    sivo_app.to_html(output_file)
    print(f"Generated {output_file}")

if __name__ == "__main__":
    main()
