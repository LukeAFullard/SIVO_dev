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
        disable_zoom_controls=True,
        lock_canvas=True,
        theme="light"
    )

    # Inject into the existing <text id="text_performance_overview"> natively
    app.fill_template_zone("text_performance_overview", "Global Performance", font_size=28, font_weight="800", color="#0f172a")

    # Add a markdown overlay inside the first card (x=680, width=460) using pure CQW
    md_html = """
    <div style='width: 100%; height: 100%; box-sizing: border-box; container-type: inline-size; display: flex; flex-direction: column; justify-content: center; background: white; padding: 5cqw; border-radius: 2cqw; font-family: sans-serif;'>
        <h3 style='margin:0 0 3cqh 0; color: #1e293b; font-size: 6cqw;'>System Status</h3>
        <p style='margin:0; color: #64748b; font-size: 4cqw;'>All primary servers are operating at <strong>99.99%</strong> uptime.</p>
    </div>
    """
    app.add_overlay(
        "rect-users",
        md_html
    )

    # Add an image overlay to the second card
    image_html = """
    <div style='width: 100%; height: 100%; box-sizing: border-box; container-type: inline-size; padding: 4cqw;'>
        <img src='https://images.unsplash.com/photo-1551288049-bebda4e38f71?auto=format&fit=crop&w=400&q=80' alt='Data Center' style='border-radius: 2cqw; width: 100%; height: 100%; object-fit: cover; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1);' />
    </div>
    """
    app.add_overlay(
        "rect-conversion",
        image_html
    )

    output_path = os.path.join(os.path.dirname(__file__), "02_bento_grid.html")
    app.to_html(output_path)
    print(f"Generated: {output_path}")

if __name__ == "__main__":
    run()
