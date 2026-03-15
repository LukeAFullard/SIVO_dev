from sivo import Sivo
import os

def run():
    template_path = os.path.join(
        os.path.dirname(os.path.dirname(os.path.dirname(__file__))),
        "src", "sivo", "templates", "timeline_5_nodes_template.svg"
    )

    app = Sivo.from_svg(
        template_path,
        disable_zoom_controls=True,
        lock_canvas=True,
        theme="light"
    )

    header_md = """
    <div style='text-align: center; padding: 20px; font-family: -apple-system, sans-serif;'>
        <h1 style='margin: 0 0 10px 0; color: #0f172a; font-size: 32px;'>Company History</h1>
        <p style='margin: 0; color: #64748b; font-size: 16px;'>A detailed look at our <strong>journey</strong> from the start to present day.</p>
    </div>
    """
    app.add_overlay("header_area", header_md)

    # Iframe overlay
    app.add_overlay(
        "node_1_card",
        "<div style='padding: 10px; height: 100%; box-sizing: border-box;'><iframe width='100%' height='100%' src='https://example.com' frameborder='0' style='border-radius: 8px; border: 1px solid #e2e8f0;'></iframe></div>"
    )

    # Line chart overlay
    app.map_line_chart(
        element_id="node_2_card",
        title="Revenue Growth",
        categories=["2020", "2021", "2022"],
        data=[100, 200, 400],
        color="#10b981",
        smooth=True,
        tooltip="Revenue in millions"
    )

    node_3_md = """
    <div style='padding: 20px; font-family: sans-serif; display: flex; flex-direction: column; justify-content: center; height: 100%; box-sizing: border-box;'>
        <h3 style='margin: 0 0 8px 0; color: #3b82f6;'>Product Launch</h3>
        <p style='margin: 0; color: #475569; font-size: 14px; line-height: 1.5;'>
            Version 2.0 was officially released, achieving <strong>10k active users</strong> in the first month.
        </p>
    </div>
    """
    app.add_overlay("node_3_card", node_3_md)

    output_path = os.path.join(os.path.dirname(__file__), "05_timeline.html")
    app.to_html(output_path)
    print(f"Generated: {output_path}")

if __name__ == "__main__":
    run()
