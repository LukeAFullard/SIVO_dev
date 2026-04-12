# Scrollytelling Infographic Example

This example demonstrates how to create a "scrollytelling" interactive experience using SIVO. In a scrollytelling interface, the primary graphic stays fixed on the screen while the user scrolls through narrative text alongside it. The act of scrolling triggers dynamic visual changes in the graphic, such as zooming, panning, and highlighting elements.

## What is being tested/shown

1. **`bind_scrollytelling(steps)`**: The core method used to bind an array of step configurations to the `Sivo` application. It anchors the layout to a scrolling text column.
2. **Step Configurations**:
   - `content`: The HTML content (text, headers, etc.) shown for that particular scrollytelling step.
   - `zoom_to`: The target SVG element ID to zoom to when the step is reached.
   - `zoom_level`: Controls how closely the camera zooms in on the target.
   - `colors`: A dictionary that maps element IDs to specific colors, allowing us to highlight different hubs dynamically as the user reads about them.
   - `show_tooltips`: Automatically displays the corresponding information panel (or tooltip) for elements during a step.
3. **Information Mapping**: The use of `html` arguments in `sivo_app.map()` (e.g., `sivo_app.map("section1", html="...")`) to provide the interactive content that is revealed. Since `panel_position` defaults to `"none"` in newer SIVO versions, this example explicitly passes `default_panel_position="right"` in `Sivo.from_string()` so the mapped HTML appears in a side panel.

## How it works

1. We define a simple SVG containing three network hubs: a "Data Center" (rectangle), "Logistics" (circle), and "HQ" (path).
2. We initialize the application with `Sivo.from_string()` and define our narrative flow in a list of `steps`.
3. As the user scrolls down reading about each hub (e.g., "The Data Center"), the view automatically pans to `section1`, highlights it in blue, and fades the others out.
4. When `main.py` is executed, SIVO bundles the static narrative sequence along with the vector graphics into a standalone `scrollytelling.html` file.

## Running the example

Execute the script from the root of the repository:

```bash
PYTHONPATH=src python3 examples/infographics/scrollytelling/main.py
```

This will generate `scrollytelling.html` in the same directory, which you can open in your browser to view the interactive experience.
