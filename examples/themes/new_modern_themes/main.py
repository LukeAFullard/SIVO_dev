import os
from sivo import Sivo

def main():
    themes = ["monochrome", "ocean", "forest", "sunset", "pastel"]

    # We will use a standard template to demonstrate the themes
    # The gis_digital_twin_dashboard_2026 is a good choice as it has many stylized elements
    # We must resolve the absolute path to bypass the path traversal check in Sivo.from_svg.
    template_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../src/sivo/templates/16_10/gis_digital_twin_dashboard_2026.svg"))

    for theme in themes:
        print(f"Generating dashboard for theme: {theme}")

        # Initialize SIVO from template
        # Use default_panel_position="none" and specify panel_position where needed
        sivo_app = Sivo.from_svg(template_path, default_panel_position="none")

        # Map a simple interactive element to show panel_position works
        sivo_app.map(
            element_id="metric-iot-1",
            html="<h1>IoT Sensor 1</h1><p>Detailed metrics for IoT Sensor 1.</p>",
            panel_position="right"
        )

        sivo_app.map(
            element_id="metric-iot-2",
            html="<h1>IoT Sensor 2</h1><p>Detailed metrics for IoT Sensor 2.</p>",
            panel_position="overlay"
        )

        # Apply the specific theme
        sivo_app.apply_template_style(theme)

        # Generate the output HTML
        output_filename = f"output_{theme}.html"
        output_path = os.path.join(os.path.dirname(__file__), output_filename)
        sivo_app.to_html(output_path=output_path)
        print(f"Saved {output_path}")

if __name__ == "__main__":
    main()
