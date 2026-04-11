# SIVO Dashboards: Rich Media Integration

This example demonstrates how to integrate standalone third-party rich media embeds alongside an interactive SVG map using `SivoDashboard`.

## What is being shown
The example shows a three-column CSS Grid layout using `SivoDashboard`. Instead of putting everything in a single monolithic SVG, we assemble independent blocks.
1. **Interactive Map (`add_sivo_block`)**: A SIVO SVG map mapping event locations to HTML tooltip data. It uses `default_panel_position="none"` since we don't want SIVO's built-in sliding sidebar panel, but instead rely on our own grid layout.
2. **Details Panel (`add_details_panel`)**: A dedicated slot on the dashboard that listens to SIVO clicks and automatically renders the `html` content mapped to the clicked SVG element.
3. **Rich Media Block (`add_html_block`)**: A pure HTML block containing structural markup that can be used to load external widgets (e.g., Typeform, Calendly, Stripe Checkout, or Google Forms) inside an iframe.

## Steps Involved
1. Initialize a base Sivo map from an SVG string representing event locations. Set `default_panel_position="none"` because we use a custom dashboard grid.
2. Prepare a pure HTML string that represents our third-party rich media container (e.g., an iframe for a registration form).
3. Use Sivo's `map()` method to bind schedule details (`html`) to individual circles (`event_nyc`, `event_ldn`) on the SVG.
4. Construct a `SivoDashboard` and arrange the three distinct components using `add_sivo_block`, `add_details_panel`, and `add_html_block`.
5. Export the fully composed reactive dashboard using `dashboard.to_html()`.

## Key Code Snippets

### Suppressing Default Panels
Since we want our details rendered in the dashboard's dedicated slot rather than SIVO's built-in sliding sidebar, we specify `default_panel_position="none"`.
```python
sivo_map = Sivo.from_string(map_svg, default_panel_position="none")
```

### Building the Layout Blocks
We divide our grid into specialized sections.
```python
dashboard = SivoDashboard(title="Event Registration Portal")

# 1. The Interactive Map
dashboard.add_sivo_block("event_map", sivo_map)

# 2. The No-Code HTML Interactivity Panel
dashboard.add_details_panel("schedule", title="Event Schedule")

# 3. The Pure HTML Extensibility Block
dashboard.add_html_block("registration", registration_form_html)
```

## Running the Example
```bash
PYTHONPATH=src python3 examples/dashboards/rich_media_integration/main.py
```
This will generate `output.html` in this directory. Open it in a web browser to interact with the map, observe the details populating in the center panel, and see the placeholder for the rich media registration form on the right.
