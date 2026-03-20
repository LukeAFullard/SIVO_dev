import os
import sys

# Ensure SIVO is importable from src
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from sivo import Sivo

# Sample SVG mimicking a minimal campus or office layout
sample_svg = """<?xml version="1.0" encoding="UTF-8"?>
<svg viewBox="0 0 500 500" xmlns="http://www.w3.org/2000/svg">
  <rect id="buildingA" x="50" y="50" width="150" height="150" fill="#cccccc" stroke="#333333" stroke-width="2"/>
  <rect id="buildingB" x="250" y="50" width="200" height="100" fill="#cccccc" stroke="#333333" stroke-width="2"/>
  <circle id="fountain" cx="250" cy="300" r="40" fill="#aaccff" stroke="#333333" stroke-width="2"/>
  <path id="pathway" d="M 125 200 L 125 300 L 210 300" fill="none" stroke="#666666" stroke-width="10"/>
</svg>
"""

def run():
    print("Initializing SIVO with sample SVG...")
    # Initialize from a string (is_file=False)
    sivo_instance = Sivo.from_string(sample_svg)

    # Map elements to tooltips and HTML
    print("Mapping interactions...")
    sivo_instance.map(
        "buildingA",
        html="<h3>Building A</h3><p>Main Administrative Building.</p><p>Capacity: 500</p>",
        tooltip="Main Admin",
        color="#ffcccc" # Light red
    )

    sivo_instance.map(
        "buildingB",
        html="<h3>Building B</h3><p>Engineering & Sciences.</p><ul><li>Labs</li><li>Classrooms</li></ul>",
        tooltip="Engineering Block",
        color="#ccffcc" # Light green
    )

    sivo_instance.map(
        "fountain",
        html="""
        <style>
          h3 { color: darkblue; }
          .fountain-desc { border: 1px solid blue; padding: 5px; }
        </style>
        <h3>Central Fountain</h3>
        <p class="fountain-desc">A nice place to relax. Note this CSS does not bleed out due to Shadow DOM!</p>
        """,
        tooltip="Relaxation Zone",
        color="#ccccff", # Light blue
        hover_color="#aaaaff",
        border_width=3,
        border_color="#0000ff",
        glow=True
    )

    # Note: 'pathway' has no custom mapping, defaults will apply

    output_path = os.path.join(os.path.dirname(__file__), "output.html")
    print(f"Exporting HTML to {output_path}...")
    sivo_instance.to_html(output_path)

    metadata_path = os.path.join(os.path.dirname(__file__), "metadata.json")
    print(f"Exporting Metadata to {metadata_path}...")
    sivo_instance.export_metadata(metadata_path)

    print("Done! Open examples/output.html in your browser.")
    print("Check examples/metadata.json for the extracted SVG metadata.")

if __name__ == "__main__":
    run()
