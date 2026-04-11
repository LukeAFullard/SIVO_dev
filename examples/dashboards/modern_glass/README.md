# Modern Glass Dashboard Example

This example demonstrates how to build a highly stylized, multi-block "Modern Glass" (glassmorphism) dashboard using `SivoDashboard`.

The example showcases:
1. **Responsive CSS Grid Layout**: Using `set_grid_layout()` to define desktop and mobile views.
2. **Glassmorphism Styling**: Injecting custom CSS (`custom_js`) to apply dynamic gradient backgrounds, backdrop blur, and semi-transparent borders to dashboard grid items.
3. **Interactive Visualizations**: Mapping SVG components (like regions and metric boxes) to rich text tooltips and data payloads.
4. **Dynamic Side Panels**: Using `add_details_panel` and `add_metrics_panel` to display data based on the payloads associated with clicked shapes on the SIVO map.

## Code highlights

```python
# Custom CSS for Glassmorphism
custom_css_js = '''
<style>
    body {
        background: linear-gradient(135deg, #f6d365 0%, #fda085 100%);
    }
    .sivo-grid-item {
        background: rgba(255, 255, 255, 0.45);
        backdrop-filter: blur(12px);
        border-radius: 16px;
        border: 1px solid rgba(255, 255, 255, 0.18);
        box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
    }
</style>
'''
dashboard.to_html("output.html", custom_js=custom_css_js)
```

## Running the example

```bash
PYTHONPATH=src python3 examples/dashboards/modern_glass/main.py
```

This will generate an `output.html` file in this directory. Open it in a web browser to see the interactive, glass-styled dashboard.
