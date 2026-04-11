# Trendline Variations Chart Example

This example demonstrates how to use the `map_trendline_chart` method in SIVO to visualize scatter plot data with different types of overlaid trendlines.

## What is being tested/shown

1.  **Multiple Trendline Types**: The example displays four different charts mapped to distinct SVG elements, each illustrating a specific mathematical trendline:
    *   **Linear**: A straight line representing a constant rate of change.
    *   **Exponential**: A curve showing a constantly accelerating growth rate.
    *   **Logarithmic**: A curve representing a trend that grows quickly initially but then levels off.
    *   **Polynomial**: A curve that fits data with multiple fluctuations (in this case, used for a simulated stock price).
2.  **Custom Styling**: The trendlines are customized with different colors, widths, and arrows to differentiate them visually, using properties like `trendline_color`, `trendline_width`, and `trendline_arrow`.
3.  **Side Panel Configuration**: The example correctly configures the side panel to be visible by setting `default_panel_position="right"` in `ProjectConfig` and `panel_position="right"` in the individual chart mappings, making the charts pop up on the right-hand side when the associated SVG elements are clicked.

## Relevant Code

*   **`ProjectConfig`**: Shows initialization with `default_panel_position="right"` so the default "none" is overridden, ensuring panels open.
    ```python
    config = ProjectConfig(
        title="Trendline Variations",
        svg_file=svg_path,
        enable_minimap=False,
        theme="light",
        default_panel_position="right"
    )
    ```

*   **`map_trendline_chart` calls**: Examples of applying the different variations of the trendlines to the data sets, customizing their visual presentation. For example, for the logarithmic trendline:
    ```python
    app.map_trendline_chart(
        element_id="chart_logarithmic",
        title="Engagement (Logarithmic)",
        data=log_data,
        trendline_type="logarithmic",
        trendline_color="#10b981", # Green
        trendline_width=4,
        trendline_arrow=True,
        color="#6ee7b7", # Light Green
        panel_position="right"
    )
    ```

## How to Run

To run this example and generate the HTML output:

```bash
PYTHONPATH=src python3 examples/charts/trendlines/main.py
```
This will compile `output.html` in the current directory. Open this file in a web browser and click on the elements within the SVG image to view the interactive scatter charts and their corresponding trendlines in the right-side panel.
