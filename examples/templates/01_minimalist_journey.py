from sivo import Sivo
import os

def run():
    template_path = os.path.join(
        os.path.dirname(os.path.dirname(os.path.dirname(__file__))),
        "src", "sivo", "templates", "minimalist_journey_flow_2026.svg"
    )

    app = Sivo.from_svg(
        template_path,
        disable_zoom_controls=True,
        lock_canvas=True,
        theme="light"
    )

    # Header
    app.fill_template_zone("header-subtitle-placeholder", "E-Commerce Pipeline", font_size=14, color="#94a3b8")
    app.fill_template_zone("header-title-placeholder", "Customer Acquisition Flow", font_size=36, font_weight="800", color="#0f172a")

    # Node 1
    app.fill_template_zone("node-1-step-placeholder", "1. Awareness", font_size=20, font_weight="600", color="#1e293b", align="left")

    # Text overlay formatted professionally using Markdown-like content
    markdown_html = """
    <div style='font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; max-width: 200px;'>
        <h4 style='margin: 0 0 8px 0; color: #3b82f6; font-size: 14px; text-transform: uppercase; letter-spacing: 0.5px;'>Strategy</h4>
        <p style='margin: 0; color: #64748b; font-size: 13px; line-height: 1.5;'>
            Launch targeted ads across <b>social media</b> and major search engines.
        </p>
    </div>
    """

    app.add_overlay(
        "node-1-desc-1-placeholder",
        markdown_html,
        offset_y=30,
        offset_x=20
    )

    # Bar chart overlay bound to node-2-step-placeholder
    app.map_bar_chart(
        element_id="node-2-step-placeholder",
        title="Traffic Sources",
        categories=["Ad Spend", "Organic", "Referral"],
        data=[500, 200, 100],
        panel_position="right",
        tooltip="Click to view breakdown",
        color="#3b82f6"
    )

    output_path = os.path.join(os.path.dirname(__file__), "01_minimalist_journey.html")
    app.to_html(output_path)
    print(f"Generated: {output_path}")

if __name__ == "__main__":
    run()
