# Embedded Bar Race Chart Example

This example demonstrates how to embed a complex ECharts animation—specifically an automated Bar Race chart—inside a SIVO dashboard.

## Purpose

The main goal of this example is to show how to configure ECharts natively using its `timeline` functionality. A Bar Race chart is essentially a bar chart that changes its data over time, re-sorting its values in real-time to create a "racing" effect.

## Key Concepts

- **ECharts Timeline (`timeline`)**: The `baseOption` contains a `timeline` block that automatically plays through different years (`2019` to `2023`).
- **Realtime Sorting (`realtimeSort`)**: Setting `realtimeSort: True` on the bar series tells ECharts to automatically re-order the bars from highest to lowest during each timeline step.
- **Side Panel (`panel_position`)**: This example maps the race to open in the right side panel when a button on the SVG canvas is clicked. Since SIVO's default panel position is `none`, we explicitly configure it via `ProjectConfig` and `ElementConfig`.

## Code Highlights

In `main.py`, the core configuration for the bar race is defined inside the `bar_race_option` dictionary:

```python
    bar_race_option = {
        "baseOption": {
            "timeline": {
                "axisType": 'category',
                "autoPlay": True,
                "playInterval": 1500,
                "data": years,
                "label": {"formatter": '{value}'}
            },
            "series": [
                {
                    "realtimeSort": True,
                    "name": 'Sales',
                    "type": 'bar',
                    # ...
                }
            ],
            # ...
        },
        "options": options # The specific data snapshots for each year
    }
```

The SVG trigger is then mapped to this ECharts configuration:

```python
    config = ProjectConfig(
        svg_file=svg_path,
        default_panel_position="right",
        mappings={
            "race_trigger_button": ElementConfig(
                tooltip="Open Race Chart",
                echarts_option=bar_race_option,
                panel_position="right",
                open_by_default=True
            )
        }
    )
```

## How to Run

Execute the `main.py` script:

```bash
PYTHONPATH=src python3 examples/charts/bar_race_embed/main.py
```

This will generate a `bar_race.html` file that you can open in your browser to view the interactive dashboard with the embedded bar race chart.
