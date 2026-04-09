---
Last Updated: 2026-04-09
SIVO Version: 1.0.0
---

# H-06: Drilldowns & State Management

Managing the `viewHistory` stack and multi-level data dashboards in SIVO.

## Table of Contents

1. **Understanding Drilldowns**
2. **Configuring Multiple Views**
3. **The `viewHistory` Stack**
4. **State Restoration**
5. **Complex Multi-Level Dashboards**

---

## 1. Understanding Drilldowns

A **drilldown** allows a user to navigate from a parent SVG element (like a country on a map or a category bar in a chart) to a completely new child SVG or "View" (such as states within that country or sub-categories).

In SIVO, drilldowns replace the currently visible interactive map canvas with a different pre-configured map while keeping the overall user interface intact. SIVO retains the navigation history, letting users seamlessly return to the parent views using an auto-generated "Back" button.

This mechanism enables the creation of complex, multi-layered exploratory data visualisations without forcing the browser to load entirely new web pages.

## 2. Configuring Multiple Views

To use drilldowns effectively, you need a mechanism to bundle multiple SIVO instances into a single output. You achieve this using the `SivoProject` class.

Instead of generating a standalone HTML file from a single `Sivo` instance, a `SivoProject` serves as a container for many named `Sivo` instances (views).

### Step 1: Create the Views

First, create independent `Sivo` objects for your parent and child views.

```python
from sivo.core import Sivo
from sivo.core.actions import DrillDownAction
from sivo.core.project import SivoProject

# 1. Create the parent map (e.g., USA map)
usa_map = Sivo.from_svg("usa.svg")

# 2. Create the child map (e.g., California map)
ca_map = Sivo.from_svg("california.svg")

# 3. Add interactivity to the child map
ca_map.map(
    "los_angeles_county",
    tooltip="Population: 9.8M",
    fill_color="#ffcc00"
)
```

### Step 2: Link the Parent to the Child View

Use the `DrillDownAction` on the parent view to link a specific SVG element to the ID of the child view you intend to register.

```python
# Link the 'california_state' element in usa.svg to the 'view_california' child view.
usa_map.map(
    "california_state",
    click=DrillDownAction(target_svg="view_california", transition="fade")
)
```

*Note: The `target_svg` in `DrillDownAction` must exactly match the `view_id` you will use when registering the view with the project.*

### Step 3: Bundle with `SivoProject`

Register all your views with a `SivoProject`, specifying which view should be displayed first.

```python
# Create a project, setting the initial view ID
project = SivoProject(initial_view_id="view_usa")

# Add the parent and child Sivo instances to the project
project.add_view(view_id="view_usa", sivo_app=usa_map)
project.add_view(view_id="view_california", sivo_app=ca_map)

# Export the entire multi-view project as a single HTML bundle
html_output = project.to_html(output_path="dashboard.html")
```

## 3. The `viewHistory` Stack

When the SIVO frontend is generated, it automatically manages a `viewHistory` stack in JavaScript.

This stack tracks the user's path through the linked views.

### How it works under the hood

When a user clicks an element configured with a `DrillDownAction`, SIVO's ECharts event handler intercepts it.
If the target is a registered internal view, SIVO performs the following actions:

1. **Pushes** the `currentViewId` onto the `viewHistory` array.
2. **Updates** the `currentViewId` to the target view.
3. **Renders** the new view using the `renderView()` function.
4. **Evaluates** the "Back" button visibility based on the stack depth.

```javascript
// A conceptual snippet of SIVO's internal drilldown handling logic
if (action.action_type === 'drilldown') {
    if (viewsData[action.target_svg]) { // Check if internal view
        // Push the current view onto history stack before changing
        viewHistory.push(currentViewId);

        // Render the target view
        renderView(action.target_svg, false);

        // Update the Back Button visibility
        updateBackButton();
    }
}
```

The "Back" button (usually displayed as an overlay in the top-left corner) is updated using a simple function that checks the history length:

```javascript
function updateBackButton() {
    if (viewHistory.length > 0) {
        backBtn.style.display = 'flex';
    } else {
        backBtn.style.display = 'none';
    }
}
```

*Important Note:* Avoid using `setInterval` or polling loops to check `viewHistory.length` to show/hide the back button. Always rely on direct function calls like `updateBackButton()` triggered by actual state transitions to prevent memory leaks.

## 4. State Restoration

Navigating backwards through a multi-view project requires more than just loading the previous SVG. If the user had previously zoomed or panned in the parent view, that state must be cleanly reset when returning.

When the user clicks the "Back" button:

1. The last view ID is popped from the `viewHistory` stack.
2. The `renderView(prevView, true)` function is called, with a flag indicating it is a "Back" navigation.
3. Crucially, SIVO dispatches a `'restore'` action to ECharts to clear pan, zoom, and transform mutations.
4. SIVO re-applies the baseline view configurations (like the initial `layoutSize` and `zoom`) to ensure the map renders exactly as intended, unaffected by prior user interactions.

## 5. Complex Multi-Level Dashboards

You can chain multiple `DrillDownAction` connections to create deep, nested dashboards.

For example: **World Map** -> **Country Map** -> **State Map** -> **County Map**.

To manage complex multi-level structures efficiently:

1. **Use clear, hierarchical `view_id` names** (e.g., `view_world`, `view_us`, `view_us_ny`, `view_us_ny_kings`).
2. **Pre-process Data:** Loop through your geographical hierarchies in Python, dynamically instantiating `Sivo` objects and linking them to their parents before adding them to the `SivoProject`.
3. **External SVG loading:** The `DrillDownAction` also supports loading external SVG files via a URL as a fallback if the ID isn't registered in the `SivoProject`. This is useful if the data payload is too large to bundle into a single HTML file initially. Note that external views loaded this way will lack internal map configuration and interactive mappings initially.
