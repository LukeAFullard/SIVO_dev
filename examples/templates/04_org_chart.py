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

    # Narrative: Tech Unicorn Leadership Structure
    app.fill_template_zone("text_hierarchy_details", "Tech Unicorn Hierarchy", font_size="100%", font_weight="800", color="#0f172a")

    # Tier 1 - CEO
    ceo_html = """
    <div style='width: 100%; height: 100%; box-sizing: border-box; container-type: size; display: flex; align-items: center; justify-content: center; flex-direction: column; padding-top: 10cqh;'>
        <img src='https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?auto=format&fit=crop&w=150&q=80' alt='CEO' style='border-radius: 50%; border: 3px solid white; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.3); width: 25cqw; height: 25cqw; object-fit: cover; margin-bottom: 2cqh;'/>
        <span style='color: white; font-family: sans-serif; font-size: 8cqw; font-weight: 800;'>Elena Rostova</span>
        <span style='color: #e2e8f0; font-family: sans-serif; font-size: 6cqw; font-weight: 600;'>CEO & Founder</span>
    </div>
    """
    app.add_overlay("poly-tier-1", ceo_html)

    # Tier 2 - C-Suite
    app.add_scalable_text("poly-tier-2", "C-Suite & EVP", font_size="15%", color="white", font_weight="800", align="center", vertical_align="middle")
    app.add_scalable_text("poly-tier-2", "CTO, CFO, COO", font_size="10%", color="#e2e8f0", font_weight="600", align="center", top="60%")

    # Tier 3 - Management
    app.add_scalable_text("poly-tier-3", "VP & Directors", font_size="12%", color="white", font_weight="800", align="center", vertical_align="middle")
    app.add_scalable_text("poly-tier-3", "Engineering, Product, Marketing", font_size="8%", color="#e2e8f0", font_weight="600", align="center", top="60%")

    # Tier 4 - Individual Contributors
    app.add_scalable_text("poly-tier-4", "Execution Teams (ICs)", font_size="10%", color="white", font_weight="800", align="center", vertical_align="middle")
    app.add_scalable_text("poly-tier-4", "1,200+ Global Employees driving innovation and daily operations", font_size="6%", color="#e2e8f0", font_weight="600", align="center", top="60%")


    # Info Panel Side Content
    app.add_scalable_text("info-panel-data", "Workforce Distribution", left="0%", top="0%", width="100%", height="10%", font_size="25%", font_weight="800", color="#1e293b")

    # Let's replace the bullet points with a bar chart showing department sizes
    app.map_bar_chart(
        element_id="info-panel-data",
        title="",
        categories=["Eng", "Sales", "Prod", "Mktg", "HR"],
        data=[650, 300, 150, 80, 20],
        color="#3b82f6",
        extra_options={
            "grid": {"top": 60, "bottom": 30, "left": 40, "right": 20},
            "backgroundColor": "transparent"
        }
    )

    output_path = os.path.join(os.path.dirname(__file__), "04_org_chart.html")
    app.to_html(output_path)
    print(f"Generated: {output_path}")

if __name__ == "__main__":
    run()