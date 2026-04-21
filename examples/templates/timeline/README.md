# 5-Node Timeline Flow

This example visualizes a clinical trial progression timeline using a 5-node horizontal template, enriched with embedded data visualizations at each stage.

## Key Features Demonstrated

1.  **Timeline Template**: Uses the `timeline_5_nodes_template.svg` to structure a linear process flow.
2.  **Scalable Data Annotations**: Replaces static placeholder text with responsive, auto-shrinking text (`app.add_scalable_text`) detailing the drug development phases across nodes (`node_1_card` to `node_5_card`).
3.  **Embedded HTML Visualizations**: Incorporates different mini-charts onto the timeline nodes:
    *   **Pie Chart** (SVG) on Node 1
    *   **Bar Chart** (HTML divs) on Node 2
    *   **Multi-series Line Chart** (SVG) on Node 3
4.  **Native Progress Bar Integration**: Demonstrates using `app.add_scalable_progress_bar` on Node 4 to show clinical trial enrollment progress natively without custom HTML.
5.  **Hover Interactions & Glow Effects**: Maps a subtle `hover_color` and enabling the `glow=True` effect on each node card to make the timeline feel interactive and polished.

## Example Code Highlights

**Adding Scalable Text with Auto-Shrink:**

```python
app.add_scalable_text(
    "node_1_card",
    "In vitro/vivo testing. Pharmacodynamics established.",
    left="5%", top="25%", width="90%", height="20%",
    font_size="10%", font_weight="500", color="#475569",
    auto_shrink=True # Ensures text fits within constraints
)
```

**Native Progress Bar Definition:**

```python
app.add_scalable_progress_bar(
    "node_4_card",
    progress="100%",
    left="55%", top="80%", width="40%", height="5%",
    rx="4", bg_color="#e2e8f0", fill_color="#f59e0b"
)
```
