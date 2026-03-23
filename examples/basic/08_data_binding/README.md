# Basic: Data Binding

This example demonstrates how to automatically color and add data visualization to SVG elements by binding external datasets directly to specific SVG IDs in Sivo.

## What is being tested/demonstrated
* Providing structured dictionary data associating values to SVG element IDs.
* Using `sivo_app.bind_data()` to generate color gradients based on specific metric values ("sales").
* Automatic generation of tooltips by ECharts to show underlying data.

## Key Code

```python
# Provide a dataset mapping SVG IDs to numeric values
data = {
    "TX": {"sales": 15000},
    "CA": {"sales": 22000},
    "NY": {"sales": 8000},
    "WY": {"sales": 500}
}

# Bind data to SVG IDs with a color scale
sivo_app.bind_data(
    data=data,
    key="sales",                     # The metric to base the color on
    colors=["#e0f3db", "#43a2ca"],   # Gradient from min to max
    min_val=0,
    max_val=25000
)

# Optional: add a generic tooltip
for state in data.keys():
    sivo_app.map(element_id=state, tooltip=f"State: {state}")
```
