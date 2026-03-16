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
    app.fill_template_zone("text_global_operations_digital_twin", "Global Operations Digital Twin", font_size="100%", font_weight="700", color="#f8fafc")
    app.fill_template_zone("text_real_time_sensor_feeds", "Real-Time Sensor Feeds", font_size="100%", font_weight="600", color="#ffffff")
    app.fill_template_zone("text_system_alerts", "System Alerts", font_size="100%", font_weight="600", color="#ffffff")

    # Add overlays to metrics using scalable text instead of HTML
    app.add_scalable_text("metric-iot-1", "Power Output", left="5%", top="20%", width="90%", height="30%", font_size="20%", font_weight="normal", color="#94a3b8", align="left")
    app.add_scalable_text("metric-iot-1", "1.21 GW", left="5%", top="50%", width="90%", height="40%", font_size="40%", font_weight="bold", color="#10b981", align="left")

    app.add_scalable_text("metric-iot-2", "Core Temp", left="5%", top="20%", width="90%", height="30%", font_size="20%", font_weight="normal", color="#94a3b8", align="left")
    app.add_scalable_text("metric-iot-2", "82°C", left="5%", top="50%", width="90%", height="40%", font_size="40%", font_weight="bold", color="#f59e0b", align="left")

    app.add_scalable_text("metric-iot-3", "Efficiency", left="5%", top="20%", width="90%", height="30%", font_size="20%", font_weight="normal", color="#94a3b8", align="left")
    app.add_scalable_text("metric-iot-3", "94.5%", left="5%", top="50%", width="90%", height="40%", font_size="40%", font_weight="bold", color="#3b82f6", align="left")

    # Change to a heatmap to make the dashboard look cooler
    app.map_heatmap_chart(
        element_id="predictive-chart-zone",
        title="Predictive Metrics",
        x_categories=["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
        y_categories=["Alpha", "Beta", "Gamma"],
        data=[[0,0,10], [0,1,20], [0,2,30], [1,0,40], [1,1,50], [1,2,60], [2,0,70], [2,1,80], [2,2,90], [3,0,100], [3,1,110], [3,2,120], [4,0,130], [4,1,140], [4,2,150], [5,0,160], [5,1,170], [5,2,180]],
        color=["#0f172a", "#3b82f6", "#38bdf8"],
        title_color="#ffffff",
        axis_color="#94a3b8",
        extra_options={
            "grid": {"top": 40, "bottom": 30, "left": 50, "right": 20},
            "visualMap": {"show": False}
        }
    )

    output_path = os.path.join(os.path.dirname(__file__), "03_modern_dashboard.html")
    app.to_html(output_path)
    print(f"Generated: {output_path}")

if __name__ == "__main__":
    run()
