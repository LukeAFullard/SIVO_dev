# Exaggerated Trendlines

This example demonstrates how to create exaggerated trendlines using `map_trendline_chart`. It features large trendlines with dynamic labels ("Increasing", "Reducing", "Flat") and arrows to quickly draw attention to the specific trend of different chart components within a project map.

The `ProjectConfig` includes `default_panel_position="overlay"` so that when elements are clicked, they trigger the display of these line charts in an overlay above the view.

## Code Highlight

```python
    # 1. Increasing Trendline
    label_increasing = analyze_trend(data_increasing)
    app.map_trendline_chart(
        element_id="chart_increasing",
        title="Sales (Increasing)",
        data=data_increasing,
        trendline_type="linear",
        trendline_color="#10b981", # Green
        trendline_width=10,        # Exaggerated width
        trendline_arrow=True,
        trendline_arrow_size=30,   # Exaggerated arrow size
        trendline_label=label_increasing, # Dynamic label
        color="#a7f3d0",           # Light Green
        grid_margin=[60, 100, 40, 40] # Add right margin so label isn't cut off
    )
```

## Running the Example

Run from the root of the project with:

```bash
PYTHONPATH=src python3 examples/charts/exaggerated_trendlines/main.py
```

Then open `output.html` in your browser.
