# Building Reactive Dashboards with SIVO

SIVO provides a powerful, Python-native way to build complex, responsive, multi-block dashboards without writing any custom HTML, CSS, or JavaScript. Instead of relying on rigid, pre-built templates, SIVO uses a **CSS Grid Builder** architecture.

This allows you to define flexible grid layouts natively in Python, assign SIVO maps or custom HTML panels to those grid areas, and let SIVO generate a single, highly-optimized HTML artifact that seamlessly switches between desktop and mobile layouts.

## The `SivoDashboard` Class

To create a dashboard, you instantiate the `SivoDashboard` class and configure its layout:

```python
from sivo import Sivo, SivoDashboard

# Initialize the dashboard container
dashboard = SivoDashboard(title="My Dashboard")
```

### 1. Defining the Layout (`set_grid_layout`)

The core of the dashboard is defined using the `set_grid_layout` method. This method accepts two parameters: `desktop` and `mobile`. These are multiline strings defining [CSS grid-template-areas](https://developer.mozilla.org/en-US/docs/Web/CSS/grid-template-areas).

Each distinct word represents a unique "grid area" that you will later assign a block to. Repeating a word across columns or rows makes that block span those areas.

```python
dashboard.set_grid_layout(
    desktop='''
    "header header header"
    "map map details"
    "metrics metrics metrics"
    ''',
    mobile='''
    "header"
    "map"
    "details"
    "metrics"
    '''
)
```

**Important Rules for Grid Layouts:**
* **Unique Names:** Every distinct block must have a unique grid area name (e.g., `"map1"`, `"map2"`). If you assign two different blocks to the same `"map"` area, they will overlap each other in the browser.
* **Rectangular Areas:** A grid area spanned across multiple rows/columns must form a perfect rectangle. You cannot create an "L" shaped area.
* **Mobile Fallback:** The `mobile` string determines how the blocks stack on screens smaller than 768px. Typically, this is a single vertical column.

### 2. Adding Blocks to the Dashboard

Once the grid is defined, you can populate it by adding blocks. SIVO provides four types of blocks out-of-the-box. When adding a block, you **must** pass the `grid_area` parameter matching a name you defined in `set_grid_layout`.

#### A. Interactive SIVO Maps (`add_sivo_block`)

This is the primary way to embed your interactive SVGs into the dashboard.

```python
sivo_map = Sivo.from_svg('my_map.svg')
sivo_map.map("region_1", tooltip="Region 1 Active")

dashboard.add_sivo_block("main_map_id", sivo_map, grid_area="map")
```

#### B. Custom HTML (`add_html_block`)

You can inject static HTML anywhere in the grid. This is perfect for headers, titles, static legends, or embedding external widgets.

```python
header_html = "<h2>Global System Status</h2><p>Live telemetry data.</p>"
dashboard.add_html_block("header_id", header_html, grid_area="header")
```

#### C. Details Panels (`add_details_panel`)

A Details Panel is a pre-built, reactive "no-code" block. It automatically listens for clicks on *any* SIVO map in the dashboard. When a user clicks a mapped SVG element, this panel automatically renders that element's `html` or `tooltip` content.

```python
dashboard.add_details_panel(
    "details_id",
    title="Region Insights",
    placeholder="Click a region on the map to see details...",
    grid_area="details"
)
```

#### D. Metrics Panels (`add_metrics_panel`)

A Metrics Panel is another reactive block. It automatically listens for clicks on SIVO maps and extracts specific data keys from the clicked element's `callback_payload`.

```python
# Map an element with a data payload
sivo_map.map("server_1", callback_payload={"cpu": "45%", "ram": "2GB"})

# Create a panel that listens for 'cpu' and 'ram' keys
dashboard.add_metrics_panel(
    "metrics_id",
    title="Live Telemetry",
    metrics=["cpu", "ram"],
    grid_area="metrics"
)
```

### 3. Generating the Dashboard

Once all blocks are assigned to their grid areas, export the dashboard to an HTML file.

```python
dashboard.to_html("my_dashboard.html")
```

## Legacy Fallback (Simple Grids)

If you do not call `set_grid_layout`, SIVO will fall back to a simple, auto-flowing column layout based on the `columns` parameter passed during initialization. You can then use the `col_span` parameter on individual blocks to make them span multiple columns.

*Note: This approach is less flexible than explicit CSS Grids and is primarily retained for backward compatibility.*

```python
# Create a 3-column auto-grid
dashboard = SivoDashboard(title="Simple Grid", columns=3)

# Make this map take up 2 of the 3 columns
dashboard.add_sivo_block("map", sivo_map, col_span=2)
# Make this panel take up 1 column
dashboard.add_details_panel("details", col_span=1)
```

## Advanced Features Supported

Because `SivoDashboard` natively wraps the core SIVO runtime, **all advanced interactive features** are fully supported inside individual dashboard blocks, including:
* **Zoom to Element:** `sivo_map.map(..., zoom_to="target_id")`
* **VisualMaps (Choropleths):** Apply data-driven color gradients.
* **Drilldowns:** Seamlessly load secondary SVG views.
* **Confetti & URL Actions:** Trigger external links or visual effects natively.
