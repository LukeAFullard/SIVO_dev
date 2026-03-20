import os
import random
from sivo import Sivo

# 1. Initialize SIVO with a basic SVG canvas
svg_string = """
<svg viewBox="0 0 800 600" xmlns="http://www.w3.org/2000/svg">
    <rect id="calendar_box" x="50" y="50" width="300" height="200" fill="#f0f0f0" stroke="#ccc" rx="10"/>
    <text x="200" y="150" font-family="sans-serif" font-size="20" text-anchor="middle" pointer-events="none">Click for Calendar Heatmap</text>

    <rect id="wordcloud_box" x="450" y="50" width="300" height="200" fill="#f0f0f0" stroke="#ccc" rx="10"/>
    <text x="600" y="150" font-family="sans-serif" font-size="20" text-anchor="middle" pointer-events="none">Click for Word Cloud</text>
</svg>
"""

sivo_app = Sivo.from_string(svg_string, default_panel_position="bottom")

# Generate some fake calendar data for 2017
calendar_data = []
for month in range(1, 13):
    for day in range(1, 29): # keeping it simple
        date_str = f"2017-{month:02d}-{day:02d}"
        calendar_data.append([date_str, random.randint(0, 1000)])

sivo_app.map_calendar_heatmap_chart(
    element_id="calendar_box",
    title="2017 Commit History",
    data=calendar_data,
    calendar_range="2017",
    tooltip="View full calendar heatmap"
)

# Generate some word cloud data
wordcloud_data = [
    {"name": "Python", "value": 1000},
    {"name": "Data Visualization", "value": 800},
    {"name": "SIVO", "value": 1200},
    {"name": "Infographics", "value": 600},
    {"name": "Interactive", "value": 900},
    {"name": "SVG", "value": 1100},
    {"name": "ECharts", "value": 850},
    {"name": "Streamlit", "value": 750},
    {"name": "Word Cloud", "value": 500},
    {"name": "Calendar", "value": 400},
    {"name": "Dashboard", "value": 300},
    {"name": "Components", "value": 200},
    {"name": "Maps", "value": 100},
    {"name": "Scrollytelling", "value": 150},
]

# We use a larger base64 string of a circle shape for the mask so the words have room to render
# Generated via a 400x400 PIL image with a black circle
large_mask_b64 = open("mask_b64.txt").read().strip()

sivo_app.map_word_cloud_chart(
    element_id="wordcloud_box",
    title="Topic Relevance (Circle Mask)",
    data=wordcloud_data,
    mask_image=large_mask_b64,
    tooltip="View full word cloud",
    extra_options={
        "series": [{
            "sizeRange": [10, 40], # Reduced size range to ensure words fit in the mask
            "textStyle": {}
        }],
        "color": ["#5470c6", "#91cc75", "#fac858", "#ee6666", "#73c0de", "#3ba272", "#fc8452", "#9a60b4", "#ea7ccc"]
    }
)


# 3. Export to HTML
output_file = os.path.join(os.path.dirname(__file__), 'output.html')
sivo_app.to_html(output_file)
print(f"Generated {output_file}. Open it in a browser to test.")