from sivo import Sivo
import os

def build_journey_flow():
    template_path = os.path.join(
        os.path.dirname(os.path.dirname(os.path.dirname(__file__))),
        "src", "sivo", "templates", "minimalist_journey_flow_2026.svg"
    )
    output_dir = os.path.dirname(__file__)

    app = Sivo.from_svg(
        template_path,
        disable_zoom_controls=True,
        lock_canvas=True,
        theme="light"
    )

    app.apply_template_style("minimalist")

    # Header
    app.fill_template_zone("header-subtitle-placeholder", "E-Commerce Pipeline", font_size=14, font_weight="600", color="#94a3b8")
    app.fill_template_zone("header-title-placeholder", "Customer Acquisition Flow", font_size=36, font_weight="800", color="#0f172a")

    # Node 1
    app.fill_template_zone("node-1-step-placeholder", "1. Awareness", font_size=20, font_weight="600", color="#1e293b", align="center")
    app.fill_template_zone("node-1-desc-1-placeholder", "Social media campaigns", font_size=14, font_weight="400", color="#64748b", align="center")
    app.fill_template_zone("node-1-desc-2-placeholder", "and targeted ads.", font_size=14, font_weight="400", color="#64748b", align="center")

    # Node 2
    app.fill_template_zone("node-2-step-placeholder", "2. Consideration", font_size=20, font_weight="600", color="#1e293b", align="left")
    app.fill_template_zone("node-2-desc-1-placeholder", "Landing page engagement", font_size=14, font_weight="400", color="#64748b", align="left")
    app.fill_template_zone("node-2-desc-2-placeholder", "and product reviews.", font_size=14, font_weight="400", color="#64748b", align="left")

    # Node 3
    app.fill_template_zone("node-3-step-placeholder", "3. Conversion", font_size=20, font_weight="600", color="#1e293b", align="center")
    app.fill_template_zone("node-3-desc-1-placeholder", "Checkout flow completion", font_size=14, font_weight="400", color="#64748b", align="center")
    app.fill_template_zone("node-3-desc-2-placeholder", "and payment capture.", font_size=14, font_weight="400", color="#64748b", align="center")

    # Node 4
    app.fill_template_zone("node-4-step-placeholder", "4. Delivery", font_size=20, font_weight="600", color="#1e293b", align="left")
    app.fill_template_zone("node-4-desc-1-placeholder", "Order fulfillment and", font_size=14, font_weight="400", color="#64748b", align="left")
    app.fill_template_zone("node-4-desc-2-placeholder", "shipping tracking.", font_size=14, font_weight="400", color="#64748b", align="left")

    # Node 5
    app.fill_template_zone("node-5-step-placeholder", "5. Loyalty", font_size=20, font_weight="600", color="#1e293b", align="center")
    app.fill_template_zone("node-5-desc-1-placeholder", "Post-purchase follow-up", font_size=14, font_weight="400", color="#64748b", align="center")
    app.fill_template_zone("node-5-desc-2-placeholder", "and subscription.", font_size=14, font_weight="400", color="#64748b", align="center")

    # Interactive Map Funnel
    funnel_data = [
        {"value": 100, "name": "Awareness"},
        {"value": 75, "name": "Consideration"},
        {"value": 50, "name": "Conversion"},
        {"value": 45, "name": "Delivery"},
        {"value": 20, "name": "Loyalty"}
    ]

    app.map_funnel_chart(
        element_id="node-3-conversion",
        title="Overall Funnel Drop-off",
        data=funnel_data,
        color=["#e2e8f0", "#94a3b8", "#3b82f6", "#10b981", "#ec4899"],
        tooltip="Click to view step-by-step conversion funnel drop-off rates.",
        panel_position="right"
    )

    output_path = os.path.join(output_dir, "customer_journey.html")
    app.to_html(output_path)
    print(f"Generated: {output_path}")

if __name__ == "__main__":
    build_journey_flow()