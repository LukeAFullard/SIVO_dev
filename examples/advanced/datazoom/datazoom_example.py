import os
import random
import math
from sivo.core.sivo import Sivo
from sivo.core.infographic import Infographic

# Generate a large dataset for demonstration
data = []
for i in range(1000):
    x = i
    y = math.sin(i / 10.0) * 100 + random.uniform(-10, 10)
    data.append([x, y])

# Create an empty SVG canvas programmatically
svg_string = """
<svg width="800" height="600" xmlns="http://www.w3.org/2000/svg">
    <rect id="chart-container" width="100%" height="100%" fill="#f9f9f9" />
</svg>
"""

# Initialize Sivo
app = Sivo.from_string(svg_string, theme="light")

# Map a Scatter Chart to the container, explicitly enabling datazoom
app.map_scatter_chart(
    element_id="chart-container",
    title="High-Density Scatter with DataZoom",
    data=data,
    color="#43a2ca",
    tooltip="Value: {c}",
    datazoom=True,
    extra_options={
        "xAxis": {"type": "value", "scale": True},
        "yAxis": {"type": "value", "scale": True}
    }
)

# Output dynamically to the script's directory
output_path = os.path.join(os.path.dirname(__file__), "output.html")
app.to_html(output_path)

print(f"Generated datazoom example at: {output_path}")
