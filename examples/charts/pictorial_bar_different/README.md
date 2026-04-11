# Alternative Pictorial Bar Chart Example

This example demonstrates how to create a pictorial bar chart in SIVO using standard built-in symbols. Instead of a custom path, this uses the built-in `rect` symbol to mimic a stack of building blocks for city data.

## What is being tested/shown

1. **SVG String Parsing:** Loading a basic layout containing a rounded rectangle trigger from a string.
2. **Interactive Triggers:** Assigning an interactive `map_pictorial_bar_chart` event to an SVG rectangle (`#city_trigger`).
3. **Built-in Symbols:** Using the standard ECharts symbol `"rect"` rather than a custom `path://` to create the stacked blocks.
4. **Symbol Sizing:** Adjusting the `symbol_size=[30, 10]` parameter to make wide, short blocks that visually resemble stories of a building or a stack of cards.
5. **Panel Settings:** Setting `panel_position="right"` so the pictorial chart displays in the side panel when the user clicks the trigger.

## Code Highlights

- The chart is mapped using the basic `"rect"` symbol and `symbol_size`:
  ```python
  sivo_app.map_pictorial_bar_chart(
      element_id="city_trigger",
      title="City Skyscraper Count",
      data=data,
      categories=categories,
      symbol="rect",
      symbol_repeat=True,
      symbol_size=[30, 10], # 30px wide, 10px tall blocks
      color="#1f77b4",
      panel_position="right",
      # ...
  )
  ```

## Running the Example

Execute the following command from the root of the repository:

```bash
PYTHONPATH=src python3 examples/charts/pictorial_bar_different/main.py
```

This will generate an `output.html` file in this directory that you can open in any modern web browser.
