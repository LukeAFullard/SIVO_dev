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
]

# We use extra_options to inject a color callback for the word cloud natively if we want,
# but echarts-wordcloud handles random colors by default if we don't specify textStyle.color.
# We use a base64 string of a simple black star shape for the mask
star_mask_b64 = "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADIAAAAyCAYAAAAeP4ixAAAAAXNSR0IArs4c6QAAArhJREFUaEPtWst2wjAMdZ4/0I2zY+es1L3//w+snO3G6IIGQhVInMQm0qWdE1uS7yPZ8uI44l+aC/xLFmRBgXw8Ho/9fr/VdV2b/1+S5GiaBvM8I1xL0/R9Pp/fI4hYgDzAbrfblGXJWZbBMAz4fD5gMpmw2rB5NptBHMffXdf9cBxnM4vInLIs+c1mA0VRyB/Qh2vKsgRVVQHruu9VVSXXbTYb115EZADzPF+yA7/fL6zXawwGA1BVFcIwBFmWWf+1Wq2grmuGf7FYsL5N13VRkiTvLJeYkI7jcD8MwyCEYfT7PWsM7/f7c1+w1+sBmqZ1d2EYMv/lcjkjG3wz2Qx2u11AkiTwPA+0Wq1O281mEyRJYn33+/3PPoH1eq25rst+q6oKu92OlS4WiwE1TTNEFhF01DQNer0ew+J5Howx9jEajUAURYbf7XYM8XQ6HdoB1nUd/rB932fXbDYbeL/f3w1yvV5Z3bVarR/7TNPwfd/M8xx2u927y6cR4bpuAId9g7ZcLu9gYRgGSqWSERQ/o6pqQkS4rhvx1Hq9ZgQeDgfot57nQbPZ7NyN2Ijj4+R5/tJ4PMYj4Z/I9/2nQ0aIf4pEItfRarWCIAicIPIhWq1WoFgsGvF4/K6RSI1Go+D1ev27K41EwslkEkwmkw9ycnMqlYKz2Yz1nUql4Hg8Hl5XFAr1ZlOpFFyv1+/06nQ6gA0M9gO2KwqF2kwmE7b+A0A2iZzP50+LXC6X7b/b7Yblcnl3QhAEXvJ4PB4kSeLEyI7j2DkchmF2dJvNpjt9l8sFIpFIRw4oimIH7vf77QnJ5XLsdwBgT00mk3dObrVaQaFQsAMx4r228iQSiYDD4bB7QhRFQbfbrROk2+0Co9H4621C/V14s9kEoVDIHiKfzyeXy+XbgcK8SiaTgcFgwHqLRCIQCoW6a/FwOKQv+P4fEQwGQS6Xs254NBqx/rLZLGy32x/Iu/sI7A1c1+1Yg02O0WgEgUDAv2nEbR1N02CaJltHMBiEVCp1a13X/b2+RSLRRCJBNs+2tN1uh0wmA71ez1qjYyN070xGCMsylMvtUj6fh1wuR/Y7X/eZ2ZGMkEAgkCqXyxAMBu0rVqvV72kOa8pmszQJk8mEvb1oZLPZ8Hw+fz2261yTjRDaWdM0sD1pNBq3z/99w3Q6DcFg8D316f+N7B/r51/L+l+yIL//B77L0Q8q+rYBAAAAAElFTkSuQmCC"

sivo_app.map_word_cloud_chart(
    element_id="wordcloud_box",
    title="Topic Relevance",
    data=wordcloud_data,
    mask_image=star_mask_b64,
    tooltip="View full word cloud",
    extra_options={
        "series": [{
            "textStyle": {
                # This string gets interpreted as JS by ECharts if we pass it through carefully,
                # but ECharts wordcloud actually handles random if color is omitted or we can just pass an array of colors via generic option color
            }
        }],
        "color": ["#5470c6", "#91cc75", "#fac858", "#ee6666", "#73c0de", "#3ba272", "#fc8452", "#9a60b4", "#ea7ccc"]
    }
)


# 3. Export to HTML
output_file = os.path.join(os.path.dirname(__file__), 'output.html')
sivo_app.to_html(output_file)
print(f"Generated {output_file}. Open it in a browser to test.")
