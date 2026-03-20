import os
from sivo import Sivo

def main():
    # 1. Initialize Sivo with a standard SVG template
    # We will use the bento grid template to demonstrate a background that peers through
    app = Sivo.from_svg(
        os.path.join("src", "sivo", "templates", "bento_grid_template.svg"),
        title="Bento Grid with Astronomical Background"
    )

    # 2. Add some dummy interactions to demonstrate standard functionality
    app.map("bento-hero-data", tooltip="Primary metric overview.")
    app.map("bento-metric-1-data", tooltip="Secondary metric breakdown.")
    app.map("bento-sidebar-data", tooltip="Geospatial distribution.")
    app.map("bento-main-chart-data", tooltip="Performance analysis.")

    # 3. Add the new background image feature
    # A beautiful public domain astronomy image from NASA/Unsplash as a dramatic backdrop
    bg_url = "https://images.unsplash.com/photo-1462331940025-496dfbfc7564?q=80&w=2000&auto=format&fit=crop"

    # We apply opacity to make it subtle and set grayscale=True for a styled look
    app.add_background_image(bg_url, opacity=0.8, grayscale=True)

    # 4. Save the interactive HTML
    output_path = os.path.join(os.path.dirname(__file__), "index.html")
    app.to_html(output_path)
    print(f"Generated example at {output_path}")

if __name__ == "__main__":
    main()
