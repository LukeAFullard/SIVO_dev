# 08 Data Binding

This example demonstrates how to bind external data to SVG elements and automatically color them based on their value using a color scale gradient.

### Key Code

```python
data = {
    "TX": {"sales": 15000},
    "CA": {"sales": 22000}
}

# Bind data to SVG IDs with a color scale
sivo_app.bind_data(
    data=data,
    key="sales",                     # The metric to base the color on
    colors=["#e0f3db", "#43a2ca"],   # Gradient from min to max
    min_val=0,
    max_val=25000
)
```
