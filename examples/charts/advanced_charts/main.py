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

        <rect id="radar_chart" x="500" y="300" width="250" height="200" fill="#f1f5f9" stroke="#cbd5e1" stroke-width="2" rx="10"/>
        <text x="625" y="400" font-family="sans-serif" font-size="20" font-weight="bold" fill="#334155" text-anchor="middle">Radar Chart</text>
    </svg>
    """

    # 1. Initialize Sivo orchestrator
    app = Sivo.from_string(
        svg_string,
        title="Advanced Chart Types",
        subtitle="Exploring Polar, Liquid Fill, and Radar charts natively in SIVO",
        disable_zoom_controls=True,
        panel_width="40%",
        default_panel_position="right"
    )

    # Let's map the general theme options like hover_color independently using base app.map
    app.map("polar_bar", hover_color="#e2e8f0", open_by_default=True)
    app.map("polar_line", hover_color="#e2e8f0")
    app.map("polar_scatter", hover_color="#e2e8f0")
    app.map("liquid_fill", hover_color="#e2e8f0")
    app.map("radar_chart", hover_color="#e2e8f0")

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

    # 6. Map Radar Chart
    radar_indicators = [
        {"name": "Sales", "max": 6500},
        {"name": "Administration", "max": 16000},
        {"name": "Information Technology", "max": 30000},
        {"name": "Customer Support", "max": 38000},
        {"name": "Development", "max": 52000},
        {"name": "Marketing", "max": 25000}
    ]
    radar_data = [
        {
            "value": [4200, 3000, 20000, 35000, 50000, 18000],
            "name": "Allocated Budget"
        },
        {
            "value": [5000, 14000, 28000, 26000, 42000, 21000],
            "name": "Actual Spending"
        }
    ]
    app.map_radar_chart(
        element_id="radar_chart",
        title="Budget vs Spending",
        indicators=radar_indicators,
        data=radar_data,
        color=["#f59e0b", "#10b981"]
    )

    # Export the bundle
    output_path = os.path.join(os.path.dirname(__file__), "output.html")
    app.to_html(output_path)
    print(f"Successfully generated: {output_path}")

if __name__ == "__main__":
    main()
