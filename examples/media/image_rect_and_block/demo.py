import os
from sivo.core.sivo import Sivo
from sivo.core.dashboard import SivoDashboard

def main():
    # Example Image URLs (Using unsplash placeholders for demo)
    image_url_1 = "https://images.unsplash.com/photo-1550684848-fac1c5b4e853?q=80&w=1200&auto=format&fit=crop"
    image_url_2 = "https://images.unsplash.com/photo-1518770660439-4636190af475?q=80&w=1200&auto=format&fit=crop"

    # --- 1. Demonstrate add_image_rect on a SIVO SVG Canvas ---
    # Create a basic blank 16:9 canvas
    svg_canvas = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1600 900"></svg>'
    sivo_app = Sivo.from_string(svg_canvas, title="Image Rect Demo")

    # Add an image rectangle that takes up 50% width and 100% height on the left
    sivo_app.add_image_rect("left_image", image_url_1, x="0", y="0", width="50%", height="100%", preserve_aspect_ratio="xMidYMid slice")

    # Add an image rectangle that takes up 50% width and 100% height on the right
    sivo_app.add_image_rect("right_image", image_url_2, x="50%", y="0", width="50%", height="100%", preserve_aspect_ratio="xMidYMid slice")

    # Add some text over the images
    sivo_app.add_shape("text", {"id": "title", "x": "50%", "y": "10%", "font-size": "64", "font-weight": "bold", "fill": "white", "text-anchor": "middle"})
    sivo_app.map("title", markdown="## Native SVG Images\nThese images are rendered via `<image>` tags natively on the vector canvas.")

    # --- 2. Demonstrate add_image_block in a Dashboard ---
    # Create a dashboard with 3 columns
    dashboard = SivoDashboard(title="Image Helpers Dashboard", columns=3, theme="neo_brutalism")

    # Define a layout
    dashboard.set_grid_layout(
        desktop="""
        "hero hero hero"
        "img1 sivo img2"
        """,
        mobile="""
        "hero"
        "img1"
        "sivo"
        "img2"
        """
    )

    # Add a title block
    dashboard.add_html_block(
        "hero",
        "<div style='padding: 2rem; text-align: center; background: var(--primary-color); color: white; border-radius: 8px;'><h1>Image Helpers Demo</h1><p>Demonstrating add_image_block and add_image_rect</p></div>",
        grid_area="hero"
    )

    # Add standard Image Blocks (Option A) to the dashboard grid
    dashboard.add_image_block("img1", image_url_1, object_fit="cover", grid_area="img1")
    dashboard.add_image_block("img2", image_url_2, object_fit="cover", grid_area="img2")

    # Add the interactive SIVO block (Option B) containing native SVG image rectangles
    dashboard.add_sivo_block("sivo", sivo_app, grid_area="sivo")

    # Save the output
    output_path = os.path.join(os.path.dirname(__file__), "output.html")
    dashboard.to_html(output_path)
    print(f"✅ Generated demo at {output_path}")

if __name__ == "__main__":
    main()
