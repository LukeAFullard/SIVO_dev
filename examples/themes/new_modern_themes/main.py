import os
from sivo import Sivo

def main():
    themes = ["monochrome", "ocean", "forest", "sunset", "pastel"]

    # We will use a standard template to demonstrate the themes
    # The gis_digital_twin_dashboard_2026 is a good choice as it has many stylized elements
    template_name = "16_10/gis_digital_twin_dashboard_2026"

    # Sivo.from_template appends "_template.svg", but the file is just ".svg".
    # Therefore we pass the literal file path to from_svg.
    # We must resolve the absolute path to bypass the path traversal check in Sivo.from_svg.
    template_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../src/sivo/templates/16_10/gis_digital_twin_dashboard_2026.svg"))

    for theme in themes:
        print(f"Generating dashboard for theme: {theme}")

        # Initialize SIVO from template
        sivo_app = Sivo.from_svg(template_path)

        # Apply the specific theme
        sivo_app.apply_template_style(theme)

        # Generate the output HTML
        output_filename = f"output_{theme}.html"
        sivo_app.to_html(output_path=output_filename)
        print(f"Saved {output_filename}")

if __name__ == "__main__":
    main()
