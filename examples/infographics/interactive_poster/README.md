# Interactive Poster Infographic

This example demonstrates how to create a tall, vertical "interactive poster" using SIVO. Unlike typical maps or dashboards, this layout mirrors a long-form scrolling infographic (often used in digital media reports), where various sections become interactive when clicked.

## Key Features Showcased

1. **Tall SVG Canvas**: The base SVG is a tall canvas (`viewBox="0 0 1000 2400"`) styled like a modern digital poster with a grid background and distinct sections.
2. **Scrolling Layout**: Custom CSS ensures the SVG container (`#chart-container`) handles the tall format gracefully by allowing vertical scrolling and a central alignment, mimicking a physical poster.
3. **Rich HTML Detail Panels**: Interactive elements open side panels containing HTML content (`html` mapping property), providing deep dives into the topic summarized in the poster section.
4. **Embedded ECharts**:
    - The "Short-Form Video" section uses a mapped line chart to show engagement trajectories.
    - The "Creator Economy" section uses a mapped pie chart to show revenue diversification.
5. **Embedded Media**: The "Audio Resurgence" section embeds a Spotify episode using the `social` mapping property.
6. **Image Gallery**: The "AI Co-Pilot" section uses the `gallery` property to display a sequence of images.

## Relevant Code Snippets

### Sivo Initialization without Bounding Coords
To allow the native SVG to size itself inside the container, we omit `bounding_coords`. We also set the default panel position to the right so interactions reveal the deep dives.

```python
sivo_app = Sivo.from_string(
    svg_content,
    title="The State of Digital Media",
    theme="light",
    panel_width="450px",
    default_panel_position="right",
    disable_zoom_controls=False
)
```

### Mapping Rich HTML Content and ECharts
Here we bind an ECharts line chart and descriptive HTML to the `section_video` group in the SVG.

```python
sivo_app.map(
    element_id="section_video",
    hover_color="#f8fafc",
    glow=True,
    html="""
    <h4>Deep Dive: Short-Form Video</h4>
    <h3>Engagement Trajectory</h3>
    <p>Short-form video has completely cannibalized traditional feed scrolling...</p>
    """,
    echarts_option={
        "tooltip": {"trigger": "axis"},
        "legend": {"data": ["TikTok", "Reels", "Shorts"]},
        # ... ECharts configuration ...
    }
)
```

### Mapping a Social Embed (Spotify)
```python
sivo_app.map(
    element_id="section_audio",
    hover_color="#f8fafc",
    glow=True,
    html="...",
    social={"provider": "website", "url": "https://open.spotify.com/embed/episode/...?utm_source=generator"}
)
```

### Mapping an Image Gallery
```python
sivo_app.map(
    element_id="section_ai",
    hover_color="#334155",
    glow=True,
    html="...",
    gallery=[
        "https://images.unsplash.com/photo-1682687982501-...",
        "https://images.unsplash.com/photo-1677442136019-...",
        "https://images.unsplash.com/photo-1682687220742-..."
    ]
)
```

## How to Run

Execute the main script to generate the HTML output:
```bash
PYTHONPATH=src python examples/infographics/interactive_poster/main.py
```
Open `poster.html` in your web browser.