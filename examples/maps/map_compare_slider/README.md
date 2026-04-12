# Map Compare Slider Example

This example demonstrates how to create a native before/after drag slider separating two SIVO canvases to compare changes over time or between datasets.

## Key Features Tested

- `to_html_compare(other_sivo, output_file)`: This method on the base `Sivo` instance generates an interactive HTML that renders both the base map and the provided `other_sivo` map with a drag slider.
- Use of multiple `Sivo.from_string()` instances to define independent SVGs and mappings for the left and right sides of the slider.
- Using `html` for mapped regions (instead of the deprecated `tooltip`) to display rich content in the panel.
- Setting `default_panel_position="overlay"` for both Sivo instances.

## Code Example

```python
sivo_left = Sivo.from_string(
    svg_left,
    title="Regional Growth Comparison",
    subtitle="Swipe to see changes from 2020 to 2024",
    default_panel_position="overlay"
)
sivo_left.map("region1", html="<h3>Region 1 - 2020</h3>", color="#cbd5e1")

sivo_right = Sivo.from_string(svg_right, default_panel_position="overlay")
sivo_right.map("region1", html="<h3>Region 1 - 2024</h3>", color="#10b981")

sivo_left.to_html_compare(sivo_right, output_file)
```
