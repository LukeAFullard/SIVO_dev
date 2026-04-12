# SIVO Tour to PDF Export Demo

This example demonstrates how to create an interactive guided tour using SIVO, which users can navigate through and subsequently download as a PDF presentation deck offline.

## What this example shows

- **Guided Tour Creation**: Binding a sequence of steps to specific elements within an SVG map, with custom zoom levels.
- **HTML Content in Tour Steps**: Formatting the tour text using HTML tags (e.g., `<h3>` for headers, `<p>` for paragraphs) within the `content` property of `TourStepConfig`.
- **Tour to PDF Generation**: Showing the built-in capability to let users download the entire SIVO tour as a PDF by interacting with the tour UI.
- **Dynamic Bounding Boxes**: Demonstrating how the map automatically zooms and centers on the targeted native SVG elements (like `rect1`, `rect2`) as the user moves from step to step.

## Relevant Code

The core of this example is the usage of the `bind_tour` method in `Sivo`:

```python
from sivo import Sivo, ProjectConfig
from sivo.core.config import TourStepConfig

# Define the tour sequence and map it to specific SVG elements
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
    # ... more steps
]

# Initialize Sivo configuration
config = ProjectConfig(
    svg_file=SVG_FILE,
    title="Interactive Guided Tour to PDF Export Demo",
    default_panel_position="none"
)

sivo_app = Sivo.from_config(config)

# Bind the configured tour steps
sivo_app.bind_tour(tour_steps)
```

## Running the Example

To execute the example and generate the `output.html` file, run:

```bash
PYTHONPATH=src python3 examples/infographics/tour_pdf/main.py
```
