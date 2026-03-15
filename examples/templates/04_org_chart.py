from sivo import Sivo
import os
import lxml.etree as etree

def run():
    template_path = os.path.join(
        os.path.dirname(os.path.dirname(os.path.dirname(__file__))),
        "src", "sivo", "templates", "pyramid_hierarchy_template.svg"
    )

    with open(template_path, 'r') as f:
        svg_content = f.read()

    # We will add id to the polygons
    svg_content = svg_content.replace('<polygon class="pyramid-tier tier-1"', '<polygon id="poly-tier-1" class="pyramid-tier tier-1"')
    svg_content = svg_content.replace('<polygon class="pyramid-tier tier-2"', '<polygon id="poly-tier-2" class="pyramid-tier tier-2"')
    svg_content = svg_content.replace('<text id="text_tier_1" class="tier-text" x="250" y="160"></text>', '<rect id="text_tier_1" x="200" y="140" width="100" height="30" fill="transparent"/>')

    temp_path = os.path.join(os.path.dirname(__file__), "temp_pyramid.svg")
    with open(temp_path, "w") as f:
        f.write(svg_content)

    app = Sivo.from_svg(
        temp_path,
        disable_zoom_controls=True,
        lock_canvas=True,
        theme="light"
    )

    app.fill_template_zone("text_tier_1", "CEO", font_size=24, font_weight="700", color="#ffffff", align="center")

    md_html = """
    <div style='width: 100%; height: 100%; box-sizing: border-box; container-type: inline-size; display: flex; align-items: center; justify-content: center;'>
        <img src='https://i.pravatar.cc/100' alt='CEO' style='border-radius: 50%; border: 3px solid white; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.3); width: 25cqw; height: 25cqw; max-width: 60px; max-height: 60px; object-fit: cover;'/>
    </div>
    """
    app.add_overlay(
        "poly-tier-1",
        md_html
    )

    app.add_overlay(
        "poly-tier-2",
        "<div style='width: 100%; height: 100%; box-sizing: border-box; container-type: inline-size; display: flex; align-items: flex-start; justify-content: center; padding-top: 2cqw;'><span style='color: white; font-family: sans-serif; font-size: clamp(14px, 4cqw, 24px); font-weight: 600;'>VPs & Directors</span></div>"
    )

    markdown_side = """
    <div style='width: 100%; height: 100%; box-sizing: border-box; container-type: inline-size; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; padding: 5cqw; display: flex; flex-direction: column; justify-content: center;'>
        <h1 style='color: #1e293b; margin: 0 0 2cqh 0; font-size: clamp(18px, 8cqw, 36px);'>Corporate Structure</h1>
        <p style='color: #475569; font-size: clamp(12px, 4.5cqw, 20px); line-height: 1.6; margin: 0 0 2cqh 0;'>
            The pyramid visualizes the <strong>decision-making hierarchy</strong> within the organization.
            The executive tier makes strategic calls, while management handles execution.
        </p>
        <ul style='color: #64748b; font-size: clamp(12px, 4.5cqw, 20px); line-height: 1.8; margin: 0; padding-left: 5cqw;'>
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

    os.remove(temp_path)
    print(f"Generated: {output_path}")

if __name__ == "__main__":
    run()
