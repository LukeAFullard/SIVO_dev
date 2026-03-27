# Bento Box Dashboard Example

This example demonstrates how to build a clean, modern, multi-block dashboard using the `bento_box.html` template.
It features an auto-fitting CSS Grid layout that naturally arranges panels of different sizes (using `col_span`)
into an asymmetrical "bento box" style UI, complete with hover states and modern shadows.

## Key Features Demonstrated

- Using a specific dashboard template (`template="bento_box"`).
- Controlling layout spanning with `col_span`.
- Cross-block communication (clicking the map updates the Details and Metrics panels).

## How to run

Ensure you have SIVO installed, then run:

```bash
python main.py
```

Open `output.html` in your browser.