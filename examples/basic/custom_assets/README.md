# Custom Assets Example

This example demonstrates how to inject custom CSS styling and custom JavaScript into a SIVO interactive map.

## What is being shown?

By default, SIVO relies on its internal styling and logic to present SVGs via ECharts. However, there are scenarios where you want to add your own CSS (for instance, to style custom HTML tooltips or side panels) or run your own JavaScript functions once the map has loaded.

The `to_html()` method allows injecting a `custom_css` block and a `custom_js` block directly into the output bundle.

## Key Code Snippets

### 1. Mapping a custom HTML Tooltip
When you provide raw HTML to the `html` parameter in `sivo_app.map()`, you can include inline `<style>` tags. Because SIVO renders HTML mapped content inside a secure **Shadow DOM**, standard global CSS classes won't automatically style it. Injecting the styles directly into the payload ensures they penetrate the Shadow DOM.

```python
html_payload = \"\"\"
<style>
    /* This style block will be safely injected inside the Shadow DOM */
    .custom-tooltip {
        background-color: #ff0055 !important;
        color: #fff !important;
        padding: 30px !important;
        border-radius: 20px !important;
        box-shadow: 0 10px 20px rgba(0,0,0,0.5) !important;
        font-size: 24px !important;
        text-align: center !important;
    }
    .custom-tooltip h3 {
        margin-top: 0 !important;
        color: #ffff00 !important;
        font-size: 32px !important;
        text-transform: uppercase !important;
    }
</style>
<div class='custom-tooltip'><h3>The Custom Sun</h3><p>Styled with VERY custom CSS to make it obvious!</p></div>
\"\"\"

sivo_app.map(
    element_id="sun",
    tooltip="The Custom Sun",
    html=html_payload,
    panel_position="overlay" # Explicitly show the HTML inside an overlay panel
)
```

### 2. Defining Custom CSS and JS
You can still define standard CSS strings and JavaScript strings in Python. This CSS will be injected into the main document (e.g. to style the overall body or outer containers).

```python
custom_css = """
    /* Main document custom CSS */
    body {
        /* Example of styling the main window */
    }
"""

custom_js = """
    console.log('Hello from custom injected JS!');
"""
```

### 3. Injecting into `to_html`
Pass the defined strings to the `to_html` method. SIVO's Jinja2 bundler will safely place these within `<style>` and `<script>` blocks in the final output file.

```python
sivo_app.to_html(output_path, custom_css=custom_css, custom_js=custom_js)
```

## Running the example

Run this example from the root directory of the repository:

```bash
PYTHONPATH=src python examples/basic/custom_assets/main.py
```

Then, open `examples/basic/custom_assets/output.html` in your web browser. When you click the sun element, the custom styled tooltip will appear. You will also see the message in your browser's developer console.