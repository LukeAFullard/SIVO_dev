# SIVO Drill-Through Example

This example demonstrates how to map a `drill_through` action onto an SVG element in SIVO.

## What is being shown
- Creating an SVG string inline and passing it to SIVO using `Sivo.from_string`.
- Using `sivo_app.map()` to attach a `drill_through` parameter. When the mapped element is clicked, the application will navigate directly to the provided URL (in this case, `https://example.com`) without opening a new tab or rendering a side panel.

## Key Code Snippets

```python
# Map the button to drill-through to a new URL
sivo_app.map(
    element_id="button_dashboard",
    tooltip="Navigates to example.com in same tab",
    drill_through="https://example.com"
)
```

## Running the example
To run the example and generate the HTML output:
```bash
python drill_through.py
```
Open the generated `drill_through_example.html` in your browser. Hover over the green button to see the tooltip, and click it to navigate to example.com.
