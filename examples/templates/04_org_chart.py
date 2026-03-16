from sivo import Sivo
import os
import lxml.etree as etree

def run():
    template_path = os.path.join(
        os.path.dirname(os.path.dirname(os.path.dirname(__file__))),
        "src", "sivo", "templates", "pyramid_hierarchy_template.svg"
    )

    app = Sivo.from_svg(
        template_path,
        disable_zoom_controls=False,
        lock_canvas=True,
        theme="light"
    )

    # Use native text replacement without overwriting SVG logic
    app.fill_template_zone("text_hierarchy_details", "Hierarchy Details", font_size=28, font_weight="800", color="#0f172a")

    md_html = """
    <div style='width: 100%; height: 100%; box-sizing: border-box; container-type: size; display: flex; align-items: center; justify-content: center; flex-direction: column;'>
        <img src='https://i.pravatar.cc/100' alt='CEO' style='border-radius: 50%; border: 3px solid white; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.3); width: 35cqw; height: 35cqw; object-fit: cover; margin-bottom: 2cqh;'/>
        <span style='color: white; font-family: sans-serif; font-size: 16cqw; font-weight: 700;'>CEO</span>
    </div>
    """

    app.add_overlay(
        "poly-tier-1",
        md_html
    )

    app.add_overlay(
        "poly-tier-2",
        "<div style='width: 100%; height: 100%; box-sizing: border-box; container-type: size; display: flex; align-items: center; justify-content: center;'><span style='color: white; font-family: sans-serif; font-size: 10cqw; font-weight: 700;'>Executives</span></div>"
    )

    app.add_overlay(
        "poly-tier-3",
        "<div style='width: 100%; height: 100%; box-sizing: border-box; container-type: size; display: flex; align-items: center; justify-content: center;'><span style='color: white; font-family: sans-serif; font-size: 8cqw; font-weight: 700;'>Middle Management</span></div>"
    )

    app.add_overlay(
        "poly-tier-4",
        "<div style='width: 100%; height: 100%; box-sizing: border-box; container-type: size; display: flex; align-items: center; justify-content: center;'><span style='color: white; font-family: sans-serif; font-size: 8cqw; font-weight: 700;'>Operations & Staff</span></div>"
    )

    markdown_side = """
    <div style='width: 100%; height: 100%; box-sizing: border-box; container-type: size; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; padding: 5cqw; display: flex; flex-direction: column; justify-content: center;'>
        <h1 style='color: #1e293b; margin: 0 0 2cqh 0; font-size: 10cqw;'>Corporate Structure</h1>
        <p style='color: #475569; font-size: 6cqw; line-height: 1.6; margin: 0 0 2cqh 0;'>
            The pyramid visualizes the <strong>decision-making hierarchy</strong> within the organization.
            The executive tier makes strategic calls, while management handles execution.
        </p>
        <ul style='color: #64748b; font-size: 6cqw; line-height: 1.8; margin: 0; padding-left: 5cqw;'>
            <li><b>Tier 1:</b> Executive Board</li>
            <li><b>Tier 2:</b> Management</li>
            <li><b>Tier 3:</b> Team Leads</li>
            <li><b>Tier 4:</b> Operations</li>
        </ul>
    </div>
    """

    app.add_overlay(
        "info-panel-data",
        markdown_side
    )

    output_path = os.path.join(os.path.dirname(__file__), "04_org_chart.html")
    app.to_html(output_path)
    print(f"Generated: {output_path}")

if __name__ == "__main__":
    run()
