# Odometer Animation Example

This example demonstrates how to use SIVO to animate native SVG text nodes as odometers. Odometers smoothly count up to a target number over a specified duration, supporting different formatting styles like currency or standard integer display.

## How it works

1.  **SVG Preparation**: The example defines an inline SVG containing two KPI boxes (`kpi_box1` and `kpi_box2`) and text nodes for the values (`revenue_val` and `users_val`). The text nodes are initialized to `0`.
2.  **Sivo Initialization**: The Sivo app is initialized from the SVG string. **Crucially, `render_mode="svg"` must be used** because the odometer feature works by manipulating the DOM of native SVG text nodes, which is not supported in the standard `canvas` rendering mode.
3.  **Mapping Odometers**: The `app.map()` function is used to attach the odometer behavior to the text elements using their IDs.
    *   `odometer_value`: The target value to count up to.
    *   `odometer_duration_ms`: The duration of the animation in milliseconds.
    *   `odometer_format`: The formatting style (`"currency"`, `"int"`, etc.).

## Key Code Snippets

```python
# Must use render_mode="svg" for odometers as it manipulates native SVG text nodes
sivo_app = Sivo.from_string(svg_content, render_mode="svg")

# Map odometer properties to the text nodes
sivo_app.map(
    element_id="revenue_val",
    odometer_value=124500.50,
    odometer_duration_ms=3000,
    odometer_format="currency"
)

sivo_app.map(
    element_id="users_val",
    odometer_value=8432,
    odometer_duration_ms=2500,
    odometer_format="int"
)
```

## Running the Example

Execute the script to generate the HTML output:

```bash
python examples/uncategorized/odometers/main.py
```

This will create an `odometers.html` file in the same directory. Open it in a web browser to see the numbers smoothly count up from 0 to their target values when the page loads.
