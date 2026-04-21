# Analytics and Data Example

This example demonstrates how to integrate data analytics and live data fetching into a Sivo application. It showcases tracking interactions with elements using an analytics provider and retrieving live data via a public API when elements are clicked.

## What is Being Tested/Shown

- **Google Analytics Integration**: Mapping an element to trigger a Google Analytics event upon interaction.
- **Data Source Fetching**: Mapping an element to fetch data from an external API (simulated here with JSONPlaceholder).
- **Interactive UI Panel**: Setting `panel_position="right"` so that when elements are clicked, relevant content (such as custom HTML or fetched API data) displays in an interactive sliding side panel rather than doing nothing, as the default position is `"none"`.

## Relevant Code Snippets

```python
# Add Google Analytics event to box1
app.map(
    "box1",
    tooltip="Click to track event",
    html="<h3>Google Analytics</h3><p>Clicking this fires a Google Analytics event (if gtag is loaded).</p>",
    panel_position="right",
    analytics={
        "provider": "google_analytics",
        "event_name": "clicked_box1",
        "payload": {"source": "sivo_demo"}
    }
)

# Add a public API fetch to circle1 (e.g., retrieving a public JSON file or sheet proxy)
app.map(
    "circle1",
    tooltip="Click to fetch live data",
    panel_position="right",
    datasource={
        "provider": "google_sheets",
        "api_endpoint": "https://jsonplaceholder.typicode.com/users/1"
    }
)
```

By explicitly setting `panel_position="right"`, we ensure that the HTML content or fetched data has a dedicated space to be rendered visibly to the user.
