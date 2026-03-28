# Complex Multi-Block Dashboard with Templates

This example demonstrates how to build a responsive, multi-block dashboard where **each block can be dynamically constructed** using the `SivoDashboard` framework.

## What is Demonstrated

1.  **Dashboard Templates (`Sivo.from_template`)**: We initialize standard SIVO template SVGs, such as `dashboards/sidebar_layout` and `dashboards/four_quadrants`, to easily create common layout structures and inject data into them seamlessly.
2.  **GeoDataFrames (`Sivo.from_geodataframe`)**: We render a block natively generated from spatial boundaries (`GeoPandas` + `Shapely`), mapping interactive data features and choropleth visualizations.
3.  **Cross-Block Interaction**:
    - A central map interacts directly with a **Metrics Panel** and a **Details Panel**, passing specific payload variables via `callback_payload`.
    - Clicking on quadrants also triggers the global metrics panel across block boundaries without requiring custom HTML or JS.
4.  **Embedding ECharts Natively in Templates**: The script embeds two fully interactive ECharts configurations (a bar chart and a pie chart) dynamically injected onto specific SVGs in the four quadrants block template (`quadrant_1` and `quadrant_2`).

## Execution

Ensure you are in this folder, and have `geopandas` and `shapely` installed.

```bash
PYTHONPATH=../../../src python main.py
```

This will produce `output.html`. Open it in any browser to experience the cross-block native interactions and template compositions.
