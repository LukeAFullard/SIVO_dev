# Native ECharts Graphic Overlay Example

This example demonstrates how to use the `add_graphic` method in SIVO to overlay native ECharts graphic elements on top of an interactive visualization.

## Purpose

The `add_graphic` method allows you to directly pass [ECharts graphic component configurations](https://echarts.apache.org/en/option.html#graphic) to the underlying renderer. This is useful for adding titles, watermarks, arbitrary shapes, text, or floating UI elements that are independent of the SVG layout itself.

In this example, we show two use cases:
1. Adding a grouped graphic component containing a rounded rectangle and text in the top center of the visualization.
2. Adding a simple floating text watermark in the bottom right corner.

## Code Highlights

### 1. Grouped Graphic Element (Title)
This snippet adds a centered box with text by nesting elements within a `group` type.

```python
app.add_graphic({
    "type": "group",
    "left": "center",
    "top": "20%",
    "children": [
        {
            "type": "rect",
            "z": 100,
            "left": "center",
            "top": "middle",
            "shape": {
                "width": 250,
                "height": 50,
                "r": [5, 5, 5, 5]
            },
            "style": {
                "fill": "rgba(255,255,255,0.8)",
                "stroke": "#cbd5e1",
                "lineWidth": 1
            }
        },
        {
            "type": "text",
            "z": 100,
            "left": "center",
            "top": "middle",
            "style": {
                "fill": "#1e293b",
                "text": "Native ECharts Graphic Element",
                "font": "bold 16px sans-serif"
            }
        }
    ]
})
```

### 2. Floating Watermark
This snippet adds a single text element anchored to the bottom right corner.

```python
app.add_graphic({
    "type": "text",
    "right": 20,
    "bottom": 20,
    "z": 100,
    "style": {
        "fill": "#94a3b8",
        "text": "SIVO x ECharts",
        "font": "italic 14px sans-serif"
    }
})
```

## Running the Example

To run this example and generate the `output.html` file, execute the following command from the root directory:

```bash
PYTHONPATH=src python3 examples/advanced/echarts_graphic/echarts_graphic.py
```
