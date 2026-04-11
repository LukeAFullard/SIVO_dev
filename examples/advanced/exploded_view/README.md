# Exploded View Transition

This example demonstrates how to use the `SivoProject` class and the `explode_to` mapping property to create an animated "explode" or "peel-back" transition between two distinct map views (SVGs).

## What is being shown?
Often, in complex dashboards, you want to show a dense cluster of elements (like a map) and allow the user to expand or "explode" those elements out into a stylized grid or hexbin view to see more detail without clutter.

Instead of an instant jump (like standard drill-down), SIVO's `explode_to` property tells the frontend runtime to attempt to morph the current view into the new target view over a specified duration, creating a smooth visual transition.

## Key Code Snippets

### 1. Creating the Project
Because we are navigating between multiple views (the dense map and the exploded grid), we use a `SivoProject` to orchestrate them.

```python
# Initialize the project with the ID of the starting view
project = SivoProject(initial_view_id="dense_view")
```

### 2. The Dense View (Starting State)
We map a button (`explode_btn`) to trigger the transition using `explode_to="exploded_view"` and setting an animation duration.

```python
s1 = Sivo.from_svg(dense_map, default_panel_position="none")
s1.map("explode_btn", explode_to="exploded_view", explode_duration_ms=600, tooltip="Click to Peel-Back")
project.add_view("dense_view", s1)
```

### 3. The Exploded View (Target State)
We map a return button (`reset_btn`) to animate back to the initial map. Notice we also map interactions to elements within the exploded view (like `r1_exp`).

```python
s2 = Sivo.from_svg(exploded_map, default_panel_position="none")
s2.map("reset_btn", explode_to="dense_view", explode_duration_ms=600, tooltip="Go Back")
s2.map("r1_exp", tooltip="District A (Expanded)", footnote="Detailed demographics available here.")
project.add_view("exploded_view", s2)
```

### 4. Generation
Finally, we output the entire project to a single standalone HTML bundle.
```python
project.to_html(output_path)
```
