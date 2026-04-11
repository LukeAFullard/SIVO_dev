# Footnotes Example

This example demonstrates how to use the SIVO framework to add footnotes to interactive SVG elements. Footnotes are helpful for adding context, data provenance, methodology notes, and disclaimers to specific data points.

## What is being shown
- An SVG map containing two interactive points.
- Mapping footnotes and their titles to SVG elements.
- Configuring a panel location so that the footnotes can be seen in an overlay.

## How it works
1. An SVG element containing points is generated and saved as `footnote_map.svg`.
2. The SIVO framework initializes an application from the `footnote_map.svg` using `Sivo.from_svg`.
3. To display the footnote content, we configure the initialization with `default_panel_position="overlay"`. (Without a panel position set to right, left, overlay, etc. footnotes will not appear).
4. Footnotes and footnote titles are mapped to elements `point1` and `point2` using the `sivo_app.map` method.

### Code Snippet
The following Python snippet demonstrates how the framework is configured and elements are mapped:

```python
# Initialize Sivo with a default panel position to display footnotes
sivo_app = Sivo.from_svg(svg_path, default_panel_position="overlay")

sivo_app.map(
    element_id="point1",
    tooltip="Red Data Point",
    footnote="This figure excludes data from Alaska and Hawaii due to reporting differences. Source: U.S. Census Bureau 2023.",
    footnote_title="Methodology Note"
)
```

## Running the Example
To run this example, execute the following command from the root directory:
```bash
PYTHONPATH=src python3 examples/advanced/footnotes/footnotes.py
```
This generates an `output.html` file that can be opened in any web browser.
