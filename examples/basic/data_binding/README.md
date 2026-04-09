# Data Binding Example

This example demonstrates how to dynamically bind quantitative data to SVG elements using SIVO.

It shows how to associate numeric values with specific SVG IDs and apply a color scale gradient automatically.

## Purpose

The purpose of this example is to show how to create data-driven visualizations (like choropleth maps) by feeding a dataset into a base SVG template, without needing to manually define colors for every single element.

## Key Code Components

1. **Initialize SIVO**:
   We start with a base SVG map containing elements with IDs matching our dataset keys (e.g., "TX", "CA").
   ```python
   sivo_app = Sivo.from_svg(svg_path)
   ```

2. **Define the Dataset**:
   We provide a dictionary mapping element IDs to their corresponding data values.
   ```python
   data = {
       "TX": {"sales": 15000},
       "CA": {"sales": 22000},
       "NY": {"sales": 8000},
       "WY": {"sales": 500}
   }
   ```

3. **Bind Data and Apply Color Scale**:
   We use `bind_data()` to connect the dataset to the SVG. We specify the `key` to look for within the data dictionary ("sales"), define a gradient using `colors`, and set the `min_val` and `max_val` for the scale. SIVO will automatically interpolate colors based on the data values and apply them to the corresponding SVG elements.
   ```python
   sivo_app.bind_data(
       data=data,
       key="sales",                     # The metric to base the color on
       colors=["#e0f3db", "#43a2ca"],   # Gradient from min to max
       min_val=0,
       max_val=25000
   )
   ```

4. **Add Tooltips (Optional)**:
   We can still use `map()` to add tooltips. When `bind_data()` is used, ECharts automatically appends the data value (e.g., "sales: {value}") to the tooltip.
   ```python
   for state in data.keys():
       sivo_app.map(element_id=state, tooltip=f"State: {state}")
   ```

5. **Export**:
   Finally, we export the result to an HTML file.
   ```python
   sivo_app.to_html(output_path)
   ```

## How to Run

1. Ensure SIVO dependencies are installed.
2. Run the script: `PYTHONPATH=src python examples/basic/data_binding/main.py`
3. Open `output.html` in your web browser.
4. Observe the varying colors of the states based on their "sales" values, and hover over them to see the tooltips.