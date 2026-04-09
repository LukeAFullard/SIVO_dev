---
Last Updated: 2026-04-09
SIVO Version: 0.1.0
---

# Multi-View Projects

SIVO supports multi-level dashboards (drilldowns) by registering secondary views with `SivoProject`. This allows you to organize complex applications and interconnected views that compile down to a single standalone HTML bundle.

## The `SivoProject` Class

The `SivoProject` class manages multiple `Sivo` instances, acting as "views" within a larger application.

### Basic Initialization

To begin, you create an instance of `SivoProject` and specify the `initial_view_id`. This is the ID of the view that will be displayed when the application first loads.

```python
from sivo.core.project import SivoProject
from sivo.core.sivo import Sivo

# Initialize the main view and a secondary view
main_view = Sivo.from_svg("main_map.svg")
detail_view = Sivo.from_svg("detail_map.svg")

# Create a SivoProject with the initial view
project = SivoProject(initial_view_id="main_view")
```

### Adding Views

Once the project is created, you add `Sivo` instances using the `add_view` method, specifying a unique ID for each view.

```python
# Add the views to the project
project.add_view(view_id="main_view", sivo_app=main_view)
project.add_view(view_id="detail_view", sivo_app=detail_view)
```

## Connecting Views

To connect views, you configure an element in one view to drill down into another view. This is done by passing the `drill_to` parameter to the `map` method.

```python
# Configure a state shape in the main view to drill down to the detail view
main_view.map(
    element_id="state_california",
    drill_to="detail_view",
    drill_transition="slide" # Optional transition effect
)
```

Behind the scenes, this creates a `DrillDownAction(target_svg="detail_view")` which tells the SIVO JS runtime to transition to the new view and push it onto the view history stack. You can also configure a `drill_through` to an external URL or use other interactions simultaneously.

## Compiling the Project

To compile all registered views into a single interactive HTML bundle, use the `to_html` method on the `SivoProject` instance.

```python
# Generate a single interactive HTML string containing all views
project.to_html(output_path="multi_view_app.html")
```

The compiled `multi_view_app.html` file will contain all necessary SVG data, mappings, and configurations for every registered view. Users can interact with the initial view, drill down to secondary views, and use built-in navigation (e.g. back buttons or breadcrumbs depending on the layout) to return.
