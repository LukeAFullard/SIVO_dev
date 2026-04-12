# Proportional Symbol Map

This example demonstrates how to apply proportional symbols to an SVG map using SIVO.

It shows how to use the `apply_proportional_symbols` method to scale symbols dynamically based on a data mapping, positioning them accurately onto bounding boxes mapped with the `map` method.
The size of each symbol is dynamically scaled within the range specified by `min_size` and `max_size` based on the data values provided.

## Key Concepts

### Mapping Map Elements
To begin, you first need to explicitly map the relevant geographical areas or SVG objects using `sivo_app.map(...)`. This parses the elements and registers their bounding box coordinates.
Here, we replace the deprecated `tooltip` argument with `html` for any on-hover data, although it's not strictly necessary for the proportional symbols to render:

```python
sivo_app.map("sun", html="Building A (Budget: $500k)")
sivo_app.map("house", html="Building B (Budget: $250k)")
sivo_app.map("river", html="Building C (Budget: $1.2M)")
```

### Applying Proportional Symbols
After mapping the elements, we use the `apply_proportional_symbols` function. This overlays visual symbols based on a `data_map` dictionary mapping the element IDs to numeric values. You can define the minimum and maximum sizes, as well as customize the color:

```python
sivo_app.apply_proportional_symbols(
    data_map={
        "sun": 500,
        "house": 250,
        "river": 1200
    },
    min_size=10,
    max_size=50,
    color="rgba(56, 189, 248, 0.7)" # Light blue semi-transparent
)
```

By explicitly specifying a `default_panel_position` in the `Sivo.from_svg` initialization, you can optionally show an interactive side panel as well.
