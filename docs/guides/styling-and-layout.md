---
Last Updated: 2026-04-09
SIVO Version: 1.0.0
---

# H-04: Styling and Layout Guide Plan

Comprehensive guide on SVG attributes, CSS injection, and layout containers.

## Table of Contents

1. **SVG Attributes and ECharts**
   - How ZRender parses standard SVG attributes.
   - Limitations (e.g., `<text>` nodes without `id`, `textLength` ignored).
2. **Injecting CSS into SIVO**
   - Using `panel_css` and `global_css`.
   - Security considerations (CSS sanitization).
3. **Layout Containers**
   - Configuring the main canvas.
   - Multi-block dashboards vs. single-view (Dashboard Blocks vs. Echarts runtime).
4. **Programmatic Card Generation**
   - Using `Sivo.add_card()` to generate auto-scaled SVG elements.
   - Example Python snippet:
     ```python
     sivo.add_card(
         target_id="background_rect",
         title="Sales Data",
         value="$1M",
         subtitle="Q3 Results",
         shape="pill"
     )
     ```
5. **Interactive Image Fills**
   - Setting `fill_pattern` and `hover_image`.
