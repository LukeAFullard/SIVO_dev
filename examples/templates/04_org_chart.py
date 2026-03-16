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
    app.fill_template_zone("text_hierarchy_details", "Hierarchy Details", font_size="100%", font_weight="800", color="#f8fafc")

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

    app.add_scalable_text(
        "poly-tier-2",
        "Executives",
        font_size="25%",
        color="white",
        font_weight="700",
        align="center",
        vertical_align="middle"
    )

    app.add_scalable_text(
        "poly-tier-3",
        "Middle Management",
        font_size="20%",
        color="white",
        font_weight="700",
        align="center",
        vertical_align="middle"
    )

    app.add_scalable_text(
        "poly-tier-4",
        "Operations & Staff",
        font_size="20%",
        color="white",
        font_weight="700",
        align="center",
        vertical_align="middle"
    )

    app.add_scalable_text(
        "info-panel-data",
        "Corporate Structure",
        left="5%", top="5%", width="90%", height="10%",
        font_size="10%",
        font_weight="800",
        color="#1e293b"
    )

    app.add_scalable_text(
        "info-panel-data",
        "The pyramid visualizes the decision-making hierarchy within the organization. The executive tier makes strategic calls, while management handles execution.",
        left="5%", top="20%", width="90%", height="40%",
        font_size="4%",
        color="#475569"
    )

    app.add_scalable_text(
        "info-panel-data",
        "• Tier 1: Executive Board\n• Tier 2: Management\n• Tier 3: Team Leads\n• Tier 4: Operations",
        left="5%", top="60%", width="90%", height="35%",
        font_size="4%",
        color="#64748b"
    )

    output_path = os.path.join(os.path.dirname(__file__), "04_org_chart.html")
    app.to_html(output_path)
    print(f"Generated: {output_path}")

if __name__ == "__main__":
    run()
