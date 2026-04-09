# Masking Clipping

## Description
Demonstrates the use of SIVO for masking clipping.

## Relevant Code
```python
sivo_app = Sivo.from_string(svg_string, render_mode="svg")
sivo_app.map(
    element_id="rectToClip",
    tooltip="This rectangle is clipped by a circle",
    clip_path="url(#myClip)"
)
sivo_app.map(
    element_id="rectToMask",
    tooltip="This rectangle is masked by a circle",
    mask="url(#myMask)"
)
sivo_app.to_html(output_path)
```
