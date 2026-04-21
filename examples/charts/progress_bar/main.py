import os
from sivo import Sivo

def main():
    # Use the local sample.svg
    svg_path = os.path.join(os.path.dirname(__file__), "sample.svg")

    # Set default_panel_position to 'right' to ensure the HTML and progress bar render
    sivo_app = Sivo.from_svg(svg_path, title="Progress Bar Overlay", default_panel_position="right")

    sivo_app.map(
        "sun",
        tooltip="Fundraising Progress",
        progress_bar={
            "title": "Donations Collected",
            "progress": 75.5,
            "color": "#10b981" # Green
        },
        html="<p>Help us reach our final goal of $1,000,000!</p>",
        panel_position="right"
    )

    sivo_app.map(
        "house",
        tooltip="Construction Progress",
        progress_bar={
            "title": "Renovation Complete",
            "progress": 30.0,
            "color": "#f59e0b" # Orange
        },
        html="<p>Phase 1 of renovations are underway.</p>",
        panel_position="right"
    )

    output_path = os.path.join(os.path.dirname(__file__), "output.html")
    sivo_app.to_html(output_path)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    main()
