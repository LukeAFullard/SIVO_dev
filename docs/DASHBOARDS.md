# Building Dashboards with SIVO

Welcome to the SIVO Dashboard guide! This tutorial will walk you through building beautiful, responsive, multi-block interactive dashboards.

SIVO handles the hard parts of web development automatically. You don't need to know HTML, CSS, or JavaScript. Instead, you design your layout visually right inside your Python code using **CSS Grid Builder**.

---

## 🚀 Quick Start: Your First Dashboard

Want to see it in action immediately? Copy and paste the complete, runnable Python script below into a file named `my_dashboard.py` and run it. It generates its own SVG map and outputs a fully functional interactive dashboard.

```python
from sivo import Sivo, SivoDashboard

def main():
    # ---------------------------------------------------------
    # 1. Create an Interactive Map
    # ---------------------------------------------------------
    # We define a simple SVG string for demonstration.
    # In reality, you'd usually load this with Sivo.from_svg("my_map.svg")
    map_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 300">
        <rect width="400" height="300" fill="#f8fafc" rx="10"/>
        <circle id="server_alpha" cx="150" cy="150" r="40" fill="#3b82f6" />
        <circle id="server_beta" cx="280" cy="150" r="40" fill="#10b981" />
        <text x="150" y="210" font-family="sans-serif" font-size="14" fill="#333" text-anchor="middle">Server Alpha</text>
        <text x="280" y="210" font-family="sans-serif" font-size="14" fill="#333" text-anchor="middle">Server Beta</text>
    </svg>"""

    # Initialize the SIVO map from the SVG string
    my_map = Sivo.from_string(map_svg, title="Global Network")

    # Add interactivity to the SVGs!
    # Notice we pass `callback_payload`. This data is sent to the dashboard panels when clicked.
    my_map.map("server_alpha", hover_color="#2563eb", tooltip="Alpha is under heavy load", callback_payload={"status": "Warning", "cpu": "92%", "ram": "14GB"})
    my_map.map("server_beta", hover_color="#059669", tooltip="Beta is operating normally", callback_payload={"status": "Healthy", "cpu": "24%", "ram": "4GB"})


    # ---------------------------------------------------------
    # 2. Design the Dashboard Layout
    # ---------------------------------------------------------
    # Create the dashboard container
    dashboard = SivoDashboard(title="Network Operations Center")

    # Define the responsive Grid Layout.
    # Just imagine this text block as drawing the layout of your screen!
    dashboard.set_grid_layout(
        desktop='''
        "header header"
        "interactive_map metrics_panel"
        "interactive_map details_panel"
        ''',
        mobile='''
        "header"
        "interactive_map"
        "metrics_panel"
        "details_panel"
        '''
    )

    # ---------------------------------------------------------
    # 3. Add Blocks to the Grid Areas
    # ---------------------------------------------------------
    # Now we drop our content into the named areas we just defined above!

    # 1. Header (Custom HTML)
    header_html = "<h2 style='margin:0;'>Network Status Overview</h2><p>Live telemetry dashboard.</p>"
    dashboard.add_html_block("my_header", header_html, grid_area="header")

    # 2. The Map
    dashboard.add_sivo_block("network_map", my_map, grid_area="interactive_map")

    # 3. Metrics Panel (Automatically listens to 'callback_payload' from the map)
    dashboard.add_metrics_panel(
        "live_metrics",
        title="Live Server Stats",
        metrics=["status", "cpu", "ram"], # These must match keys in your callback_payload
        grid_area="metrics_panel"
    )

    # 4. Details Panel (Automatically displays tooltips and HTML mapped to elements)
    dashboard.add_details_panel(
        "server_logs",
        title="Server Logs",
        placeholder="Click a server node on the map to view logs...",
        grid_area="details_panel"
    )


    # ---------------------------------------------------------
    # 4. Generate the Final HTML File
    # ---------------------------------------------------------
    dashboard.to_html("output.html")
    print("Dashboard created successfully! Open 'output.html' in your browser.")

if __name__ == "__main__":
    main()
```

Run the file:
```bash
python my_dashboard.py
```
Then double click the generated `output.html` file to open it in your web browser. Try clicking the blue and green circles!

---

## 🛠️ How It Works in Detail

### 1. Drawing the Grid Layout
The magic of the `SivoDashboard` comes from the `set_grid_layout` function. You define multiline strings that represent the columns and rows of your dashboard.

For example, look at this desktop layout:
```python
desktop='''
"main main side"
"bottom1 bottom2 bottom3"
'''
```
This draws a grid with 2 rows and 3 columns.
* The area named `"main"` spans across the first *two columns* of the first row.
* The area named `"side"` occupies the last column of the first row.
* The bottom row is split evenly into three areas: `"bottom1"`, `"bottom2"`, and `"bottom3"`.

**Rules for Grids:**
1. **Always use a perfect rectangle.** You cannot have "L" shaped areas. If `"main"` is in column 1 of row 1, it cannot be in column 2 of row 2 unless it is also in column 1 of row 2 and column 2 of row 1.
2. **Every area needs a unique name.** Do not name two different sidebars `"sidebar"`. Name them `"sidebar1"` and `"sidebar2"`.
3. **Always define a mobile layout.** The `mobile` parameter determines how the layout collapses on phones. Usually, you just want to stack all the areas vertically in a single column:
    ```python
    mobile='''
    "main"
    "side"
    "bottom1"
    "bottom2"
    "bottom3"
    '''
    ```

### 2. Available Block Types

Once you have your grid drawn out in text, you populate it using four methods. Notice how every method takes `grid_area="name"` to assign it to its spot!

* **`add_sivo_block(id, sivo_app, grid_area)`**: Inserts your interactive SIVO SVG maps. You can put as many independent SIVO maps as you want into a single dashboard.
* **`add_html_block(id, html_string, grid_area)`**: Drops raw HTML into the grid. Useful for headers, titles, or embedding external widgets like a YouTube video iframe.
* **`add_metrics_panel(id, title, metrics, grid_area)`**: Creates a pre-styled "No-Code" panel that listens to map clicks. The `metrics` array (e.g. `["revenue", "status"]`) tells the panel which data keys to extract from the clicked element's `callback_payload`.
* **`add_details_panel(id, title, placeholder, grid_area)`**: Creates a pre-styled panel that listens to map clicks and renders the full HTML or text `tooltip` associated with the clicked element.

### 3. Cross-Block Communication
You do not need to write any JavaScript to make the blocks talk to each other.

If you configure a SIVO map with `callback_payload`:
```python
my_map.map("element_id", tooltip="My Tooltip", callback_payload={"revenue": "$100"})
```
When a user clicks that element on the map:
1. The **Details Panel** will instantly update to show `"My Tooltip"`.
2. The **Metrics Panel** will instantly update the row labeled `revenue` to display `"$100"`.

Everything handles itself dynamically!
