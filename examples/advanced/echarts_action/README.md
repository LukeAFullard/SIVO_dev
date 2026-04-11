# ECharts Action Example

This example demonstrates how to attach interactive Apache ECharts (like Bar, Line, Pie, and Gauge charts) directly to native SVG elements using SIVO's `echarts_option` argument. By clicking on specific states on the map (Texas, California, New York, Wyoming), a side panel or tooltip opens to reveal a fully functional, interactive ECharts visualization.

## What is being shown
- Using `sivo_app.map(...)` with the `echarts_option` parameter to pass a complete ECharts configuration dictionary.
- Associating distinct chart types (Bar, Line, Pie, Gauge) with different interactive SVG elements (state maps).
- Injecting an `html` title along with an embedded ECharts instance.

## Code highlights
The key part of this example is defining standard ECharts configuration dictionaries and passing them to `sivo_app.map(element_id="...", echarts_option=...)`:

```python
    # 1. Bar Chart Option (TX)
    bar_chart_option = {
        "title": {"text": "Texas Regional Sales"},
        "tooltip": {},
        "xAxis": {"data": ["Austin", "Dallas", "Houston", "San Antonio"]},
        "yAxis": {},
        "series": [{
            "name": "Sales",
            "type": "bar",
            "data": [5000, 20000, 36000, 10000],
            "itemStyle": {"color": "#43a2ca"}
        }]
    }

    # Map the element using echarts_option
    sivo_app.map(
        element_id="TX",
        tooltip="View Regional Data (Bar)",
        html="<h3>Bar Chart</h3>",
        echarts_option=bar_chart_option,
        panel_position="overlay"
    )
```

## How to Run

1. Make sure your virtual environment is active.
2. Run the main script from the root directory:
   ```bash
   PYTHONPATH=src python3 examples/advanced/echarts_action/main.py
   ```
3. Open `examples/advanced/echarts_action/output.html` in your web browser.
4. Click on the different states (TX, CA, NY, WY) to see the corresponding ECharts embedded in the information panel.
