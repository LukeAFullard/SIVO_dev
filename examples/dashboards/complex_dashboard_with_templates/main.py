from sivo.core.sivo import Sivo
from sivo.core.dashboard import SivoDashboard
import geopandas as gpd
from shapely.geometry import Polygon

def main():
    dashboard = SivoDashboard(title="Complex Dashboard with Multiple Blocks", columns=4)

    # ---------------------------------------------------------
    # Block 1: Sidebar Dashboard Template (from_template)
    # ---------------------------------------------------------
    sidebar_block = Sivo.from_template("dashboards/sidebar_layout")

    try:
        sidebar_block.map(
            element_id="nav_item_1",
            tooltip="Map View",
            hover_color="#1e293b",
            callback_event="nav_click",
            callback_payload={"section": "Geospatial Data"}
        )
        sidebar_block.map(
            element_id="nav_item_2",
            tooltip="Chart View",
            hover_color="#1e293b",
            callback_event="nav_click",
            callback_payload={"section": "Quadrant Analytics"}
        )
    except ValueError:
        pass # Ignore missing IDs if template is simpler

    dashboard.add_sivo_block(block_id="sidebar", sivo_app=sidebar_block, col_span=1)


    # ---------------------------------------------------------
    # Block 2: Generated GeoDataFrame Map (from_geodataframe)
    # ---------------------------------------------------------
    # Let's mock a simple map block using Shapely polygons
    p1 = Polygon([(0, 0), (0, 10), (10, 10), (10, 0)])
    p2 = Polygon([(10, 0), (10, 10), (20, 10), (20, 0)])
    p3 = Polygon([(0, 10), (0, 20), (10, 20), (10, 10)])

    gdf = gpd.GeoDataFrame({
        "id": ["ZoneA", "ZoneB", "ZoneC"],
        "name": ["North Region", "East Region", "South Region"],
        "value": [100, 250, 50],
        "geometry": [p1, p2, p3]
    })

    geo_block = Sivo.from_geodataframe(gdf, id_col="id", name_col="name")

    # Map a choropleth color scale natively to the regions
    data_map = {"ZoneA": 100, "ZoneB": 250, "ZoneC": 50}
    geo_block.apply_choropleth(data_map, min_color="#e0f2fe", max_color="#1e40af")

    # Bind detailed callback payloads to update the Details Panel when clicked
    geo_block.map(
        element_id="ZoneA",
        tooltip="North Region",
        callback_payload={"Region": "North", "Users": 100, "Status": "Active"}
    )
    geo_block.map(
        element_id="ZoneB",
        tooltip="East Region",
        callback_payload={"Region": "East", "Users": 250, "Status": "Warning"}
    )
    geo_block.map(
        element_id="ZoneC",
        tooltip="South Region",
        callback_payload={"Region": "South", "Users": 50, "Status": "Active"}
    )

    dashboard.add_sivo_block(block_id="geomap", sivo_app=geo_block, col_span=3)


    # ---------------------------------------------------------
    # Block 3: Four Quadrants Template (from_template)
    # ---------------------------------------------------------
    quad_grid_block = Sivo.from_template("dashboards/four_quadrants")

    # Render an ECharts bar chart directly onto Quadrant 1
    quad_grid_block.map_bar_chart(
        element_id="quadrant_1",
        title="Revenue by Quarter",
        categories=["Q1", "Q2", "Q3", "Q4"],
        data=[12000, 15000, 14000, 18000],
        color=["#3b82f6", "#10b981", "#f59e0b", "#ef4444"]
    )

    # Render an ECharts pie chart directly onto Quadrant 2
    quad_grid_block.map_pie_chart(
        element_id="quadrant_2",
        title="User Distribution",
        data=[
            {"name": "Mobile", "value": 400},
            {"name": "Desktop", "value": 300},
            {"name": "Tablet", "value": 200}
        ],
        color=["#6366f1", "#ec4899", "#14b8a6"]
    )

    quad_grid_block.map(
        element_id="quadrant_3",
        tooltip="Interactive Quadrant 3",
        hover_color="#f8fafc",
        callback_payload={"Region": "Q3", "Revenue": "$14,000", "Growth": "+5%"}
    )

    quad_grid_block.map(
        element_id="quadrant_4",
        tooltip="Interactive Quadrant 4",
        hover_color="#f8fafc",
        callback_payload={"Region": "Q4", "Revenue": "$18,000", "Growth": "+12%"}
    )

    dashboard.add_sivo_block(block_id="quadrants", sivo_app=quad_grid_block, col_span=2)


    # ---------------------------------------------------------
    # Block 4: Built-in Details & Metrics Panels
    # ---------------------------------------------------------
    # This panel will automatically catch ANY clicks from geo_block or quad_grid_block
    # that contain matching payload keys.
    dashboard.add_metrics_panel(
        block_id="kpi_metrics",
        title="Live Metrics",
        metrics=["Users", "Revenue", "Growth"],
        col_span=1
    )

    dashboard.add_details_panel(
        block_id="details_info",
        title="Selection Details",
        placeholder="Click any region or quadrant to see details...",
        col_span=1
    )

    # Output to HTML
    output_file = "output.html"
    dashboard.to_html(output_file)
    print(f"Successfully generated {output_file}")

if __name__ == "__main__":
    main()
