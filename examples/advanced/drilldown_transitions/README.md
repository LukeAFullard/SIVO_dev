# Drilldown Transitions Example

This example demonstrates how to configure view-to-view transition animations in SIVO multi-view projects (drilldowns). Using `SivoProject`, multiple independent `Sivo` applications are linked together, and clicking on an element in one view transitions to another view.

SIVO supports various transition animations when navigating between views. In this example, we configure:

- **Flip**: A 3D flip animation (View 1 -> View 2).
- **Page Turn**: A page turning effect (View 2 -> View 3).
- **Slide Right / Slide Up**: Directional sliding animations (View 2 -> View 1 and View 3 -> View 1).

## Relevant Code

Linking elements and defining transitions is handled in `sivo.map()` using the `drill_to` and `drill_transition` parameters:

```python
# From View 1 -> View 2 using a 3D "flip" animation
app1.map("btn_next_1", drill_to="view2", drill_transition="flip", hover_color="#0284c7")

# From View 2 -> View 3 using a "page-turn" animation
app2.map("btn_next_2", drill_to="view3", drill_transition="page-turn", hover_color="#15803d")

# From View 2 -> View 1 using a "slide-right" animation (like going back)
app2.map("btn_back_2", drill_to="view1", drill_transition="slide-right", hover_color="#15803d")

# From View 3 -> View 1 using a "slide-up" animation
app3.map("btn_home_3", drill_to="view1", drill_transition="slide-up", hover_color="#7e22ce")
```

The multi-view application is combined using `SivoProject`:

```python
# Combine them into a multi-view application using SivoProject
from sivo.core.project import SivoProject
project = SivoProject(initial_view_id="view1")
project.add_view("view1", app1)
project.add_view("view2", app2)
project.add_view("view3", app3)

# Export to an HTML file
project.to_html(output_path='index.html')
```

## Running the Example

Run the following command from the project root:

```bash
PYTHONPATH=src python examples/advanced/drilldown_transitions/main.py
```

Then, open `examples/advanced/drilldown_transitions/index.html` in a web browser to experience the animations in action.
