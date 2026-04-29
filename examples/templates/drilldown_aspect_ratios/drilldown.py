import os
from sivo.core.project import SivoProject
from sivo.core.sivo import Sivo

def run():
    # 1. 1:1 Aspect Ratio (Home View)
    home_app = Sivo.from_template(
        "1_1/large_node_to_4_nodes",
        layout_size="95%",
        disable_zoom_controls=False,
        lock_zoom_out=True,
        default_panel_position="overlay",
        panel_width="90%",
        panel_height="90%",
    )

    # Customize 1:1 Home View
    # Note: large_node_to_4_nodes.svg doesn't have a 'header_area' ID natively, so we'll just map the start node and 4 cards

    home_app.add_scalable_text("large_node_dot", "SIVO\nLayout\nTest", left="-100%", top="-100%", width="300%", height="300%", align="center", font_size="30%", font_weight="bold", color="#1e293b")

    # Add text to cards for nodes. Due to `pointer-events: none` on the text, it will not block drilldown.
    home_app.add_scalable_text("node_1_card", "Click to Drilldown:\n3:2 Aspect Ratio", left="0%", top="0%", width="100%", height="100%", align="center", font_size="30%", color="#1e293b")
    home_app.add_scalable_text("node_2_card", "Click to Drilldown:\n4:3 Aspect Ratio", left="0%", top="0%", width="100%", height="100%", align="center", font_size="30%", color="#1e293b")
    home_app.add_scalable_text("node_3_card", "Click to Drilldown:\n16:10 Aspect Ratio", left="0%", top="0%", width="100%", height="100%", align="center", font_size="30%", color="#1e293b")
    home_app.add_scalable_text("node_4_card", "Click to Drilldown:\n4:7 Mobile Layout", left="0%", top="0%", width="100%", height="100%", align="center", font_size="30%", color="#1e293b")


    # Map directly to the original cards without needing new overlapping shapes.
    home_app.map("node_1_card", drill_to="view_3_2", tooltip="Drilldown to a 3:2 layout.", hover_color="rgba(0,0,0,0.05)", glow=True)
    home_app.map("node_2_card", drill_to="view_4_3", tooltip="Drilldown to a 4:3 layout.", hover_color="rgba(0,0,0,0.05)", glow=True)
    home_app.map("node_3_card", drill_to="view_16_10", tooltip="Drilldown to a 16:10 layout.", hover_color="rgba(0,0,0,0.05)", glow=True)
    home_app.map("node_4_card", drill_to="view_4_7", tooltip="Drilldown to a 4:7 Mobile layout.", hover_color="rgba(0,0,0,0.05)", glow=True)

    # 2. 3:2 Aspect Ratio View
    app_3_2 = Sivo.from_template(
        "3_2/bento_grid_template",
        layout_size="95%",
        lock_zoom_out=True,
        default_panel_position="overlay",
        panel_width="90%",
        panel_height="90%",
    )
    app_3_2.fill_template_zone("text_hero_insight_section", "3:2 Aspect Ratio Layout - Click to return")
    # For <g> elements like bento-hero, we still map directly to an explicit inner rect for ECharts compatibility
    app_3_2.add_shape("rect", {
        "id": "bento-hero-click-area",
        "x": "40",
        "y": "40",
        "width": "740",
        "height": "240",
        "fill": "transparent",
        "rx": "24"
    })
    app_3_2.map("bento-hero-click-area", drill_to="home", tooltip="Go back home", glow=True, hover_color="rgba(0,0,0,0.05)")

    # 3. 4:3 Aspect Ratio View
    app_4_3 = Sivo.from_template(
        "4_3/sleek_bento_grid_2026",
        layout_size="95%",
        lock_zoom_out=True,
        default_panel_position="overlay",
        panel_width="90%",
        panel_height="90%",
    )
    app_4_3.fill_template_zone("dash_title", "4:3 Aspect Ratio Layout")
    app_4_3.fill_template_zone("dash_subtitle", "Click background to return home")
    # Map to the existing base background rect that ECharts can interact with
    app_4_3.map("background", drill_to="home", tooltip="Go back home", hover_color="#e2e8f0", glow=True)

    # 4. 16:10 Aspect Ratio View
    app_16_10 = Sivo.from_template(
        "16_10/gis_digital_twin_dashboard_2026",
        layout_size="95%",
        lock_zoom_out=True,
        default_panel_position="overlay",
        panel_width="90%",
        panel_height="90%",
    )
    app_16_10.fill_template_zone("text_global_operations_digital_twin", "16:10 Aspect Ratio Layout", color="#ffffff")
    app_16_10.fill_template_zone("text_live_telemetry_from_deployed_assets", "Click map area to return home", color="#94a3b8")
    app_16_10.map("map-container-main", drill_to="home", tooltip="Go back home", hover_color="#334155", glow=True)

    # 5. 4:7 Mobile Portrait Aspect Ratio View
    app_4_7 = Sivo.from_template(
        "4_7/mobile_app_dashboard_2026",
        layout_size="95%",
        lock_zoom_out=True,
        default_panel_position="overlay",
        panel_width="90%",
        panel_height="90%",
    )
    app_4_7.fill_template_zone("mobile-hero-text-zone", "Tap Here to Go Home", font_size="50%", color="#64748b", align="center")
    # The text has pointer-events: none, so clicks pass down to the card
    app_4_7.map("mobile-hero-card", drill_to="home", tooltip="Go back home", hover_color="rgba(0,0,0,0.05)", glow=True)


    # Build Project
    project = SivoProject(initial_view_id="home")
    project.add_view("home", home_app)
    project.add_view("view_3_2", app_3_2)
    project.add_view("view_4_3", app_4_3)
    project.add_view("view_16_10", app_16_10)
    project.add_view("view_4_7", app_4_7)

    # Output
    output_path = os.path.join(os.path.dirname(__file__), "drilldown_aspect_ratios.html")
    project.to_html(output_path)
    print(f"Generated test file: {output_path}")

if __name__ == "__main__":
    run()
