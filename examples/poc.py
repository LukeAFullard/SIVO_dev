import os
import sys

# Ensure SIVO is importable from src
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from sivo.core.infographic import Infographic

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
    sivo_instance = Infographic.from_string(sample_svg)

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
        html="<h3>Central Fountain</h3><p>A nice place to relax.</p>",
        tooltip="Relaxation Zone",
        color="#ccccff" # Light blue
    )

    # Note: 'pathway' has no custom mapping, defaults will apply

    output_path = os.path.join(os.path.dirname(__file__), "output.html")
    print(f"Exporting to {output_path}...")
    sivo_instance.to_echarts_html(output_path)
    print("Done! Open examples/output.html in your browser.")

if __name__ == "__main__":
    run()
