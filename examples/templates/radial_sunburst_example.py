import os
import sys

# Ensure sivo can be imported from the repo root
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'src')))

from sivo import Sivo

def main():
    # Initialize the infographic using the built-in template loader
    # The 'digital_first_glassmorphism' theme gives a highly sophisticated, translucent layered depth look
    app = Sivo.from_template("16_10/radial_concentric_burst", theme="digital_first_glassmorphism", title="Ecosystem Map")

    # Map the background to enable interaction or target it, letting the new transparent default take effect
    app.map("background")

    # Map data to the center hub
    app.map("text_hub", "CORE")
    app.map("radial-center-data", tooltip="Central Hub: The primary command node of the ecosystem.")

    # Map inner satellites
    inner_data = [
        ("A", "SYS A", "99.9%"),
        ("B", "SYS B", "98.5%"),
        ("C", "SYS C", "99.1%")
    ]
    for i, (key, title, metric) in enumerate(inner_data):
        app.map(f"text_sys_{key.lower()}", title)
        app.map(f"val_sys_{key.lower()}", metric)
        app.map(f"sat-inner-{i+1}-data",
                html=f"<h3>{title} Status</h3><p>Current Uptime: {metric}</p><p>All services are functioning normally within {title}.</p>",
                panel_position="right")

    # Map outer satellites
    outer_data = [
        ("1", "EXT 1", "Active"),
        ("2", "EXT 2", "Active"),
        ("3", "EXT 3", "Warning"),
        ("4", "EXT 4", "Active"),
        ("5", "EXT 5", "Active"),
        ("6", "EXT 6", "Offline"),
    ]
    for key, title, metric in outer_data:
        app.map(f"text_ext_{key}", title)
        app.map(f"val_ext_{key}", metric)

        # Configure the interaction to show more detail in a side panel
        app.map(f"sat-outer-{key}-data",
                markdown=f"## {title}\n**Status:** {metric}\n\nDetailed logs and monitoring data for the external node {title}. Notice the status state and check recent alerts.",
                panel_position="right")

    # Generate the output HTML bundle
    output_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'radial_sunburst_example_output.html'))
    app.to_html(output_path)
    print(f"Generated example HTML at: {output_path}")

if __name__ == "__main__":
    main()
