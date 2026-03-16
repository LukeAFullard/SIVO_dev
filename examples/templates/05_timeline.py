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

    header_md = """
    <div style='width: 100%; height: 100%; box-sizing: border-box; container-type: size; display: flex; flex-direction: column; align-items: center; justify-content: center; padding: 2cqw; font-family: -apple-system, sans-serif; text-align: center;'>
        <h1 style='margin: 0 0 1cqh 0; color: #0f172a; font-size: 6cqw;'>Company History</h1>
        <p style='margin: 0; color: #64748b; font-size: 3cqw;'>A detailed look at our <strong>journey</strong> from the start to present day.</p>
    </div>
    """
    app.add_overlay("header_area", header_md)

    # Image overlay
    app.add_overlay(
        "node_1_card",
        "<div style='width: 100%; height: 100%; box-sizing: border-box; container-type: size; padding: 2cqw;'><img src='https://images.unsplash.com/photo-1556761175-4b46a572b786?auto=format&fit=crop&w=400&q=80' style='width: 100%; height: 100%; object-fit: cover; border-radius: 1cqw;'/></div>"
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

    node_3_md = """
    <div style='width: 100%; height: 100%; box-sizing: border-box; container-type: size; padding: 5cqw; font-family: sans-serif; display: flex; flex-direction: column; justify-content: center;'>
        <h3 style='margin: 0 0 2cqh 0; color: #3b82f6; font-size: 8cqw;'>Product Launch</h3>
        <p style='margin: 0; color: #475569; font-size: 5cqw; line-height: 1.5;'>
            Version 2.0 was officially released, achieving <strong>10k active users</strong>.
        </p>
    </div>
    """
    app.add_overlay("node_3_card", node_3_md)

    app.add_overlay("node_4_card", "<div style='width: 100%; height: 100%; box-sizing: border-box; container-type: size; padding: 5cqw; font-family: sans-serif; display: flex; flex-direction: column; justify-content: center;'><h3 style='margin: 0 0 2cqh 0; color: #f59e0b; font-size: 8cqw;'>Global Expansion</h3><p style='margin: 0; color: #475569; font-size: 5cqw; line-height: 1.5;'>Opened offices in London and Tokyo.</p></div>")
    app.add_overlay("node_5_card", "<div style='width: 100%; height: 100%; box-sizing: border-box; container-type: size; padding: 5cqw; font-family: sans-serif; display: flex; flex-direction: column; justify-content: center;'><h3 style='margin: 0 0 2cqh 0; color: #10b981; font-size: 8cqw;'>Series C Funding</h3><p style='margin: 0; color: #475569; font-size: 5cqw; line-height: 1.5;'>Raised <strong>$50M</strong>.</p></div>")

    output_path = os.path.join(os.path.dirname(__file__), "05_timeline.html")
    app.to_html(output_path)
    print(f"Generated: {output_path}")

if __name__ == "__main__":
    run()
