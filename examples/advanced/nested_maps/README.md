# Nested Maps Example

This example demonstrates how to create a "nested map" or drill-down effect in SIVO. By clicking on a specific region in the main SVG map, a secondary, detailed SVG map will open inside the side panel.

## What is being shown
- Initializing SIVO with a main map SVG.
- Reading a secondary "submap" SVG from disk.
- Using `map_nested_map_chart()` to bind the submap to an element (`regionA`) on the main map.
- Passing structured data to populate the visual map scale of the nested map.
- Adding hover styling to the interactive region.

## Relevant Code

The core of this example is reading the submap SVG as a string and using `map_nested_map_chart()` to embed it as an interactive ECharts map inside the panel when the target element (`regionA`) is clicked:

```python
# Read the submap SVG as a string so we can pass it as map_data
with open(os.path.join(os.path.dirname(__file__), "submap.svg"), "r") as f:
    submap_svg = f.read()

# Map the nested map chart to Region A
sivo_app.map_nested_map_chart(
    element_id="regionA",
    title="Region A Districts",
    map_name="regionA_map",
    map_data=submap_svg,
    data=[
        {"name": "district1", "value": 80},
        {"name": "district2", "value": 40},
        {"name": "district3", "value": 100}
    ],
    min_val=0,
    max_val=100,
    color=["#fee2e2", "#991b1b"], # Red scale
    tooltip="Click to view district breakdown",
    panel_position="right"
)
```

We also enable visual feedback for the clickable region in the main map:

```python
sivo_app.map(
    "regionA",
    hover_color="#cbd5e1",
    glow=True
)
```
