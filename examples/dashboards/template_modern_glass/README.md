# Modern Glass Dashboard Layout

This example demonstrates how to create a sleek, "Glassmorphism" styled dashboard using `SivoDashboard` and custom CSS injection.

Historically, SIVO relied on pre-built HTML templates (like `modern_glass.html`). With the shift to the modular **CSS Grid Builder** (`set_grid_layout()`), developers now have complete control over dashboard styling without relying on hidden template files.

## What is being shown?

1.  **CSS Grid Layout Engine**: The dashboard is constructed using `dashboard.set_grid_layout()`, dynamically placing components (a header, a main interactive map, and two side panels).
2.  **Custom CSS Injection**: We inject a custom `<style>` block via the `custom_js` parameter during `dashboard.to_html()`. This targets the `.sivo-grid-block` class to apply `backdrop-filter: blur()`, translucent backgrounds, and drop shadows, creating the frosted glass effect.
3.  **No-Panel Default**: By default, SIVO's internal map sidebars (`panel_position`) are disabled. Instead, the interactive map delegates data to external `add_details_panel` and `add_metrics_panel` blocks positioned in the CSS Grid.
4.  **Payload Extraction**: The `add_metrics_panel` automatically extracts `revenue`, `growth`, and `active_users` from the `callback_payload` whenever a region is clicked on the map.

## Relevant Code

The core of the glass effect is applied here in `main.py`:

```python
custom_js = '''
<style>
    /* Gradient body background */
    body {
        background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
    }

    /* Target all SIVO blocks to apply glassmorphism */
    .sivo-grid-block {
        background: rgba(255, 255, 255, 0.1) !important;
        backdrop-filter: blur(10px);
        -webkit-backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.2) !important;
        border-radius: 16px !important;
        box-shadow: 0 4px 30px rgba(0, 0, 0, 0.1) !important;
        color: white !important;
    }
</style>
'''
dashboard.to_html("output.html", custom_js=custom_js)
```

## How to run

1. Ensure dependencies are installed.
2. Run the script:

```bash
PYTHONPATH=src python3 examples/dashboards/template_modern_glass/main.py
```

3. Open the generated `output.html` in your web browser. Click the colored regions on the left graphic to watch the sidebars update dynamically.
