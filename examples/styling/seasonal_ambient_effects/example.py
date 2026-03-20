import os
from sivo import Sivo, ProjectConfig, ElementConfig

# Base directory for the output HTML
base_dir = os.path.dirname(__file__)

# Use a generic simple map from another example
svg_path = os.path.join(base_dir, "..", "01_hello_world", "sample.svg")

if not os.path.exists(svg_path):
    print(f"Warning: Ensure {svg_path} exists to run this example.")

seasons = ["spring", "summer", "fall", "winter"]

for season in seasons:
    print(f"Generating infographic with '{season}' ambient effect...")
    config = ProjectConfig(
        svg_file=svg_path,
        ambient_effect=season,
        title=f"{season.capitalize()} Ambient Effect",
        subtitle="SIVO Custom Ambient Effects",
        theme="dark" if season in ["summer", "winter"] else "light"
    )

    sivo_app = Sivo.from_config(config)

    sivo_app.map("house", tooltip=f"Enjoy the {season}!")

    output_path = os.path.join(base_dir, f"{season}_effect.html")
    sivo_app.to_html(output_path)
    print(f"Successfully generated {output_path}")
