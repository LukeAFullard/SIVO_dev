# Loading Animations Showcase

This example demonstrates the usage of the **Loading Animations** feature in SIVO (`LoadingAction`). Loading animations provide visual feedback to users during simulated data processing, fetching, or other asynchronous operations.

In this example, multiple interactive cards are mapped to different built-in CSS loading animation styles. When a card is clicked, a loading animation overlay is shown for a specified duration, and upon completion, the original graphic is replaced with the defined `completion_html` and `completion_color`.

## What is being tested/shown:

*   **`sivo.map()` configuration for loading animations**: The mapping configures interactive cards with the `loading` dictionary parameter.
*   **Various visual styles**: Tests different available animation styles like `spinner`, `pulse`, `typewriter`, `shimmer`, `glitch`, `matrix`, etc.
*   **`trigger` option**: Demonstrates triggering an animation immediately on map load (`"trigger": "load"`) versus clicking an element (`"trigger": "click"`).
*   **`duration_ms`**: Controls how long the animation plays before completing.
*   **Completion state overrides**: Once the loading finishes, the `completion_html` replaces the default text content in the overlay, and `completion_color` is applied to the mapped SVG element to reflect success/status states.

## Relevant Code Snippets

```python
# Map a standard loading animation with click trigger
app.map("card-pulse", tooltip="Pulse Animation",
        loading={
            "trigger": "click",
            "duration_ms": 3000,
            "style": "pulse",
            "text": "Processing...",
            "completion_html": "<h2 style='margin:0; color:#3b82f6;'>$4.2M</h2><span style='font-size:12px; color:#64748b;'>Revenue</span>",
            "completion_color": "#dbeafe"
        })

# Map an "on load" animation
app.map("card-onload", tooltip="This triggers as soon as the map loads",
        loading={
            "trigger": "load",
            "duration_ms": 4000,
            "style": "typewriter",
            "text": "Welcome to SIVO...",
            "completion_html": "<h3 style='margin:0; color:#0f172a;'>System Ready</h3>"
        })
```