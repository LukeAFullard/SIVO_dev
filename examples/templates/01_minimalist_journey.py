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
    app.fill_template_zone("header-subtitle-placeholder", "E-Commerce Pipeline", font_size=14, color="#94a3b8")
    app.fill_template_zone("header-title-placeholder", "Customer Acquisition Flow", font_size=36, font_weight="800", color="#0f172a")

    # Node 1
    app.fill_template_zone("node-1-step-placeholder", "1. Awareness", font_size=20, font_weight="600", color="#1e293b", align="left")

    # Text overlay formatted professionally using Markdown-like content
    # Binding to the proper large bounding box (node-1-card), not a tiny single text line
    # Using pure cqw/cqh or % for fluid scaling, preventing overflow on small bounds.
    markdown_html = """
    <div style='width: 100%; height: 100%; box-sizing: border-box; container-type: size; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; display: flex; flex-direction: column; justify-content: center; padding: 8cqw;'>
        <h4 style='margin: 0 0 4cqh 0; color: #3b82f6; font-size: 10cqw; text-transform: uppercase; letter-spacing: 0.5px;'>Strategy</h4>
        <p style='margin: 0; color: #64748b; font-size: 8cqw; line-height: 1.5;'>
            Launch targeted ads across <br><b>social media</b> and major <br>search engines.
        </p>
    </div>
    """

    app.add_overlay(
        "node-1-card",
        markdown_html
    )

    # Node 2 - ECharts Bar Chart directly in overlay
    app.fill_template_zone("node-2-step-placeholder", "2. Acquisition", font_size=20, font_weight="600", color="#1e293b", align="left")

    chart_html = """
    <div style='width: 100%; height: 100%; box-sizing: border-box; container-type: size; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; padding: 4cqw;'>
        <div style='width: 100%; height: 100%; display: flex; flex-direction: column;'>
            <h4 style='margin: 0 0 2cqh 0; color: #1e293b; font-size: 8cqw;'>Traffic Sources</h4>
            <div style='flex: 1; position: relative;'>
                <div style='position: absolute; bottom: 0; left: 0; width: 100%; height: 80%; display: flex; align-items: flex-end; justify-content: space-around; padding: 0 2cqw;'>
                    <div style='width: 25%; height: 100%; background: #3b82f6; border-radius: 4px 4px 0 0;'></div>
                    <div style='width: 25%; height: 40%; background: #60a5fa; border-radius: 4px 4px 0 0;'></div>
                    <div style='width: 25%; height: 20%; background: #93c5fd; border-radius: 4px 4px 0 0;'></div>
                </div>
            </div>
            <div style='display: flex; justify-content: space-around; margin-top: 2cqh; font-size: 5cqw; color: #64748b;'>
                <span>Ads</span><span>Org</span><span>Ref</span>
            </div>
        </div>
    </div>
    """

    app.add_overlay(
        "node-2-card",
        chart_html
    )

    # Node 3
    app.fill_template_zone("node-3-step-placeholder", "3. Conversion", font_size=20, font_weight="600", color="#1e293b", align="left")

    conversion_html = """
    <div style='width: 100%; height: 100%; box-sizing: border-box; container-type: size; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; display: flex; flex-direction: column; justify-content: center; padding: 8cqw; align-items: center; text-align: center;'>
        <h4 style='margin: 0; color: #64748b; font-size: 8cqw; text-transform: uppercase;'>Conversion Rate</h4>
        <p style='margin: 2cqh 0 0 0; color: #10b981; font-size: 24cqw; font-weight: 800;'>
            4.2%
        </p>
    </div>
    """
    app.add_overlay(
        "node-3-card",
        conversion_html
    )

    output_path = os.path.join(os.path.dirname(__file__), "01_minimalist_journey.html")
    app.to_html(output_path)
    print(f"Generated: {output_path}")

if __name__ == "__main__":
    run()
