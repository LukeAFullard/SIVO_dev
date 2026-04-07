# 05 Custom Assets

This example shows how to inject custom CSS and JavaScript into the generated HTML output. This is useful for custom styling of elements like tooltips or adding additional functionality.

### Key Code

```python
# Custom CSS and JS to inject into the HTML template
custom_css = """
    .custom-tooltip { background-color: #333; color: #fff; padding: 10px; }
"""

custom_js = """
    console.log('Hello from custom injected JS!');
"""

sivo_app.to_html(output_path, custom_css=custom_css, custom_js=custom_js)
```
