import os
from sivo.core.sivo import Sivo
from sivo.core.dashboard import SivoDashboard

def main():
    # Example Image URLs
    image_url_1 = "https://images.unsplash.com/photo-1550684848-fac1c5b4e853?q=80&w=1200&auto=format&fit=crop"
    image_url_2 = "https://images.unsplash.com/photo-1518770660439-4636190af475?q=80&w=1200&auto=format&fit=crop"

    # --- 1. Create a SIVO SVG Canvas ---
    svg_canvas = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1600 900"></svg>'
    sivo_app = Sivo.from_string(svg_canvas, title="Transparent Rect Demo")

    # Add an image rectangle that takes up half the canvas on the left
    sivo_app.add_image_rect("left_image", image_url_1, x="0", y="0", width="800", height="900", preserve_aspect_ratio="xMidYMid slice")

    # Add an image rectangle that takes up half the canvas on the right
    sivo_app.add_image_rect("right_image", image_url_2, x="800", y="0", width="800", height="900", preserve_aspect_ratio="xMidYMid slice")

    sivo_app.add_shape("text", {"id": "title", "x": "800", "y": "100", "font-size": "64", "font-weight": "bold", "fill": "white", "text-anchor": "middle"})
    sivo_app.map("title", markdown="## Native SVG Images")

    # --- 2. Create a Dashboard with "transparent" theme ---
    # The 'transparent' theme removes the card backgrounds, borders, and box shadows.
    dashboard = SivoDashboard(title="Transparent Image Helpers Dashboard", columns=3, theme="transparent")

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
        "<div style='padding: 2rem; text-align: center; background: rgba(0,0,0,0.8); color: white;'><h1>Transparent Dashboard Demo</h1><p>Notice the images have no rounded borders and the layout blocks have no card backgrounds.</p></div>",
        grid_area="hero"
    )

    # Add standard Image Blocks with 0px border radius
    dashboard.add_image_block("img1", image_url_1, object_fit="cover", border_radius="0px", grid_area="img1")
    dashboard.add_image_block("img2", image_url_2, object_fit="cover", border_radius="0px", grid_area="img2")

    # Add the interactive SIVO block
    dashboard.add_sivo_block("sivo", sivo_app, grid_area="sivo")

    # Save the output
    output_path = os.path.join(os.path.dirname(__file__), "output_transparent.html")
    dashboard.to_html(output_path)
    print(f"✅ Generated demo at {output_path}")

if __name__ == "__main__":
    main()
