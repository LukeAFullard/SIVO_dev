from sivo import Sivo
import os
import lxml.etree as etree

def run():
    template_path = os.path.join(
        os.path.dirname(os.path.dirname(os.path.dirname(__file__))),
        "src", "sivo", "templates", "bento_grid_dashboard_2026.svg"
    )

    with open(template_path, 'r') as f:
        svg_content = f.read()

    # We will just create a new temporary SVG file with rect ids that match exactly the positions of the cards
    # Looking at the original: <rect x="680" y="160" width="460" height="180" class="card" />
    svg_content = svg_content.replace('<rect x="680" y="160" width="460" height="180" class="card" />', '<rect id="rect-users" x="680" y="160" width="460" height="180" class="card" />')
    svg_content = svg_content.replace('<rect x="680" y="360" width="460" height="180" class="card" />', '<rect id="rect-conversion" x="680" y="360" width="460" height="180" class="card" />')

    # For text, replace the empty <text> tag with a placeholder rect
    svg_content = svg_content.replace('<text id="text_performance_overview" x="60" y="80" class="title"></text>', '<rect id="text_performance_overview" x="60" y="50" width="300" height="40" fill="transparent" />')

    temp_path = os.path.join(os.path.dirname(__file__), "temp_bento.svg")
    with open(temp_path, "w") as f:
        f.write(svg_content)

    app = Sivo.from_svg(
        temp_path,
        disable_zoom_controls=True,
        lock_canvas=True,
        theme="light"
    )

    # Use fill_template_zone on the rect placeholder
    app.fill_template_zone("text_performance_overview", "Global Performance", font_size=28, font_weight="800", color="#0f172a")

    # Add a markdown overlay inside the first card (x=680, width=460)
    md_html = """
    <div style='background: white; padding: 24px; border-radius: 12px; font-family: sans-serif;'>
        <h3 style='margin:0 0 12px 0; color: #1e293b;'>System Status</h3>
        <p style='margin:0; color: #64748b; font-size: 14px;'>All primary servers are operating at <strong>99.99%</strong> uptime.</p>
    </div>
    """
    app.add_overlay(
        "rect-users",
        md_html,
        offset_y=20
    )

    # Add an image overlay to the second card
    image_html = """
    <div style='padding: 20px;'>
        <img src='https://images.unsplash.com/photo-1551288049-bebda4e38f71?auto=format&fit=crop&w=400&q=80' alt='Data Center' style='border-radius: 12px; width: 100%; height: 140px; object-fit: cover; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1);' />
    </div>
    """
    app.add_overlay(
        "rect-conversion",
        image_html,
        offset_y=0
    )

    output_path = os.path.join(os.path.dirname(__file__), "02_bento_grid.html")
    app.to_html(output_path)

    # Cleanup temp
    os.remove(temp_path)
    print(f"Generated: {output_path}")

if __name__ == "__main__":
    run()
