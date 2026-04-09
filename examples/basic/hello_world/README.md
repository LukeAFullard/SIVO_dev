# Hello World

This example demonstrates the basic usage of SIVO. It shows how to initialize a SIVO application from an SVG file, map interactions to different elements, and export the result to an interactive HTML file.

## What is being tested/shown

1.  **Initialization**: Loading an SVG file using `Sivo.from_svg()`. We also enable search and set the default panel position to the right.
    ```python
    sivo_app = Sivo.from_svg(svg_path, enable_search=True, default_panel_position="right")
    ```
2.  **Mapping Interactions**: We map interactions to specific elements in the SVG by their `element_id`.
    *   The "sun" element gets a tooltip, an HTML side panel, a specific color, a hover color, and a glow effect.
    ```python
    sivo_app.map(
        element_id="sun",
        tooltip="The Sun",
        html="<h3>The Sun</h3><p>It is very bright and hot.</p>",
        color="gold",
        hover_color="yellow",
        glow=True
    )
    ```
    *   The "mountain1" and "house" elements get tooltips, specific colors, and hover colors.
3.  **Exporting**: The configured application is exported to a standalone HTML file.
    ```python
    sivo_app.to_html(output_path)
    ```

## Steps to run

1.  Navigate to the root directory of the repository.
2.  Run the script: `PYTHONPATH=src python examples/basic/hello_world/main.py`
3.  Open the generated `output.html` file in your browser.
4.  Interact with the "sun", "mountain1", and "house" elements to see the tooltips and side panels.
