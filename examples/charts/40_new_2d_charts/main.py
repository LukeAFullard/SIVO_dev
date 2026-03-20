import os
from sivo import Sivo

def main():
    sivo_app = Sivo.from_svg(
        os.path.join(os.path.dirname(__file__), "grid.svg"),
        title="New 2D ECharts Wrappers",
        subtitle="Click any box to view the corresponding advanced ECharts visualization"
    )

    # 1. Boxplot
    sivo_app.map_boxplot_chart(
        element_id="box1",
        title="Monthly Revenue Distribution",
        categories=["Jan", "Feb", "Mar", "Apr"],
        data=[
            [850, 880, 940, 960, 1020], # [min, Q1, median, Q3, max]
            [800, 850, 900, 940, 980],
            [900, 920, 950, 980, 1050],
            [920, 950, 980, 1020, 1100]
        ],
        color="#38bdf8",
        tooltip="View Boxplot"
    )

    # 2. Candlestick (K-Line)
    sivo_app.map_candlestick_chart(
        element_id="box2",
        title="Stock Performance",
        categories=["2023-10-01", "2023-10-02", "2023-10-03", "2023-10-04"],
        data=[
            [20, 34, 10, 38], # [open, close, lowest, highest]
            [40, 35, 30, 50],
            [31, 38, 33, 44],
            [38, 15, 5, 42]
        ],
        item_color="#ef4444",   # Red for up
        item_color0="#10b981",  # Green for down
        tooltip="View Candlestick"
    )

    # 3. Cartesian Heatmap
    # Generate simple 3x3 grid data [x, y, value]
    heatmap_data = [[i, j, (i*10 + j*5)] for i in range(3) for j in range(3)]
    sivo_app.map_heatmap_chart(
        element_id="box3",
        title="Activity Heatmap",
        x_categories=["Morning", "Afternoon", "Evening"],
        y_categories=["Mon", "Tue", "Wed"],
        data=heatmap_data,
        color=["#f8fafc", "#bae6fd", "#38bdf8", "#0284c7", "#0f172a"],
        tooltip="View Heatmap"
    )

    # 4. Graph (Network Force Layout)
    nodes = [{"name": "A", "symbolSize": 50}, {"name": "B", "symbolSize": 30}, {"name": "C", "symbolSize": 40}]
    links = [{"source": "A", "target": "B"}, {"source": "A", "target": "C"}, {"source": "B", "target": "C"}]
    sivo_app.map_graph_chart(
        element_id="box4",
        title="Network Graph",
        nodes=nodes,
        links=links,
        layout="force",
        color="#8b5cf6",
        tooltip="View Force Graph"
    )

    # 5. Sankey Diagram
    sankey_nodes = [{"name": "Start"}, {"name": "Path 1"}, {"name": "Path 2"}, {"name": "End"}]
    sankey_links = [
        {"source": "Start", "target": "Path 1", "value": 60},
        {"source": "Start", "target": "Path 2", "value": 40},
        {"source": "Path 1", "target": "End", "value": 50},
        {"source": "Path 2", "target": "End", "value": 30}
    ]
    sivo_app.map_sankey_chart(
        element_id="box5",
        title="User Flow Sankey",
        nodes=sankey_nodes,
        links=sankey_links,
        tooltip="View Sankey"
    )

    # 6. Sunburst
    sunburst_data = [{
        "name": "Global",
        "value": 100,
        "children": [
            {"name": "Americas", "value": 40, "children": [{"name": "North", "value": 30}, {"name": "South", "value": 10}]},
            {"name": "EMEA", "value": 60, "children": [{"name": "Europe", "value": 40}, {"name": "Africa", "value": 20}]}
        ]
    }]
    sivo_app.map_sunburst_chart(
        element_id="box6",
        title="Hierarchy Sunburst",
        data=sunburst_data,
        tooltip="View Sunburst"
    )

    # 7. Parallel Coordinates
    schema = [
        {"dim": 0, "name": "Price"},
        {"dim": 1, "name": "Weight"},
        {"dim": 2, "name": "Speed", "type": "category", "data": ["Low", "Med", "High"]}
    ]
    parallel_data = [
        [100, 50, "High"],
        [200, 30, "Med"],
        [50, 80, "Low"]
    ]
    sivo_app.map_parallel_chart(
        element_id="box7",
        title="Product Comparison",
        schema=schema,
        data=parallel_data,
        color="#f59e0b",
        tooltip="View Parallel Coordinates"
    )

    # 8. Theme River (Streamgraph)
    # Data: [date, value, category]
    river_data = [
        ["2023-01", 10, "A"], ["2023-02", 20, "A"], ["2023-03", 15, "A"],
        ["2023-01", 15, "B"], ["2023-02", 10, "B"], ["2023-03", 30, "B"]
    ]
    sivo_app.map_theme_river_chart(
        element_id="box8",
        title="Market Share Stream",
        data=river_data,
        legend_data=["A", "B"],
        tooltip="View ThemeRiver"
    )

    # Make them interactive on hover
    for i in range(1, 9):
        sivo_app.map(f"box{i}", hover_color="#cbd5e1", glow=True)


    output_path = os.path.join(os.path.dirname(__file__), "output.html")
    sivo_app.to_html(output_path)
    print(f"Generated advanced charts example at {output_path}")

if __name__ == "__main__":
    main()
