---
Last Updated: 2026-04-09
SIVO Version: 0.1.0
---

# H-18: Built-in Templates Guide

Guide on using the built-in aspect-ratio based SVG templates (1_1, 16_10, 3_2, etc.) and filling zones programmatically.

## Table of Contents

1. **Introduction to SIVO Templates**
   - Exploring the built-in catalog.
2. **Loading Templates**
   - Using `Sivo.from_template()`.
3. **Dynamic UI Layers**
   - Using `fill_template_zone()`.
   - Using `add_overlay()`.
   - Using `add_scalable_text()`.
   - Using `add_scalable_progress_bar()`.
4. **Examples**
   - Dashboard Template Example.
   - Timeline Template Example.

## 1. Introduction to SIVO Templates

While SIVO is excellent at converting your custom SVGs into interactive maps, it also comes bundled with a library of professionally designed, responsive SVG templates. These are organized by aspect ratio (e.g., `1_1`, `16_10`, `3_2`, `4_3`, `4_7`) and use cases (e.g., dashboards, timelines, nodes).

These templates contain pre-defined "zones" or placeholder shapes (like `<rect>` or `<path>` elements with specific IDs) that you can target to inject text, charts, or HTML dynamically.

## 2. Loading Templates

You can load a specific built-in template quickly using the `Sivo.from_template()` class method.

```python
from sivo import Sivo

# Loads the 'dashboard_template.svg' from the built-in library
dashboard = Sivo.from_template("dashboard")

# Loads the 'timeline_5_nodes_template.svg' (or similar base timeline)
timeline = Sivo.from_template("timeline")
```

If you need a specific file from the templates folder, you can still use `Sivo.from_svg()` and point it directly to the path (e.g., `src/sivo/templates/16_10/gis_digital_twin_dashboard_2026.svg`).

## 3. Dynamic UI Layers

Once you have loaded a template, SIVO provides several methods to inject content into it cleanly, ensuring everything scales natively with the SVG.

### `fill_template_zone()`

This method replaces a placeholder SVG shape (like a bounding box `<rect>`) with native, perfectly-scaled SVG `<text>`.

*Why use this?* Native SVG text scales perfectly with the `viewBox`, looking crisp on both mobile and massive desktop monitors, without relying on complex CSS or HTML overlays.

```python
app.fill_template_zone(
    element_id="title_box",
    text="Global Operations",
    font_size="50%", # relative to box height
    font_weight="bold",
    color="#333333",
    align="center",
    auto_shrink=True # prevents text from spilling out of the box
)
```

### `add_overlay()`

Clips raw HTML content directly over a specific SVG element shape. This is perfect for injecting complex HTML, CSS, or even secondary ECharts instances (like mini pie charts) directly onto a dashboard panel.

```python
metric_html = """
<div style="text-align: center; display: flex; flex-direction: column; justify-content: center; height: 100%;">
    <h3 style="margin: 0; color: #888;">Revenue</h3>
    <p style="margin: 0; color: #2ecc71; font-size: 24px; font-weight: bold;">$12.5M</p>
</div>
"""
app.add_overlay("metric_panel_1", metric_html)
```

### `add_scalable_text()`

Adds a responsive HTML text container as an overlay, positioned relative to the overall canvas or a specific container. Useful when you need HTML text layout capabilities rather than native SVG text.

```python
app.add_scalable_text(
    target_id="header_area",
    text="Oncology Pipeline",
    left="5%", top="20%", width="90%", height="40%",
    font_size="35%", font_weight="900", color="#0f172a", align="left"
)
```

### `add_scalable_progress_bar()`

Injects a native, scalable SVG progress bar, useful for timelines or metric dashboards.

```python
app.add_scalable_progress_bar(
    target_id="node_4_card",
    progress="75%",
    left="55%", top="80%", width="40%", height="5%",
    bg_color="#e2e8f0", fill_color="#f59e0b"
)
```

## 4. Examples

### Dashboard Template

Using a built-in dashboard template and injecting text and interactive ECharts:

```python
from sivo import Sivo

dashboard = Sivo.from_template("dashboard")

# Inject HTML overlay into the header area
header_html = """
<div style="text-align: center; display: flex; flex-direction: column; justify-content: center; height: 100%;">
    <h1 style="margin: 0;">Global Sales Overview</h1>
</div>
"""
dashboard.add_overlay("header_area", header_html)

# Map an interactive EChart to the main chart area
main_chart_option = {
    "xAxis": {"type": "category", "data": ["Jan", "Feb", "Mar"]},
    "yAxis": {"type": "value"},
    "series": [{"data": [820, 932, 901], "type": "line"}]
}
dashboard.map(
    element_id="main_chart_area",
    tooltip="Monthly Trend",
    echarts_option=main_chart_option
)

dashboard.to_html("dashboard.html")
```

### Timeline Template

Building a step-by-step timeline using scalable text and progress bars:

```python
from sivo import Sivo

app = Sivo.from_template("timeline")

# Add text to the first node
app.add_scalable_text(
    "node_1_card",
    "2022: PHASE I",
    left="5%", top="5%", width="90%", height="20%",
    font_size="15%", font_weight="800", color="#8b5cf6"
)

# Add an interactive pie chart overlay to the node
node_pie = """
<div style="width: 100%; height: 100%; display: flex; align-items: center; justify-content: center;">
    <svg width="50%" height="50%" viewBox="0 0 32 32">
        <circle r="16" cx="16" cy="16" fill="#3b82f6" stroke-width="32" stroke-dasharray="70 100" />
    </svg>
</div>
"""
app.add_overlay("node_1_card", node_pie)
app.map("node_1_card", hover_color="#eff6ff", glow=True)

app.to_html("timeline.html")
```
