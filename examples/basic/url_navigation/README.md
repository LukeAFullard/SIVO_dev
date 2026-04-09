# URL Navigation

This example demonstrates how to configure SIVO to navigate to external URLs when SVG elements are clicked.

## What is being tested/shown

1.  **Initialization**: Loading an SVG file using `Sivo.from_svg()`.
    ```python
    sivo_app = Sivo.from_svg(svg_path)
    ```
2.  **Mapping Interactions to URLs**: We map interactions to specific elements using their `element_id` and provide a `url` parameter. When the element is clicked, the browser will navigate to this URL.
    *   Clicking the "sun" element navigates to the Wikipedia page for the Sun. It also has a tooltip, a hover color, and a glow effect.
    ```python
    sivo_app.map(
        element_id="sun",
        tooltip="Click to search about the Sun",
        url="https://en.wikipedia.org/wiki/Sun",
        hover_color="yellow",
        glow=True
    )
    ```
    *   Clicking the "mountain1" element navigates to the Wikipedia page for Mountain.
    ```python
    sivo_app.map(
        element_id="mountain1",
        tooltip="Click to search about Mountains",
        url="https://en.wikipedia.org/wiki/Mountain",
        hover_color="#c0c0c0"
    )
    ```
3.  **Exporting**: The configured application is exported to a standalone HTML file.
    ```python
    sivo_app.to_html(output_path)
    ```

## Steps to run

1.  Navigate to the root directory of the repository.
2.  Run the script: `PYTHONPATH=src python examples/basic/url_navigation/main.py`
3.  Open the generated `output.html` file in your browser.
4.  Click on the "sun" or "mountain1" elements to see the URL navigation in action.
