# Custom Sidebar Styling Example

This example demonstrates how to apply custom CSS styling to SIVO's side panel. It shows both how to define a global style for all side panels and how to override that style for a specific element.

## What is being tested/demonstrated
*   Setting a global `panel_css` attribute when initializing `Sivo`.
*   Setting `default_panel_position="right"` to ensure the side panel opens on the right side of the screen, as the default is `"none"`.
*   Overriding the global CSS with element-specific `panel_css` when mapping interactions using `app.map()`.

## Code Snippets

### 1. Global Panel Styling
When initializing SIVO, you can pass CSS that will apply to the `#info-panel` every time it is opened. We also pass `default_panel_position="right"` to configure its location.

```python
global_panel_css = """
    /* This applies globally to the info-panel container */
    #info-panel {
        background: #f8fafc;
        border-left: 4px solid #3b82f6; /* Blue edge to show global style */
        font-family: "Courier New", Courier, monospace;
    }

    .info-panel-content h3 {
        color: #1d4ed8; /* Blue headers */
        text-transform: uppercase;
        letter-spacing: 1px;
    }
"""

app = Sivo.from_string(
    svg_string,
    title="Custom Sidebar Styling",
    subtitle="Click Region A (global style) or Region B (element-specific override)",
    panel_css=global_panel_css, # Apply the global CSS
    default_panel_position="right" # Open the panel on the right side
)
```

### 2. Mapping a Global-Styled Element
Region A is mapped normally. It will inherit the global CSS defined above.

```python
app.map(
    element_id="region_a",
    html="<h3>Region A Info</h3><p>This sidebar is using the <strong>global panel CSS</strong>.</p>",
    hover_color="#bae6fd"
)
```

### 3. Overriding Styling for a Specific Element
For Region B, we define a different CSS string and pass it directly to `app.map()`. To ensure the new rules take precedence, use specific selectors or `!important`.

```python
region_b_css = """
    /* Overrides the global style specifically when Region B is clicked */
    #info-panel {
        background: #1e293b !important; /* Dark slate */
        color: #f1f5f9; /* Light text */
        border-left: 4px solid #f59e0b !important; /* Orange edge */
        font-family: "Arial", sans-serif !important;
    }

    .info-panel-content h3 {
        color: #fcd34d !important; /* Orange headers */
        border-bottom: 1px solid #334155;
        padding-bottom: 10px;
    }
"""

app.map(
    element_id="region_b",
    html="<h3>Region B Info</h3><p>This sidebar is using an <strong>element-specific CSS override</strong>.</p>",
    hover_color="#fef08a",
    panel_css=region_b_css # Pass the specific CSS here
)
```

## Running the Example
To run the example and generate the `custom_sidebar.html` output file:

```bash
python3 main.py
```

Then open `custom_sidebar.html` in your web browser. Clicking Region A will display a light-themed panel, and clicking Region B will display a dark-themed panel.
