from sivo import Sivo
import os
import lxml.etree as etree

def run():
    template_path = os.path.join(
        os.path.dirname(os.path.dirname(os.path.dirname(__file__))),
        "src", "sivo", "templates", "bento_grid_dashboard_2026.svg"
    )

    # SIVO natively supports text placeholders and adding shapes without text/file replacement hacks
    app = Sivo.from_svg(
        template_path,
        disable_zoom_controls=False,
        lock_canvas=True,
        theme="light"
    )

    # Inject into the existing <text id="text_performance_overview"> natively
    app.fill_template_zone("text_performance_overview", "Global Performance", font_size=28, font_weight="800", color="#0f172a")

    # Add a markdown overlay inside the first card (x=680, width=460) using pure CQW
    md_html = """
    <div style='width: 100%; height: 100%; box-sizing: border-box; container-type: size; display: flex; flex-direction: column; justify-content: center; padding: 5cqw; font-family: sans-serif;'>
        <h3 style='margin:0 0 3cqh 0; color: #1e293b; font-size: 5.5cqw;'>System Status</h3>
        <p style='margin:0; color: #64748b; font-size: 3.5cqw; line-height: 1.5;'>All primary servers are operating at <strong>99.99%</strong> uptime. Routine maintenance completed with zero anomalies reported.</p>
        <div style='margin-top: 4cqh; width: 100%; background-color: #f1f5f9; border-radius: 2cqw; height: 3cqh; overflow: hidden;'>
             <div style='width: 99.99%; background-color: #10b981; height: 100%;'></div>
        </div>
    </div>
    """
    app.add_overlay(
        "rect-users",
        md_html
    )

    # Add an image overlay to the second card. Note the border-radius matching the SVG rx=24. (using pure percentages for border-radius scales better)
    image_html = """
    <div style='width: 100%; height: 100%; box-sizing: border-box; container-type: size; padding: 0;'>
        <img src='https://images.unsplash.com/photo-1551288049-bebda4e38f71?auto=format&fit=crop&w=800&q=80' alt='Data Center' style='border-radius: 24px; width: 100%; height: 100%; object-fit: cover; box-shadow: inset 0 4px 6px -1px rgba(0,0,0,0.1);' />
    </div>
    """
    app.add_overlay(
        "rect-conversion",
        image_html
    )

    # Main map in main card. The `bBox` handles positioning natively over the <rect>
    app.map_nested_map_chart(
        element_id="card-main",
        title="Global Users",
        map_name="world",
        map_data="world", # Assuming world is built-in or needs separate loading, will just show map placeholder
        data=[{"name": "United States", "value": 100}],
        min_val=0,
        max_val=100
    )

    # Add text to bottom cards
    app.add_overlay("card-engagement", "<div style='width: 100%; height: 100%; box-sizing: border-box; container-type: size; display: flex; flex-direction: column; justify-content: center; align-items: flex-start; padding: 10cqw;'><h4 style='margin:0; color: #64748b; font-size: 5cqw; text-transform: uppercase; letter-spacing: 1px;'>Engagement</h4><p style='margin: 1cqh 0 0 0; font-size: 12cqw; font-weight: 800; color: #3b82f6;'>68%</p></div>")
    app.add_overlay("card-bounce", "<div style='width: 100%; height: 100%; box-sizing: border-box; container-type: size; display: flex; flex-direction: column; justify-content: center; align-items: flex-start; padding: 10cqw;'><h4 style='margin:0; color: #64748b; font-size: 5cqw; text-transform: uppercase; letter-spacing: 1px;'>Bounce Rate</h4><p style='margin: 1cqh 0 0 0; font-size: 12cqw; font-weight: 800; color: #ef4444;'>22%</p></div>")
    app.add_overlay("card-satisfaction", "<div style='width: 100%; height: 100%; box-sizing: border-box; container-type: size; display: flex; flex-direction: column; justify-content: center; align-items: flex-start; padding: 10cqw;'><h4 style='margin:0; color: #64748b; font-size: 5cqw; text-transform: uppercase; letter-spacing: 1px;'>Satisfaction</h4><p style='margin: 1cqh 0 0 0; font-size: 12cqw; font-weight: 800; color: #10b981;'>4.8/5</p></div>")

    output_path = os.path.join(os.path.dirname(__file__), "02_bento_grid.html")
    app.to_html(output_path)
    print(f"Generated: {output_path}")

if __name__ == "__main__":
    run()
