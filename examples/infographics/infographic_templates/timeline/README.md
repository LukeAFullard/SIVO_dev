# Timeline Infographic Template Example

This example demonstrates how to build an interactive timeline infographic using SIVO's built-in `other/timeline` template.

## Features Demonstrated

*   **`Sivo.from_template()`**: Loading a built-in template SVG.
*   **HTML Overlays**: Adding rich HTML content (headers, timeline node cards) directly onto specific areas of the timeline template using `add_overlay()`. The HTML is styled to be responsive using `container-type: inline-size` and `clamp()`.
*   **Interactive Mapping**: Binding interactive elements to specific SVG nodes (e.g., `node_{i}_dot` and `node_{i}_card`) using the `map()` method. The `panel_position="right"` is used to show detailed information when a user interacts with the timeline milestones.

## Code Highlights

```python
# Load the timeline template
timeline = Sivo.from_template("other/timeline", default_panel_position="none")

# Add text overlays to timeline nodes
for i, date in enumerate(["Q1 2023", "Q3 2023", "Q1 2024", "Q4 2024"], 1):
    html = f"""
    <div style="...">
        <h3>{date}</h3>
        <p>Milestone {i}: Project Phase {i} Launch</p>
        <button>View Details</button>
    </div>
    """
    timeline.add_overlay(f"node_{i}_card", html)

    # Map interactivity to the node dot
    timeline.map(
        element_id=f"node_{i}_dot",
        panel_position="right",
        html=f"<h3>{date} Details</h3><p>Extensive details for milestone phase {i}...</p><p>Resources allocated: {i*50}h</p>",
        hover_color="#60a5fa",
        glow=True
    )
```

## Running the Example

Run the following command from the root directory:

```bash
PYTHONPATH=src python3 examples/infographics/infographic_templates/timeline/main.py
```

This will generate an `output.html` file in the same directory, containing the interactive timeline.
