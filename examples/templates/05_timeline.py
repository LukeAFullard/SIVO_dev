from sivo import Sivo
import os

def run():
    template_path = os.path.join(
        os.path.dirname(os.path.dirname(os.path.dirname(__file__))),
        "src", "sivo", "templates", "timeline_5_nodes_template.svg"
    )

    app = Sivo.from_svg(
        template_path,
        disable_zoom_controls=False,
        lock_canvas=True,
        theme="light"
    )

    app.add_scalable_text(
        "header_area",
        "COMPANY HISTORY",
        left="0%", top="30%", width="100%", height="20%", font_size="25%", font_weight="800", color="#0f172a", align="center"
    )
    app.add_scalable_text(
        "header_area",
        "A detailed look at our journey from the start to present day.",
        left="0%", top="60%", width="100%", height="20%", font_size="15%", color="#64748b", align="center"
    )

    # Image overlay using the new add_image_overlay helper
    app.add_image_overlay(
        "node_1_card",
        image_url="https://images.unsplash.com/photo-1556761175-4b46a572b786?auto=format&fit=crop&w=400&q=80",
        border_radius="1cqw"
    )

    # Line chart overlay - make title larger and hide axes to fit the small card better
    app.map_line_chart(
        element_id="node_2_card",
        title="Revenue",
        categories=["2020", "2021", "2022"],
        data=[100, 200, 400],
        color="#10b981",
        smooth=True,
        tooltip="Revenue in millions",
        title_size=24,
        extra_options={"xAxis": {"show": False}, "yAxis": {"show": False}, "grid": {"top": 30, "bottom": 10, "left": 10, "right": 10}}
    )

    app.add_scalable_text(
        "node_3_card",
        "Product Launch",
        left="10%", top="20%", width="80%", height="20%", font_size="20%", font_weight="800", color="#3b82f6"
    )
    app.add_scalable_text(
        "node_3_card",
        "Version 2.0 was officially released, achieving 10k active users.",
        left="10%", top="50%", width="80%", height="40%", font_size="14%", color="#475569"
    )

    app.add_scalable_text(
        "node_4_card",
        "Global Expansion",
        left="10%", top="20%", width="80%", height="20%", font_size="20%", font_weight="800", color="#f59e0b"
    )
    app.add_scalable_text(
        "node_4_card",
        "Opened offices in London and Tokyo.",
        left="10%", top="50%", width="80%", height="40%", font_size="14%", color="#475569"
    )

    app.add_scalable_text(
        "node_5_card",
        "Series C Funding",
        left="10%", top="20%", width="80%", height="20%", font_size="20%", font_weight="800", color="#10b981"
    )
    app.add_scalable_text(
        "node_5_card",
        "Raised $50M to scale operations.",
        left="10%", top="50%", width="80%", height="40%", font_size="14%", color="#475569"
    )

    output_path = os.path.join(os.path.dirname(__file__), "05_timeline.html")
    app.to_html(output_path)
    print(f"Generated: {output_path}")

if __name__ == "__main__":
    run()
