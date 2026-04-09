# Echarts Action

## Description
1. Bar Chart Option (TX) 2. Line Chart Option (CA) 3. Pie Chart Option (NY) 4. Gauge Chart Option (WY) Map the elements Export to HTML

## Relevant Code
```python
    sivo_app = Sivo.from_svg(svg_path)
    sivo_app.map(element_id="TX", tooltip="View Regional Data (Bar)", html="<h3>Bar Chart</h3>", echarts_option=bar_chart_option)
    sivo_app.map(element_id="CA", tooltip="View Growth Trend (Line)", html="<h3>Line Chart</h3>", echarts_option=line_chart_option)
    sivo_app.map(element_id="NY", tooltip="View Demographics (Pie)", html="<h3>Pie Chart</h3>", echarts_option=pie_chart_option)
    sivo_app.map(element_id="WY", tooltip="View Energy Output (Gauge)", html="<h3>Gauge Chart</h3>", echarts_option=gauge_chart_option)
    sivo_app.to_html(output_path)
```
