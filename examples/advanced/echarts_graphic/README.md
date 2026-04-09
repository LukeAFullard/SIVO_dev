# Echarts Graphic

## Description
A simple map representing a layout Add native ECharts graphic components over the visualization This adds a title text in the center and a watermark image Add a floating watermark graphic

## Relevant Code
```python
app = Sivo.from_string(svg_content)
app.map("regionA", tooltip="Region A")
app.map("regionB", tooltip="Region B")
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
app.to_html(output_path)
```
