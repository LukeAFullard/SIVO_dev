# Uncertainty Bands Example

This example demonstrates how to create a Line Chart with Uncertainty Bands (also known as Confidence Intervals or error bands) using the SIVO library.

## Purpose

Uncertainty bands are essential in data visualization when you want to show the range of possible values or margin of error associated with a specific data point. This is very common in fields like polling data, statistical forecasting, machine learning predictions, and scientific measurements.

This example illustrates mapping a line chart onto an SVG rect element (`chart_area`), displaying "Candidate Approval Rating" with data spanning from January to July, and rendering an uncertainty band around it using the `uncertainty_lower` and `uncertainty_upper` arguments.

## Code Snippet

The core part of this example is the `map_line_chart` method, where the upper and lower bounds for the uncertainty bands are provided along with the main data points.

```python
# Add a line chart with uncertainty bands
sivo_app.map_line_chart(
    element_id="chart_area",
    title="Candidate Approval Rating",
    categories=["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul"],
    data=[45, 46, 48, 47, 49, 51, 52],
    uncertainty_lower=[41, 42, 44, 43, 46, 48, 49],
    uncertainty_upper=[49, 50, 52, 51, 52, 54, 55],
    uncertainty_color="rgba(59, 130, 246, 0.2)",
    color="#3b82f6",
    smooth=True,
    tooltip="Approval Rating",
    panel_position="overlay"  # Setting the chart to render inside an overlay panel
)
```

## Setup & Running

1. Ensure you have the SIVO library installed (`pip install -e .` from the root of the repo).
2. Run the script from the root directory or inside this folder:
   ```bash
   python examples/charts/uncertainty_bands/uncertainty.py
   ```
3. Open the generated `output.html` file in a web browser to view the interactive chart. You can interact with the element mapped to `chart_area` to display the line chart in an overlay panel.
