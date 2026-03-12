from sivo import ProjectConfig, Sivo
import json

config = ProjectConfig(svg_file="examples/01_hello_world/sample.svg")
app = Sivo.from_config(config)

data = [
    [1, 1],
    [2, 3],
    [3, 2],
    [4, 5],
    [5, 4],
    [6, 7],
    [7, 6],
    [8, 9]
]

app.map_trendline_chart(
    element_id="sun",
    title="Test Trendline",
    data=data,
    trendline_type="linear",
    trendline_color="green",
    trendline_width=4,
    trendline_arrow=True,
    color="blue"
)

html = app.to_html("test_trendline.html")
print("Done")
