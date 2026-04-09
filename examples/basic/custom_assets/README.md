# Custom Assets Example

This example demonstrates how to inject custom CSS styling and custom JavaScript into a SIVO interactive map.

## What is being shown?

By default, SIVO relies on its internal styling and logic to present SVGs via ECharts. However, there are scenarios where you want to add your own CSS (for instance, to style custom HTML tooltips or side panels) or run your own JavaScript functions once the map has loaded.

The `to_html()` method allows injecting a `custom_css` block and a `custom_js` block directly into the output bundle.

## Key Code Snippets

### 1. Mapping a custom HTML Tooltip
When you provide raw HTML to the `html` parameter in `sivo_app.map()`, you can include specific classes (e.g., `custom-tooltip`) that aren't styled by default.

```python
sivo_app.map(
    element_id="sun",
    tooltip="The Custom Sun",
    html="<div class='custom-tooltip'><h3>The Custom Sun</h3><p>Styled with custom CSS!</p></div>"
)
```

### 2. Defining Custom CSS and JS
You define standard CSS strings and JavaScript strings in Python.

```python
custom_css = """
    .custom-tooltip {
        background-color: #333;
        color: #fff;
        padding: 10px;
        border-radius: 8px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.3);
    }
    .custom-tooltip h3 {
        margin-top: 0;
        color: #f1c40f;
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