# Timeline Playback Ui

## Description
1. Provide a simple static SVG string representing a few blocks 2. Initialize SIVO 3. Create temporal data to drive the map The structure is: { "TimeStep": { "ElementID": { "DataKey": Value } } } 4. Bind the timeline to the UI We apply custom Timeline UI styling, enabling the play button, looping, and setting custom sizing 5. Output to HTML

## Relevant Code
```python
    app = Sivo.from_string(svg_data, title="Native Timeline Playback UI", subtitle="Demonstrating programmatic control over the ECharts timeline component.")
    app.bind_timeline(
        data=timeline_data,
        key="metric",
        colors=["#bae6fd", "#0284c7"], # Light blue to dark blue gradient
        min_val=0,
        max_val=100,
        auto_play=True,
        play_interval=1500, # 1.5 seconds per step
        show_play_btn=True, # Show the native play/pause button
        loop=True,          # Loop continuously
        control_position="left", # Position controls on the left side of the axis
        symbol="diamond",   # Change the step symbol to a diamond
        symbol_size=16,     # Increase symbol size
        bottom=40           # Lift the timeline up slightly from the bottom edge
    )
    app.to_html(output_path)
```
