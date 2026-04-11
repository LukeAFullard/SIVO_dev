# Complex Multi-Block Dashboard with Templates

This example demonstrates how to build a responsive, multi-block dashboard where **each block can be dynamically constructed** using the `SivoDashboard` framework. It shows the composition of standard SIVO templates and generated maps, as well as complex interactions that span across the different blocks.

## What is Demonstrated

1.  **Dashboard Layouts (`SivoDashboard`)**: We initialize a global dashboard using `SivoDashboard(title="...", columns=4)`. This creates a flexible CSS Grid wrapper to align various visual blocks seamlessly.

2.  **Dashboard Templates (`Sivo.from_template`)**: We initialize standard SIVO template SVGs, such as `dashboards/sidebar_layout` and `dashboards/four_quadrants`, to easily create common layout structures without needing custom SVG assets.
    ```python
    sidebar_block = Sivo.from_template("dashboards/sidebar_layout")
    quad_grid_block = Sivo.from_template("dashboards/four_quadrants")
    ```

3.  **GeoDataFrames Map Blocks (`Sivo.from_geodataframe`)**: We render a block natively generated from spatial boundaries (`GeoPandas` + `Shapely`), mapping interactive data features and choropleth visualizations.

4.  **Cross-Block Interaction**:
    - Interactive elements trigger shared, global panels using standard `callback_payload`.
    - Clicking on quadrants or map zones triggers a built-in Metrics Panel and a built-in Details Panel across block boundaries without requiring custom HTML or JS.
    ```python
    dashboard.add_metrics_panel(
        block_id="kpi_metrics",
        title="Live Metrics",
        metrics=["Users", "Revenue", "Growth"],
        col_span=1
    )
    ```

5.  **Embedding ECharts Natively in Templates**: We inject fully interactive ECharts components (a bar chart and a pie chart) dynamically directly onto specific template sub-regions (`quadrant_1` and `quadrant_2`). Crucially, we pass `panel_position="overlay"` so the charts overwrite the native SVG geometry rather than attempting to open in a non-existent side panel.
    ```python
    quad_grid_block.map_bar_chart(
        element_id="quadrant_1",
        title="Revenue by Quarter",
        categories=["Q1", "Q2", "Q3", "Q4"],
        data=[12000, 15000, 14000, 18000],
        color=["#3b82f6", "#10b981", "#f59e0b", "#ef4444"],
        panel_position="overlay"
    )
    ```

## Execution

Ensure you are in this folder, and have `geopandas` and `shapely` installed.

```bash
PYTHONPATH=../../../src python main.py
```

This will produce `output.html`. Open it in any browser to experience the cross-block native interactions and template compositions.
