# Folium Leaflet Embed Integration

This example demonstrates how to integrate rich, external mapping frameworks (like `folium` standard and timeline maps) into the interactive SIVO side panel via iframe embeds.

## What is being tested/shown
- Using Folium to generate standalone Leaflet HTML map exports representing map features.
- Sandboxing and embedding these generated interactive HTML maps directly within SIVO's sidebar using the `social` embedding property.
- Combining external web layers (`folium`) natively within vector base map (`Sivo`) dashboard panels.

## Code Snippets

```python
# We map 'France' to open the standard folium map in the sidebar using social embeds
sivo_app.map(
    element_id="France",
    tooltip="France - Click to view standard Folium Map",
    social={"provider": "website", "url": "folium_france.html"},
    color="#a6bddb",
    panel_position="right" # Embeds the Leaflet iframe in the right panel
)

# We map 'Germany' to open the folium timeline map in the sidebar
sivo_app.map(
    element_id="Germany",
    tooltip="Germany - Click to view Folium Timeline Map",
    social={"provider": "website", "url": "folium_germany_timeline.html"},
    color="#a6bddb",
    panel_position="right"
)
```
