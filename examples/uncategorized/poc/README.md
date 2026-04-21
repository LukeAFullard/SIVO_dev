# SIVO Proof of Concept (PoC)

This is a general proof of concept script that demonstrates the core fundamental capabilities of the SIVO engine in a single, simple example.

## What is being shown
- Generating an infographic view from an inline SVG string containing simple paths, rects, and circles.
- Mapping multiple elements with static tooltip text and complex inline HTML strings for side panels.
- Applying specific stroke colors (`border_color`), hover colors, stroke widths, and glow effects to single elements (like `fountain`).
- Using Shadow DOM automatically (demonstrated by applying arbitrary CSS `<style>` blocks in the fountain's mapped HTML, which does not break or leak onto the rest of the application styling).
- Exporting raw SVG metadata via `export_metadata()`, which dumps out the structure and ID boundaries of the SVG.

## Key Code Snippets

```python
sivo_instance.map(
    "fountain",
    html="""
    <style>
        h3 { color: darkblue; }
        .fountain-desc { border: 1px solid blue; padding: 5px; }
    </style>
    <h3>Central Fountain</h3>
    <p class="fountain-desc">A nice place to relax. Note this CSS does not bleed out due to Shadow DOM!</p>
    """,
    tooltip="Relaxation Zone",
    color="#ccccff", # Light blue
    hover_color="#aaaaff",
    border_width=3,
    border_color="#0000ff",
    glow=True
)
```

## Running the example
To run the example and generate the output files:
```bash
python poc.py
```
Open the generated `output.html` in your browser. Inspect the `metadata.json` to see the bounding box properties automatically extracted from the provided SVG paths.
