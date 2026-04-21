# Infographic Navigation Menu Example

This example demonstrates how to use the `navigation_menu` and `navigation_menu_position` configuration options on a standalone SIVO Infographic to implement a global "hamburger" dropdown menu.

## Purpose

The main purpose of this test/example is to demonstrate:
1.  **Global Navigation Configuration:** Passing a list of navigation dictionary objects to the `Sivo` instance to automatically generate a UI hamburger menu.
2.  **Internal State Routing:** Using the `view_id` key in the navigation dictionary to seamlessly transition between multiple views (e.g. from "Main" to "Detail") without reloading the page.
3.  **External URL Navigation:** Using the `url` key to link to external websites, and controlling how they open using the optional `target` attribute.
4.  **UI Positioning:** Demonstrating how `navigation_menu_position` anchors the interactive overlay on the canvas.

## Key Code Components

1.  **Configuring the Menu:**
    ```python
    main_app = Sivo.from_string(
        '<svg width="100%" height="100%" viewBox="0 0 100 100"><rect width="100" height="100" fill="#f8fafc"/><text x="50" y="50" font-family="Arial" font-size="10" text-anchor="middle" dominant-baseline="middle" fill="#334155">Main View</text></svg>',
        navigation_menu=[
            {"label": "SIVO Homepage", "url": "https://sivo.dev", "target": "_blank"},
            {"label": "Go to Detail View", "view_id": "detail_view"}
        ],
        navigation_menu_position="top-left"
    )
    ```
    This initializes the interactive SIVO application and attaches the navigation logic to the ECharts overlay interface.

2.  **Bundling the Views:**
    ```python
    project = SivoProject(initial_view_id="main_view")
    project.add_view("main_view", main_app)
    project.add_view("detail_view", detail_app)
    ```
    The `SivoProject` is required to bundle the separate `Sivo` applications together into a single HTML file, which allows the `"view_id"` logic inside the navigation menu to find the referenced views dynamically.

## How to Run

Ensure you have installed the required dependencies. Then run:

```bash
python examples/navigation_menu/infographic_nav/infographic_nav.py
```

This will regenerate `examples/navigation_menu/infographic_nav/infographic_nav.html`, which can be opened in any modern web browser to view the interactive navigation features.
