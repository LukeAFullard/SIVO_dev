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

    # Add native SVG elements to the first card (System Status) instead of HTML overlay
    # This ensures perfect fluid scaling at all zoom levels using the new add_scalable_text helper
    app.add_scalable_text("rect-users", "System Status", left="10%", top="20%", width="80%", height="20%", font_size="15%", font_weight="700", color="#1e293b")
    app.add_scalable_text("rect-users", "All primary servers are operating at", left="10%", top="45%", width="80%", height="15%", font_size="10%", color="#64748b")
    app.add_scalable_text("rect-users", "99.99% uptime.", left="10%", top="60%", width="80%", height="15%", font_size="10%", font_weight="700", color="#10b981")

    # Native SVG Progress Bar using the new scalable progress bar method
    app.add_scalable_progress_bar("rect-users", progress="99.9%", left="10%", top="80%", width="80%", height="5%", rx="6")

    # Add an image overlay to the second card using the new add_image_overlay helper
    app.add_image_overlay(
        "rect-conversion",
        image_url="https://images.unsplash.com/photo-1551288049-bebda4e38f71?auto=format&fit=crop&w=800&q=80",
        border_radius="24px",
        box_shadow="inset 0 4px 6px -1px rgba(0,0,0,0.1)"
    )

    # Main map in main card. The `bBox` handles positioning natively over the <rect>
    app.map_nested_map_chart(
        element_id="card-main",
        title="Global Users",
        map_name="world",
        map_data="world", # Assuming world is built-in or needs separate loading, will just show map placeholder
        data=[{"name": "United States", "value": 100}],
        min_val=0,
        max_val=100,
        title_size=24,
        extra_options={"visualMap": {"show": False}}
    )

    # Add native SVG text to bottom cards using add_scalable_text
    # Card 1: Engagement
    app.add_scalable_text("card-engagement", "ENGAGEMENT", left="10%", top="20%", width="80%", height="20%", font_size="10%", font_weight="600", color="#94a3b8")
    app.add_scalable_text("card-engagement", "68%", left="10%", top="45%", width="80%", height="40%", font_size="30%", font_weight="800", color="#3b82f6")

    # Card 2: Bounce Rate
    app.add_scalable_text("card-bounce", "BOUNCE RATE", left="10%", top="20%", width="80%", height="20%", font_size="10%", font_weight="600", color="#94a3b8")
    app.add_scalable_text("card-bounce", "22%", left="10%", top="45%", width="80%", height="40%", font_size="30%", font_weight="800", color="#ef4444")

    # Card 3: Satisfaction
    app.add_scalable_text("card-satisfaction", "SATISFACTION", left="10%", top="20%", width="80%", height="20%", font_size="10%", font_weight="600", color="#94a3b8")
    app.add_scalable_text("card-satisfaction", "4.8/5", left="10%", top="45%", width="80%", height="40%", font_size="30%", font_weight="800", color="#10b981")

    output_path = os.path.join(os.path.dirname(__file__), "02_bento_grid.html")
    app.to_html(output_path)
    print(f"Generated: {output_path}")

if __name__ == "__main__":
    run()
