import os
import sys

# Ensure SIVO is importable from the local source for this example
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src')))

from sivo import Sivo
from sivo.core.config import ProjectConfig, ElementConfig
import random

def create_example():
    # 1. Create a simple SVG to act as our "dashboard map"
    svg_content = """
    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 300">
        <rect width="400" height="300" fill="#f0f4f8" />

        <g id="race_trigger_button" transform="translate(100, 100)" cursor="pointer">
            <rect width="200" height="60" rx="10" fill="#3b82f6" />
            <text x="100" y="35" font-family="sans-serif" font-size="18" fill="white" text-anchor="middle" font-weight="bold">
                Show Sales Bar Race
            </text>
            <text x="100" y="50" font-family="sans-serif" font-size="12" fill="#e2e8f0" text-anchor="middle">
                (Click to open side panel)
            </text>
        </g>
    </svg>
    """

    svg_path = os.path.join(os.path.dirname(__file__), "dashboard.svg")
    with open(svg_path, "w") as f:
        f.write(svg_content)

    # 2. Define the ECharts configuration for a Bar Race
    # Note: In a real-time web application, you would update this data dynamically via custom_js.
    # For a static export, ECharts provides a `dataset` and `timeline` component to simulate a race natively.
    # Here we build a native ECharts timeline configuration that auto-plays a bar race.

    years = ['2019', '2020', '2021', '2022', '2023']
    brands = ['Brand A', 'Brand B', 'Brand C', 'Brand D']

    options = []

    # Generate some random cumulative data for the race
    current_values = {b: random.randint(10, 50) for b in brands}

    for year in years:
        # Add random growth
        for b in brands:
            current_values[b] += random.randint(5, 40)

        # Sort and take top 4
        sorted_data = sorted([{"name": b, "value": current_values[b]} for b in brands], key=lambda x: x["value"])

        options.append({
            "title": {"text": f"Global Sales - {year}"},
            "series": [
                {
                    "data": [item["value"] for item in sorted_data],
                    "realtimeSort": True,
                }
            ],
            "yAxis": {
                "data": [item["name"] for item in sorted_data]
            }
        })

    bar_race_option = {
        "baseOption": {
            "timeline": {
                "axisType": 'category',
                "autoPlay": True,
                "playInterval": 1500,
                "data": years,
                "label": {"formatter": '{value}'}
            },
            "title": {
                "subtext": "Animated Bar Race built with ECharts"
            },
            "tooltip": {"trigger": "axis"},
            "xAxis": {
                "type": 'value',
                "name": 'Sales ($)'
            },
            "yAxis": {
                "type": 'category',
                "inverse": True, # High values at the top
                "animationDuration": 300,
                "animationDurationUpdate": 300,
                "max": 3 # Show top 4
            },
            "series": [
                {
                    "realtimeSort": True,
                    "name": 'Sales',
                    "type": 'bar',
                    "itemStyle": {
                        "color": "#10b981"
                    },
                    "label": {
                        "show": True,
                        "position": 'right',
                        "valueAnimation": True
                    }
                }
            ],
            "animationDuration": 0,
            "animationDurationUpdate": 1500,
            "animationEasing": 'linear',
            "animationEasingUpdate": 'linear'
        },
        "options": options
    }

    # 3. Create the Sivo configuration
    config = ProjectConfig(
        svg_file=svg_path,
        default_panel_position="right",
        mappings={
            "race_trigger_button": ElementConfig(
                tooltip="Open Race Chart",
                echarts_option=bar_race_option,
                hover_color="#2563eb",
                glow=True,
                panel_position="right",
                open_by_default=True
            )
        }
    )

    # 4. Generate the interactive HTML
    app = Sivo.from_config(config, base_dir=os.path.dirname(__file__))

    output_path = os.path.join(os.path.dirname(__file__), "bar_race.html")
    app.to_html(output_path)
    print(f"Generated Bar Race example at {output_path}")

if __name__ == "__main__":
    create_example()
