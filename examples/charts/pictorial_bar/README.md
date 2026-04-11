# Pictorial Bar Chart Example

This example demonstrates how to create a pictorial bar chart in SIVO. Pictorial bar charts represent data values using repeated custom shapes or images, providing an engaging way to visualize categorical data.

## What is being tested/shown

1. **SVG String Parsing:** Loading an SVG directly from a string using `Sivo.from_string()`.
2. **Interactive Elements:** Adding a click interaction to a native SVG circle element (`#forest_trigger`).
3. **Pictorial Bar Mapping:** Using `map_pictorial_bar_chart` to map a dataset to the circle element, rendering a chart where each bar is made up of repeated SVG path symbols (in this case, tree shapes).
4. **Custom SVG Path Symbols:** Using an SVG path definition (`path://...`) to define the custom tree shape.
5. **Panel Positioning:** Explicitly setting the `panel_position="right"` so that the chart appears in a side panel rather than as a tooltip or overlay.
6. **ECharts Customization:** Supplying `extra_options` to hide the axis lines, ticks, and split lines for a cleaner, infographic-like appearance.

## Code Highlights

- The tree symbol is defined as an SVG path string:
  ```python
  tree_path = 'path://M150 0 L75 200 L225 200 Z'
  ```

- Mapping the pictorial bar chart ensures `symbol_repeat=True` so that the custom path stacks based on the data value:
  ```python
  sivo_app.map_pictorial_bar_chart(
      element_id="forest_trigger",
      title="Forest Density",
      data=data,
      categories=categories,
      symbol=tree_path,
      symbol_repeat=True,
      symbol_size=[20, 20],
      panel_position="right",
      # ...
  )
  ```

## Running the Example

Execute the following command from the root of the repository:

```bash
PYTHONPATH=src python3 examples/charts/pictorial_bar/main.py
```

This will generate an `output.html` file in this directory that you can open in any modern web browser.
