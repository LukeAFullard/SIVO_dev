from sivo import Sivo
import os

def run():
    template_path = os.path.join(
        os.path.dirname(os.path.dirname(os.path.dirname(__file__))),
        "src", "sivo", "templates", "gis_digital_twin_dashboard_2026.svg"
    )

    app = Sivo.from_svg(
        template_path,
        disable_zoom_controls=False,
        lock_canvas=True,
        theme="dark"
    )

    # Fill native empty text node directly
    app.fill_template_zone("text_global_operations_digital_twin", "Global Operations Digital Twin", font_size=24, font_weight="700", color="#f8fafc")
    app.fill_template_zone("text_real_time_sensor_feeds", "Real-Time Sensor Feeds", font_size=18, font_weight="600", color="#ffffff")
    app.fill_template_zone("text_system_alerts", "System Alerts", font_size=18, font_weight="600", color="#ffffff")

    # Add overlays to metrics
    app.add_overlay("metric-iot-1", "<div style='width: 100%; height: 100%; box-sizing: border-box; container-type: size; padding: 4cqw; display: flex; flex-direction: column; justify-content: center;'><span style='color:#94a3b8; font-size:12cqh;'>Power Output</span><span style='color:#10b981; font-size:24cqh; font-weight:bold;'>1.21 GW</span></div>")
    app.add_overlay("metric-iot-2", "<div style='width: 100%; height: 100%; box-sizing: border-box; container-type: size; padding: 4cqw; display: flex; flex-direction: column; justify-content: center;'><span style='color:#94a3b8; font-size:12cqh;'>Core Temp</span><span style='color:#f59e0b; font-size:24cqh; font-weight:bold;'>82°C</span></div>")
    app.add_overlay("metric-iot-3", "<div style='width: 100%; height: 100%; box-sizing: border-box; container-type: size; padding: 4cqw; display: flex; flex-direction: column; justify-content: center;'><span style='color:#94a3b8; font-size:12cqh;'>Efficiency</span><span style='color:#3b82f6; font-size:24cqh; font-weight:bold;'>94.5%</span></div>")

    app.map_line_chart(
        element_id="predictive-chart-zone",
        title="Predictive Metrics",
        categories=["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
        data=[120, 132, 101, 134, 90, 230],
        panel_position="right",
        tooltip="Predictive data over time"
    )

    # Scalable Markdown
    md_html = """
    <div style='width: 100%; height: 100%; box-sizing: border-box; container-type: size; display: flex; flex-direction: column; justify-content: center; background: rgba(30,41,59,0.8); border: 1px solid #334155; border-radius: 2cqw; padding: 4cqw; color: #f1f5f9; font-family: sans-serif; backdrop-filter: blur(8px);'>
        <h4 style='margin: 0 0 2cqh 0; color: #38bdf8; font-size: 8cqw;'>Analysis</h4>
        <p style='margin: 0; font-size: 6cqw; line-height: 1.4;'>System identified <strong>3 anomalies</strong> in the Q2 predictive cycle. Recommend manual override.</p>
    </div>
    """
    app.add_overlay(
        "predictive-chart-zone",
        md_html
    )

    output_path = os.path.join(os.path.dirname(__file__), "03_modern_dashboard.html")
    app.to_html(output_path)
    print(f"Generated: {output_path}")

if __name__ == "__main__":
    run()
