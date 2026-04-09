# Datazoom

## Description
Generate a large dataset for demonstration Create an empty SVG canvas programmatically Initialize Sivo Map a Scatter Chart to the container, explicitly enabling datazoom Output dynamically to the script's directory

## Relevant Code
```python
app = Sivo.from_string(svg_string, theme="light")
app.map_scatter_chart(
    element_id="chart-container",
    title="High-Density Scatter with DataZoom",
    data=data,
    color="#43a2ca",
    tooltip="Value: {c}",
    datazoom=True,
    extra_options={
        "xAxis": {"type": "value", "scale": True},
        "yAxis": {"type": "value", "scale": True}
    }
)
app.to_html(output_path)
```
