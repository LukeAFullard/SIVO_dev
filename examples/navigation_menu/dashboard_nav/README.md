# Dashboard Navigation Menu Example

This example demonstrates how to use the `navigation_menu` and `navigation_menu_position` configuration options globally on a `SivoDashboard`.

## Purpose

The main purpose of this test/example is to demonstrate:
1.  **Dashboard Configuration:** Passing navigation objects natively to `SivoDashboard` so the menu sits above the entire CSS Grid layout, independent of any individual block or map canvas.
2.  **URL Navigation Options:** Using the `url` key alongside the optional `target` string (e.g. `"_blank"` or `"_self"`) to control link opening behavior.
3.  **UI Positioning:** Setting the menu out of the way of the underlying components utilizing `navigation_menu_position`.

## Key Code Components

1.  **Dashboard Instantiation with Navigation:**
    ```python
    dashboard = SivoDashboard(
        title="Navigation Dashboard Example",
        columns=2,
        navigation_menu=[
            {"label": "Documentation", "url": "https://sivo.dev/docs", "target": "_blank"},
            {"label": "GitHub", "url": "https://github.com/LukeAFullard/sivo"} # Defaults to _self
        ],
        navigation_menu_position="top-right"
    )
    ```
    The menu floats above the dashboard content, providing standard application-level routing.

2.  **Assigning Sivo Blocks:**
    ```python
    dashboard.add_sivo_block("view1", block1, col_span=1)
    dashboard.add_sivo_block("view2", block2, col_span=1)
    ```
    The blocks remain visually unaffected by the global UI navigation overlays.

## How to Run

Ensure you have installed the required dependencies. Then run:

```bash
python examples/navigation_menu/dashboard_nav/dashboard_nav.py
```

This will regenerate `examples/navigation_menu/dashboard_nav/dashboard_nav.html`, which can be opened in any modern web browser to view the interactive navigation features.
