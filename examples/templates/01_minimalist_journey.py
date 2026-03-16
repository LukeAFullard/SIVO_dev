from sivo import Sivo
import os

def run():
    template_path = os.path.join(
        os.path.dirname(os.path.dirname(os.path.dirname(__file__))),
        "src", "sivo", "templates", "minimalist_journey_flow_2026.svg"
    )

    app = Sivo.from_svg(
        template_path,
        disable_zoom_controls=False,
        lock_canvas=True,
        theme="light"
    )

    # Header
    app.fill_template_zone("header-subtitle-placeholder", "E-Commerce Pipeline", font_size="100%", color="#94a3b8")
    app.fill_template_zone("header-title-placeholder", "Customer Acquisition Flow", font_size="100%", font_weight="800", color="#f8fafc")

    # Node 1
    app.fill_template_zone("node-1-step-placeholder", "1. Awareness", font_size="80%", font_weight="600", color="#1e293b", align="left")

    # Text injected natively using the upgraded auto-wrapping add_scalable_text
    app.add_scalable_text(
        "node-1-card",
        text="STRATEGY",
        left="10%", top="35%", width="80%", height="20%", font_size="14%", font_weight="800", color="#3b82f6"
    )
    app.add_scalable_text(
        "node-1-card",
        text="Launch targeted ads across social media and major search engines.",
        left="10%", top="55%", width="80%", height="50%", font_size="10%", font_weight="normal", color="#64748b"
    )

    # Node 2 - Native ECharts Bar Chart
    app.fill_template_zone("node-2-step-placeholder", "2. Acquisition", font_size="80%", font_weight="600", color="#1e293b", align="left")

    app.map_bar_chart(
        element_id="node-2-card",
        title="Traffic Sources",
        categories=["Ads", "Org", "Ref"],
        data=[100, 40, 20],
        color="#3b82f6",
        title_size=20,
        extra_options={"grid": {"top": 40, "bottom": 20, "left": 30, "right": 20}}
    )

    # Node 3 - Native Scalable Text
    app.fill_template_zone("node-3-step-placeholder", "3. Conversion", font_size="80%", font_weight="600", color="#1e293b", align="left")

    app.add_scalable_text("node-3-card", "CONVERSION RATE", left="0%", top="30%", width="100%", height="20%", font_size="12%", font_weight="700", color="#64748b", align="center")
    app.add_scalable_text("node-3-card", "4.2%", left="0%", top="60%", width="100%", height="40%", font_size="35%", font_weight="800", color="#10b981", align="center")

    output_path = os.path.join(os.path.dirname(__file__), "01_minimalist_journey.html")
    app.to_html(output_path)
    print(f"Generated: {output_path}")

if __name__ == "__main__":
    run()
