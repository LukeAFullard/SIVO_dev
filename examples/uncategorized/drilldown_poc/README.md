# SIVO Drill-Down Example

This example demonstrates how to create a multi-level SVG infographic using the `drill_to` feature in SIVO.

## What is being shown
- Initializing SIVO from an inline SVG string that represents a high-level view (e.g., a campus map).
- Mapping an interactive element (`buildingA`) with the `drill_to` parameter pointing to a secondary SVG file (`floor1.svg`).
- When a user clicks on the mapped element, SIVO will transition and load the linked SVG into the view, allowing for a "drill-down" experience.

## Key Code Snippets

```python
# Drill-down interaction on Building A
sivo_instance.map(
    "buildingA",
    html="<h3>Building A</h3><p>Main Administrative Building.</p><p>Click to view Floor 1 plan.</p>",
    tooltip="Main Admin",
    color="#ffcccc", # Light red
    drill_to="floor1.svg"
)
```

## Running the example
Because the `drill_to` feature fetches external files, this example must be served via a local HTTP server rather than opening the HTML file directly in the browser via a `file://` URL.

1. Generate the HTML output:
```bash
python drilldown_poc.py
```

2. Start a local HTTP server in the directory containing the files:
```bash
python -m http.server 8000
```

3. Open your browser and navigate to:
```
http://localhost:8000/drilldown_output.html
```

Clicking on "Building A" will trigger the drill-down animation and load the `floor1.svg` view.
