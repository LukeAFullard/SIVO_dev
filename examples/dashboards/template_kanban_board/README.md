# Kanban Board Dashboard Layout

This example demonstrates how to use the modular CSS Grid Builder layout functionality in `SivoDashboard` to create a multi-lane layout reminiscent of a Kanban board.

## Key Concepts

- **Grid Layout Emulation**: `SivoDashboard` uses `dashboard.set_grid_layout` to define customized grid configurations for different screen sizes (e.g., desktop vs. mobile). We arrange the grid layout to group Sivo instances ("task cards") into visually structured vertical areas like lanes.
- **Lanes via grid_area**: In this layout, each "task card" block is assigned to a specific space in the grid via the `grid_area` parameter when calling `dashboard.add_sivo_block`. Here, "to_do1" and "to_do2" act as multiple spots in the "to_do" lane, while "in_progress" and "done" act as subsequent lanes.
- **Independent Contexts**: Each task card is a separate, standalone `Sivo` instance (an interactive SVG), complete with its own tooltips and configurations. They are aggregated within the multi-block layout of a `SivoDashboard`.
- **Default Panel Position**: To suppress side panels and let tooltips drive the map interactions for individual task cards, `default_panel_position` is explicitly set to `"none"`.

## Relevant Code

The main grid structure is defined using the CSS Grid layout mapping for `desktop` and `mobile` views:
```python
    dashboard.set_grid_layout(
        desktop='''
    "to_do1 in_progress done review"
    "to_do2 in_progress done review"
        ''',
        mobile='''
    "to_do1"
    "to_do2"
    "in_progress"
    "done"
    "review"
        '''
    )
```

The individual Sivo objects for each task card are mapped to a given slot in the grid using `grid_area`:
```python
    # Assign blocks to different "lanes" using the 'grid_area' parameter
    dashboard.add_sivo_block("task_api", task1, grid_area="to_do1")
    dashboard.add_sivo_block("task_db", task2, grid_area="to_do2")
```

The `default_panel_position` on each task card avoids loading empty side panels by default:
```python
    return Sivo.from_string(svg, theme="light", layout_size="95%", default_panel_position="none")
```

## Running the Example

Make sure to install requirements from the root directory, then run the script:
```bash
export PYTHONPATH=src
python examples/dashboards/template_kanban_board/main.py
```
This will generate an `output.html` file in the same directory.
