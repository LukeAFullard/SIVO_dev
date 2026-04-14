import os
from sivo import Sivo, SivoDashboard

def main():
    # --- 1. Dashboard initialization ---
    # We use a beautiful, dark abstract mesh background from Unsplash for a professional look.
    # By setting `theme="transparent"`, SivoDashboard automatically strips the default
    # cards, borders, and glassmorphism, allowing elements to float seamlessly.
    dashboard = SivoDashboard(
        title="Floating UI Dashboard",
        columns=3,
        background_image_url="https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?q=80&w=2564&auto=format&fit=crop",
        theme="transparent"
    )

    dashboard.set_grid_layout(
        desktop='''
    "header header header"
    "img1 img2 img3"
    "img4 img5 img6"
        ''',
        mobile='''
    "header"
    "img1"
    "img2"
    "img3"
    "img4"
    "img5"
    "img6"
        '''
    )

    # --- 2. Add High-Quality Transparent PNGs as Interactive Sivo Blocks ---
    # We embed the transparent PNGs inside simple SVG canvases so that Sivo can natively parse
    # them and make them fully interactive (e.g. popups, URLs, drilldowns).
    # We still use the built-in `.sivo-floating-element` CSS classes to apply the floating drop-shadow.
    pngs = [
        ("img1", "Rocket", "Launch operations and deployments.", "https://raw.githubusercontent.com/microsoft/fluentui-emoji/main/assets/Rocket/3D/rocket_3d.png"),
        ("img2", "Prediction", "Future forecasts and analytics.", "https://raw.githubusercontent.com/microsoft/fluentui-emoji/main/assets/Crystal%20ball/3D/crystal_ball_3d.png"),
        ("img3", "Research", "Deep dive data inspection.", "https://raw.githubusercontent.com/microsoft/fluentui-emoji/main/assets/Microscope/3D/microscope_3d.png"),
        ("img4", "Design", "UI/UX component library.", "https://raw.githubusercontent.com/microsoft/fluentui-emoji/main/assets/Palette/3D/palette_3d.png"),
        ("img5", "Admin", "Administrative controls and settings.", "https://raw.githubusercontent.com/microsoft/fluentui-emoji/main/assets/Crown/3D/crown_3d.png"),
        ("img6", "Development", "Codebase metrics.", "https://raw.githubusercontent.com/microsoft/fluentui-emoji/main/assets/Laptop/3D/laptop_3d.png"),
    ]

    for block_id, title, desc, url in pngs:
        # We assign an inline animation delay to make the floating asynchronous
        delay = hash(block_id) % 5

        # We wrap the image in an SVG and apply our custom floating classes natively
        # Note: We do NOT apply the animation to the <image> node directly. Doing so would
        # move the visual image away from the ECharts invisible hitbox layer overlayed on top,
        # breaking clickability. Instead, we apply the float class to the entire Sivo block container.
        # We also set draggable="false" (a standard HTML attribute that ECharts respects on image elements in SVG mode).
        # We must NOT set `pointer-events: auto` because the native SVG layer overlays the ECharts canvas;
        # doing so would intercept the click and prevent ECharts from firing the sidebar overlay event.
        svg_content = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200">
            <image id="obj_{block_id}" href="{url}" x="25" y="25" width="150" height="150" draggable="false" style="filter: drop-shadow(0px 20px 30px rgba(0, 0, 0, 0.5)); user-select: none; -webkit-user-drag: none;" />
        </svg>'''

        # Create the interactive Sivo block.
        # CRITICAL: We set render_mode="svg" so Sivo renders the raw SVG.
        # We set default_panel_position="overlay" so clicks open a sliding sidebar.
        # We apply the floating animation class to the entire panel via `panel_css` to ensure
        # both the image AND the interaction hitbox bounce up and down together.
        sivo_app = Sivo.from_string(
            svg_content,
            render_mode="svg",
            default_panel_position="overlay",
            panel_css=f"animation: sivo-float 6s ease-in-out infinite; animation-delay: {delay}s;"
        )

        # Map interactivity to the image!
        # Because we added `image` to the Sivo parser, hover effects and click popups work natively.
        sivo_app.map(
            f"obj_{block_id}",
            hover_color="#ffffff", # Makes the image glow slightly on hover
            html=f"<h3>{title}</h3><p>{desc}</p><br><a href='#' style='color: #3b82f6;'>View Dashboard</a>"
        )

        dashboard.add_sivo_block(block_id, sivo_app, grid_area=block_id)

    # Export
    output_file = os.path.join(os.path.dirname(__file__), "output.html")
    dashboard.to_html(output_file)
    print(f"Successfully generated floating PNG dashboard: {output_file}")


if __name__ == "__main__":
    main()
