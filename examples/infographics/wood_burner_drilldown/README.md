# Wood Burner Drilldown Example

This example demonstrates how to create a multi-view interactive infographic using SIVO. It specifically shows:

1.  **Multiple Views**: How to bundle multiple distinct SVGs (`app_old` and `app_modern`) into a single HTML bundle.
2.  **View Transitions**: Using the `explode_to` property to transition (drill down) from one view to another when clicking an element.
3.  **HTML Overlays**: How to inject custom CSS animations (in this case, thick and light smoke) directly over target SVG elements using the `add_overlay` method.
4.  **Interactive Elements**: Mapping tooltips using `html` instead of the deprecated `markdown` and `tooltip` parameters.

### How it works
The `main.py` script starts by defining two large SVG strings: one representing an older, inefficient wood burner that produces thick smoke, and one representing a modern, clean-burning alternative.

Two `Sivo` applications are created:
```python
app_old = Sivo.from_string(...)
app_modern = Sivo.from_string(...)
```

It then injects the CSS animations over transparent target elements in the SVG:
```python
app_old.add_overlay(element_id="smoke_target_old", html=THICK_SMOKE_CSS)
app_modern.add_overlay(element_id="smoke_target_modern", html=LIGHT_SMOKE_CSS)
```

Interactive mappings are added to various parts of the SVGs using `app.map()`, notably utilizing the `explode_to` parameter to switch between the old and modern views when the respective buttons are clicked:
```python
app_old.map(
    element_id="switch_to_modern",
    html="<p>Click to upgrade to a modern wood-burner</p>",
    explode_to="modern_view",
    explode_duration_ms=800,
    ...
)
```

Finally, the `generate_echarts_html` function from `sivo.runtime.bundle_generator` is used to combine both configurations into a single `index.html` file.

### How to run

1. Ensure your `PYTHONPATH` includes the `src` directory.
2. Execute the `main.py` file:
   ```bash
   PYTHONPATH=src python3 examples/infographics/wood_burner_drilldown/main.py
   ```
3. Open the resulting `index.html` file in a browser.