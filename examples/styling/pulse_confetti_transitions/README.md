# Pulse & Confetti Transitions

This example demonstrates several advanced interactive features and styling capabilities in SIVO.

### What is being shown
1. **Multi-View Drill-Through (`SivoProject`)**: How to structure a dashboard that allows users to click an element in one view and transition to a completely different view seamlessly.
2. **Confetti Gamification**: How to reward user interactions with visual feedback (confetti).
3. **Pulse Proportional Symbols**: How to overlay animated, pulsing telemetry symbols on top of an SVG base map.

### Key Code Snippets

#### 1. Multi-View Drill-Through
To navigate between multiple dashboards or views, `drill_through` mapping is used.
```python
# Map Drill Through to a new view ID.
sivo_app.map("region_a", drill_through="region_a_details", drill_transition="zoom")
```

The multiple views are then managed using a `SivoProject`:
```python
# Create a SivoProject, specifying the initial view ID
project = SivoProject("default_view")

# Add the views to the project
project.add_view("default_view", sivo_app)
project.add_view("region_a_details", sivo_app2)

# Generate the standalone HTML file encompassing all views
project.to_html(output_path=output_path)
```

#### 2. Confetti Gamification
The `confetti` keyword argument can be passed to the `map` function to specify that clicking an element should trigger confetti.
```python
# Map Confetti Gamification. When "region_b" is clicked, it will trigger a confetti animation.
sivo_app.map("region_b", confetti={"particle_count": 200, "spread": 90}, tooltip="Goal Reached!")
```

#### 3. Pulse Markers
You can apply proportional symbols that pulse (to indicate live data or alerts) using the `apply_proportional_symbols` function with `is_pulse=True`.
```python
live_data = {
    "node_1": 100,
    "node_2": {"value": 50, "color": "#3b82f6"}, # Blue marker
    "node_3": {"value": 75, "color": "#10b981"}  # Green marker
}

sivo_app.apply_proportional_symbols(
    live_data,
    min_size=15,
    max_size=30,
    color="#ef4444",
    is_pulse=True
)
```
