# News Infographic: Election

This example demonstrates how to build a professional-grade election infographic using `Sivo.from_string`. It simulates a newspaper-style interactive graphic where clicking on map regions displays detailed demographic shifts and hourly vote counts using embedded ECharts.

## Features Showcased
- **Professional Styling**: Custom CSS is injected to replicate the look and feel of a major newspaper's election coverage.
- **Interactive Map Regions**: SVG paths representing election districts are mapped to interactive elements.
- **Embedded ECharts**: Bar charts and line graphs are embedded within the information panels to show vote share margins and hourly vote counts.
- **Custom HTML Overlays**: Rich HTML content provides editorial takeaways when regions are clicked.

## Key Code Snippets

### Setting the Default Panel Position
The info panel containing the ECharts and HTML content is set to appear on the right side of the screen when a map region is clicked:

```python
sivo_app = Sivo.from_string(
    svg_content,
    title="Election 2024 Final Tally",
    panel_width="450px",
    disable_zoom_controls=True,
    bounding_coords=[[0, 1414], [1000, 0]],
    default_panel_position="right"  # Ensure the panel appears on interaction
)
```

### Mapping Regions with Embedded Charts
Each map region is mapped using `sivo_app.map()`, combining rich HTML and ECharts configurations:

```python
sivo_app.map(
    element_id="region_north",
    tooltip="North (Cand. A)",
    color="#bfdbfe", hover_color="#93c5fd", glow=True,
    html="""
    <h3>North District</h3>
    <p>A narrow victory for Candidate A, driven entirely by high margins in the metropolitan center offsetting rural deficits.</p>
    """,
    echarts_option={
        "title": {"text": "Vote Share Margin", "textStyle": {"fontSize": 14, "fontFamily": "Helvetica Neue"}},
        # ... more ECharts options ...
    }
)
```

## Running the Example
To generate the interactive HTML file (`election_a4.html`), run:

```bash
PYTHONPATH=src python3 examples/infographics/news_infographic_election/main.py
```
