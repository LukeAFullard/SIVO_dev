import os
from sivo.core.project import SivoProject
from sivo.core.sivo import Sivo

def run():
    # 1. 1:1 Aspect Ratio (Home View)
    home_app = Sivo.from_svg(
        os.path.join(
            os.path.dirname(os.path.dirname(os.path.dirname(__file__))),
            "src", "sivo", "templates", "1_1", "large_node_to_3_nodes.svg"
        ),
        layout_size="98%",
        disable_zoom_controls=False,
    )

    # Customize 1:1 Home View
    home_app.add_scalable_text("header_area", "SIVO Layout Test: 1:1 Aspect Ratio (Home)", left="0%", top="0%", width="100%", height="100%", align="center", font_size="50%", font_weight="bold")

    home_app.add_scalable_text("large_node_dot", "START", left="-100%", top="-100%", width="300%", height="300%", align="center", font_size="50%", font_weight="bold", color="#1e293b")

    # Add text to cards for nodes
    home_app.add_scalable_text("node_1_card", "Click to Drilldown:\n3:2 Aspect Ratio", left="0%", top="0%", width="100%", height="100%", align="center", font_size="30%")
    home_app.add_scalable_text("node_2_card", "Click to Drilldown:\n4:3 Aspect Ratio", left="0%", top="0%", width="100%", height="100%", align="center", font_size="30%")
    home_app.add_scalable_text("node_3_card", "Click to Drilldown:\n16:10 Aspect Ratio", left="0%", top="0%", width="100%", height="100%", align="center", font_size="30%")

    home_app.map("node_1_card", drill_to="view_3_2", tooltip="Drilldown to a 3:2 layout.", hover_color="#f8fafc")
    home_app.map("node_2_card", drill_to="view_4_3", tooltip="Drilldown to a 4:3 layout.", hover_color="#f8fafc")
    home_app.map("node_3_card", drill_to="view_16_10", tooltip="Drilldown to a 16:10 layout.", hover_color="#f8fafc")

    # 2. 3:2 Aspect Ratio View
    app_3_2 = Sivo.from_svg(
        os.path.join(
            os.path.dirname(os.path.dirname(os.path.dirname(__file__))),
            "src", "sivo", "templates", "3_2", "bento_grid_template.svg"
        ),
        layout_size="98%"
    )
    app_3_2.fill_template_zone("text_hero_insight_section", "3:2 Aspect Ratio Layout")
    app_3_2.map("bento-hero", drill_to="home", tooltip="Go back home")

    # 3. 4:3 Aspect Ratio View
    app_4_3 = Sivo.from_svg(
        os.path.join(
            os.path.dirname(os.path.dirname(os.path.dirname(__file__))),
            "src", "sivo", "templates", "4_3", "sleek_bento_grid_2026.svg"
        ),
        layout_size="98%"
    )
    app_4_3.fill_template_zone("dash_title", "4:3 Aspect Ratio Layout")
    app_4_3.fill_template_zone("dash_subtitle", "Click to return home")
    app_4_3.map("background", drill_to="home", tooltip="Go back home")

    # 4. 16:10 Aspect Ratio View
    app_16_10 = Sivo.from_svg(
        os.path.join(
            os.path.dirname(os.path.dirname(os.path.dirname(__file__))),
            "src", "sivo", "templates", "16_10", "gis_digital_twin_dashboard_2026.svg"
        ),
        layout_size="98%"
    )
    app_16_10.fill_template_zone("text_global_operations_digital_twin", "16:10 Aspect Ratio Layout", color="#ffffff")
    app_16_10.fill_template_zone("text_live_telemetry_from_deployed_assets", "Click map area to return home", color="#94a3b8")
    app_16_10.map("map-container-main", drill_to="home", tooltip="Go back home")

    # Build Project
    project = SivoProject(initial_view_id="home")
    project.add_view("home", home_app)
    project.add_view("view_3_2", app_3_2)
    project.add_view("view_4_3", app_4_3)
    project.add_view("view_16_10", app_16_10)

    # Output
    output_path = os.path.join(os.path.dirname(__file__), "drilldown_aspect_ratios.html")
    project.to_html(output_path)
    print(f"Generated test file: {output_path}")

if __name__ == "__main__":
    run()
