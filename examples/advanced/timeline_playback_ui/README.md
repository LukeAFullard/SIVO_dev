# Native Timeline Playback UI

## Purpose
This example demonstrates how to use SIVO to programmatically control the native ECharts timeline component and bind dynamic time-series data to native SVG elements. The goal is to animate the visualization over time, providing playback controls (play/pause) and temporal navigation across an interactive SVG "map" or chart.

## What is being tested
1. **SVG Integration**: Loading a raw SVG string defining multiple visual shapes (`<rect>` nodes).
2. **Timeline Binding**: Attaching temporal metrics (data organized by year) to specific SVG elements using the `bind_timeline` method.
3. **Timeline Playback**: Testing autoplay functionality, loop behavior, playback interval speed, and UI control positioning.
4. **Color Scaling**: Automatically mapping sequential data ranges to an interpolated color scale across the specific SVG blocks over time.
5. **Configuration Options**: Ensuring all variables required for advanced timeline tuning (symbol styles, sizes, and layout anchors) correctly influence the rendered HTML structure.

## Code highlights

### 1. Preparing Timeline Data
Data is formatted hierarchically by `{ "TimeStep": { "ElementID": { "DataKey": Value } } }`.
```python
timeline_data = {
    "2020": {
        "block_a": {"metric": 10},
        "block_b": {"metric": 20}
    },
    # ... further years ...
}
```

### 2. Binding and Animating
The `bind_timeline` method handles binding data metrics to the map elements, automatically interpolating colors based on numeric boundaries.
```python
app.bind_timeline(
    data=timeline_data,
    key="metric",
    colors=["#bae6fd", "#0284c7"], # Color gradient scale
    min_val=0,
    max_val=100,
    auto_play=True,
    play_interval=1500, # Duration per step in ms
    show_play_btn=True,
    loop=True,
    control_position="left",
    symbol="diamond",
    symbol_size=16,
    bottom=40
)
```

## How to run
Run the script from the root repository directory using:
```bash
PYTHONPATH=src python examples/advanced/timeline_playback_ui/main.py
```
This generates an `output.html` file inside this directory, which you can open in a web browser to view the interactive timeline sequence.
