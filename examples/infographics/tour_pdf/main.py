import os
from sivo import Sivo, ProjectConfig
from sivo.core.config import TourStepConfig

SVG_FILE = os.path.join(os.path.dirname(__file__), 'bg.svg')

with open(SVG_FILE, 'w') as f:
    f.write("""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 600">
    <rect id="rect1" x="0" y="0" width="400" height="300" fill="#f0f0f0"/>
    <rect id="rect2" x="400" y="0" width="400" height="300" fill="#e0e0e0"/>
    <rect id="rect3" x="0" y="300" width="400" height="300" fill="#d0d0d0"/>
    <rect id="rect4" x="400" y="300" width="400" height="300" fill="#c0c0c0"/>
    <text x="200" y="150" text-anchor="middle">Step 1: Introduction</text>
    <text x="600" y="150" text-anchor="middle">Step 2: Analysis</text>
    <text x="200" y="450" text-anchor="middle">Step 3: Details</text>
    <text x="600" y="450" text-anchor="middle">Step 4: Conclusion</text>
</svg>""")

config = ProjectConfig(
    svg_file=SVG_FILE,
    title="Interactive Guided Tour to PDF Export Demo",
    subtitle="Walk through the map and download a PDF presentation deck offline",
    theme="light",
    default_panel_position="none"
)

sivo_app = Sivo.from_config(config)

tour_steps = [
    dict(
        content="<h3>Introduction</h3><p>Welcome to the SIVO Tour to PDF demo. Click 'Download PDF' below to export the whole tour.</p>",
        zoom_to="rect1",
        zoom_level=2.5
    ),
    dict(
        content="<h3>Data Analysis</h3><p>This slide highlights our new findings. Notice how the map dynamically zoomed to focus on this area.</p>",
        zoom_to="rect2",
        zoom_level=3.0
    ),
    dict(
        content="<h3>Deep Dive</h3><p>Here we can explore further details of the graphic and include any extra narrative context.</p>",
        zoom_to="rect3",
        zoom_level=2.5
    ),
    dict(
        content="<h3>Conclusion</h3><p>We've reached the end of the tour. Now go ahead and click 'Download PDF' to generate the deck!</p>",
        zoom_to="rect4",
        zoom_level=2.0
    )
]

# We bind the tour and show the tour UI container
sivo_app.bind_tour(tour_steps)

output_path = os.path.join(os.path.dirname(__file__), 'output.html')
sivo_app.to_html(output_path)
print(f"Generated {output_path}")
