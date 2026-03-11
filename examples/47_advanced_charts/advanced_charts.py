import os
from sivo import Sivo

def main():
    # A simple SVG layout
    svg_string = """
    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 600">
        <!-- Interactive Elements -->
        <rect id="polar_bar" x="50" y="50" width="250" height="200" fill="#f1f5f9" stroke="#cbd5e1" stroke-width="2" rx="10"/>
        <text x="175" y="150" font-family="sans-serif" font-size="20" font-weight="bold" fill="#334155" text-anchor="middle">Polar Bar Chart</text>

        <rect id="polar_line" x="350" y="50" width="250" height="200" fill="#f1f5f9" stroke="#cbd5e1" stroke-width="2" rx="10"/>
        <text x="475" y="150" font-family="sans-serif" font-size="20" font-weight="bold" fill="#334155" text-anchor="middle">Polar Line Chart</text>

        <rect id="polar_scatter" x="650" y="50" width="250" height="200" fill="#f1f5f9" stroke="#cbd5e1" stroke-width="2" rx="10"/>
        <text x="775" y="150" font-family="sans-serif" font-size="20" font-weight="bold" fill="#334155" text-anchor="middle">Polar Scatter Chart</text>

        <rect id="liquid_fill" x="200" y="300" width="250" height="200" fill="#f1f5f9" stroke="#cbd5e1" stroke-width="2" rx="10"/>
        <text x="325" y="400" font-family="sans-serif" font-size="20" font-weight="bold" fill="#334155" text-anchor="middle">Liquid Fill Chart</text>

        <rect id="custom_series" x="500" y="300" width="250" height="200" fill="#f1f5f9" stroke="#cbd5e1" stroke-width="2" rx="10"/>
        <text x="625" y="400" font-family="sans-serif" font-size="20" font-weight="bold" fill="#334155" text-anchor="middle">Custom Series</text>
    </svg>
    """

    # 1. Initialize Sivo orchestrator
    app = Sivo.from_string(
        svg_string,
        title="Advanced Chart Types",
        subtitle="Exploring Polar, Liquid Fill, and Custom Series natively in SIVO",
        disable_zoom_controls=True,
        panel_width="40%"
    )

    # Let's map the general theme options like hover_color independently using base app.map
    app.map("polar_bar", hover_color="#e2e8f0", open_by_default=True)
    app.map("polar_line", hover_color="#e2e8f0")
    app.map("polar_scatter", hover_color="#e2e8f0")
    app.map("liquid_fill", hover_color="#e2e8f0")
    app.map("custom_series", hover_color="#e2e8f0")

    # 2. Map Polar Bar Chart
    app.map_polar_bar_chart(
        element_id="polar_bar",
        title="Revenue by Region",
        data=[120, 200, 150, 80],
        categories=["North", "South", "East", "West"],
        color=["#38bdf8", "#818cf8", "#c084fc", "#e879f9"]
    )

    # 3. Map Polar Line Chart (e.g. for cyclical time-series data or math functions)
    import math
    # Generate data for a sine wave to plot around a circle
    math_data = [math.sin(i * math.pi / 180) * 10 for i in range(0, 360, 5)]
    app.map_polar_line_chart(
        element_id="polar_line",
        title="Cyclical Trends",
        data=math_data,
        color="#10b981"
    )

    # 4. Map Polar Scatter Chart
    app.map_polar_scatter_chart(
        element_id="polar_scatter",
        title="Distribution Map",
        # Data format for Polar Scatter: [radius, angle]
        data=[[10, 45], [20, 90], [15, 120], [30, 200], [25, 270], [5, 330]],
        color="#f59e0b",
        extra_options={
            "series": [{"symbolSize": 15}]
        }
    )

    # 5. Map Liquid Fill Chart (Requires echarts-liquidfill plugin, natively supported by SIVO HTML runtime)
    app.map_liquidfill_chart(
        element_id="liquid_fill",
        title="Water Reservoir Level",
        data=[0.6, 0.5, 0.4, 0.3], # Creates multiple waves at different percentage thresholds
        color=["#3b82f6", "#60a5fa", "#93c5fd", "#bfdbfe"],
        extra_options={
            "series": [{"outline": {"show": False}}]
        }
    )

    # 6. Map Custom Series (e.g. A Gantt Chart or specialized visualization)
    custom_render_js = """
    function (params, api) {
        var categoryIndex = api.value(0);
        var start = api.coord([api.value(1), categoryIndex]);
        var end = api.coord([api.value(2), categoryIndex]);
        var height = api.size([0, 1])[1] * 0.6;
        var rectShape = echarts.graphic.clipRectByRect({
            x: start[0],
            y: start[1] - height / 2,
            width: end[0] - start[0],
            height: height
        }, {
            x: params.coordSys.x,
            y: params.coordSys.y,
            width: params.coordSys.width,
            height: params.coordSys.height
        });
        return rectShape && {
            type: 'rect',
            transition: ['shape'],
            shape: rectShape,
            style: api.style()
        };
    }
    """
    gantt_data = [
        # [category_index, start_val, end_val]
        {"name": "Task A", "value": [0, 10, 25], "itemStyle": {"color": "#ef4444"}},
        {"name": "Task B", "value": [1, 20, 45], "itemStyle": {"color": "#f97316"}},
        {"name": "Task C", "value": [2, 40, 60], "itemStyle": {"color": "#84cc16"}},
    ]
    app.map_custom_chart(
        element_id="custom_series",
        title="Project Timeline (Custom Gantt)",
        render_item_js=custom_render_js,
        data=gantt_data,
        extra_options={
            "xAxis": {"scale": True},
            "yAxis": {"data": ["Team 1", "Team 2", "Team 3"]},
            "tooltip": {
                "formatter": "function(params) { return params.name + ': ' + params.value[1] + ' to ' + params.value[2]; }"
            }
        }
    )

    # Export the bundle
    output_path = os.path.join(os.path.dirname(__file__), "advanced_charts.html")
    app.to_html(output_path)
    print(f"Successfully generated: {output_path}")

if __name__ == "__main__":
    main()
