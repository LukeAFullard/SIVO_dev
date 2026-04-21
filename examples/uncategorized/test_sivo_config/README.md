# SIVO JSON Config Initialization

This example demonstrates how to initialize SIVO directly from a declarative JSON configuration file (`project.json`) rather than writing imperative Python code using `Sivo.map()`.

## What is being shown
- Defining a `project.json` file that specifies the base SVG file (`sample.svg`) and a dictionary of element `mappings` (e.g., tooltips, colors, html).
- Using `Sivo.from_config()` to load the application state from this JSON file.
- Generating the resulting interactive HTML bundle.

## Key Code Snippets

```python
# Load SIVO state directly from a JSON configuration file
config_path = os.path.join(os.path.dirname(__file__), "project.json")
sivo_instance = Sivo.from_config(config_path)

# Generate the output HTML
output_path = os.path.join(os.path.dirname(__file__), "config_output.html")
sivo_instance.to_html(output_path)
```

## Running the example
To run the example and generate the HTML output:
```bash
python test_sivo_config.py
```
Open the generated `config_output.html` in your browser. Inspect the `project.json` file to see how properties like `hover_color`, `tooltip`, and `html` are structured in a JSON format instead of Python keyword arguments.
