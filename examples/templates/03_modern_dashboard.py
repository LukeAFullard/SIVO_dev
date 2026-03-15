from sivo import Sivo
import os

def run():
    template_path = os.path.join(
        os.path.dirname(os.path.dirname(os.path.dirname(__file__))),
        "src", "sivo", "templates", "gis_digital_twin_dashboard_2026.svg"
    )

    with open(template_path, 'r') as f:
        svg_content = f.read()

    # We will inject a placeholder rect into chart-predictive to use for mapping charts
    svg_content = svg_content.replace(
        '<g id="chart-predictive">',
        '<g id="chart-predictive"><rect id="predictive-chart-zone" x="50" y="550" width="280" height="200" fill="transparent" />'
    )
    svg_content = svg_content.replace(
        '<text id="text_real_time_sensor_feeds" x="70" y="190" class="header" font-size="18"></text>',
        '<rect id="text_real_time_sensor_feeds" x="70" y="170" width="200" height="25" fill="transparent" />'
    )

    temp_path = os.path.join(os.path.dirname(__file__), "temp_gis.svg")
    with open(temp_path, "w") as f:
        f.write(svg_content)

    app = Sivo.from_svg(
        temp_path,
        disable_zoom_controls=True,
        lock_canvas=True,
        theme="dark"
    )

    app.fill_template_zone("text_real_time_sensor_feeds", "Real-Time Sensor Feeds", font_size=18, font_weight="600", color="#ffffff")

    app.map_line_chart(
        element_id="predictive-chart-zone",
        title="Predictive Metrics",
        categories=["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
        data=[120, 132, 101, 134, 90, 230],
        panel_position="right",
        tooltip="Predictive data over time"
    )

    md_html = """
    <div style='width: 100%; height: 100%; box-sizing: border-box; container-type: inline-size; display: flex; flex-direction: column; justify-content: center; background: rgba(30,41,59,0.8); border: 1px solid #334155; border-radius: 2cqw; padding: 4cqw; color: #f1f5f9; font-family: sans-serif; backdrop-filter: blur(8px);'>
        <h4 style='margin: 0 0 2cqh 0; color: #38bdf8; font-size: clamp(12px, 6cqw, 24px);'>Analysis</h4>
        <p style='margin: 0; font-size: clamp(10px, 4.5cqw, 20px); line-height: 1.4;'>System identified <strong>3 anomalies</strong> in the Q2 predictive cycle. Recommend manual override.</p>
    </div>
    """
    app.add_overlay(
        "predictive-chart-zone",
        md_html
    )

    output_path = os.path.join(os.path.dirname(__file__), "03_modern_dashboard.html")
    app.to_html(output_path)

    os.remove(temp_path)
    print(f"Generated: {output_path}")

if __name__ == "__main__":
    run()
