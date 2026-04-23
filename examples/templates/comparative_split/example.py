import os
from sivo import Sivo

def main():
    # Construct absolute path to the SVG template
    template_path = os.path.abspath(os.path.join(
        os.path.dirname(__file__),
        '..', '..', '..', 'src', 'sivo', 'templates', '16_10', 'comparative_split.svg'
    ))

    # Initialize Sivo with Neo-Brutalism theme
    app = Sivo.from_svg(template_path, theme="neo_brutalism", title="Comparative Split Example")

    # Map interactions and data

    # Title and Subtitle
    app.map("dash_title", tooltip="2026 Strategy vs Reality")
    app.map("dash_subtitle", tooltip="Evaluating Q1 performance against projections")

    # Panel A (Left)
    app.map("title_panel_a", tooltip="Projections")
    app.map("desc_panel_a", tooltip="Our aggressive growth strategy for Q1 2026.")

    # Map a line chart to Option A
    app.map_line_chart(
        element_id="chart_a",
        title="Projected Revenue",
        categories=["Jan", "Feb", "Mar"],
        data=[[10, 25, 45]]
    )

    # Map interactive compare to the left panel background as an interaction
    app.map("bg_panel_a", tooltip="Click to view full projection report", url="https://example.com/projections")

    # Panel B (Right)
    app.map("title_panel_b", tooltip="Reality")
    app.map("desc_panel_b", tooltip="Actual performance based on market shifts.")

    # Map a line chart to Option B
    app.map_line_chart(
        element_id="chart_b",
        title="Actual Revenue",
        categories=["Jan", "Feb", "Mar"],
        data=[[10, 15, 20]]
    )

    app.map("bg_panel_b", tooltip="Click to view reality report", url="https://example.com/reality")

    # Generate and save the HTML file
    output_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "comparative_split.html"))
    app.to_html(output_path)
    print(f"Interactive comparative split generated at: {output_path}")

if __name__ == "__main__":
    main()
