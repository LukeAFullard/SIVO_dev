import os
from sivo import Sivo, SivoDashboard

def main():
    # --- 1. Dashboard initialization with 3 columns ---
    # We provide a direct background_image_url containing a tangible scene (a forest)
    dashboard = SivoDashboard(
        title="Mixed Features with Background",
        columns=3,
        background_image_url="https://images.unsplash.com/photo-1448375240586-882707db888b?q=80&w=2070&auto=format&fit=crop"
    )

    # We set a desktop layout and a mobile layout to see how the background behaves
    dashboard.set_grid_layout(
        desktop='''
    "header header header"
    "text graph image"
    "video details image"
        ''',
        mobile='''
    "header"
    "text"
    "graph"
    "details"
    "image"
    "video"
        '''
    )

    # --- 2. Header Block ---
    header_html = '''
    <div style="text-align: center;">
        <h2 style="margin:0;">Dashboard Header</h2>
        <p>Observe how the fixed background image (forest) remains stable while the grid reshapes on different screen sizes.</p>
    </div>
    '''
    dashboard.add_html_block("header_block", header_html, grid_area="header")


    # --- 3. Text Block ---
    text_html = '''
    <div style="padding: 10px;">
        <h3>Text Feature</h3>
        <p>This is a standard text block containing HTML content.</p>
        <p>When you resize the window, this block will reposition according to the CSS Grid rules (Desktop vs Mobile).</p>
        <ul>
            <li>Item 1</li>
            <li>Item 2</li>
            <li>Item 3</li>
        </ul>
    </div>
    '''
    dashboard.add_html_block("text_block", text_html, grid_area="text")


    # --- 4. Graph Block (Sivo Canvas) ---
    graph_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400">
        <rect width="400" height="400" fill="transparent" />
        <circle cx="200" cy="200" r="100" fill="#3b82f6" id="circle_1" />
        <text x="200" y="205" font-family="sans-serif" font-size="24" fill="#fff" text-anchor="middle" pointer-events="none">Interactive SVG</text>
    </svg>"""
    sivo_graph = Sivo.from_string(graph_svg, theme="light", default_panel_position="none")
    # Setting panel_position="overlay" makes sure the sliding sidebar appears when clicked,
    # but we are also adding a Details Panel below so the html shows up there too.
    sivo_graph.map("circle_1", hover_color="#f59e0b", panel_position="overlay", html="<h4>Clicked the circle</h4><p>Interactivity works within translucent grid items. The background image of the forest is visible.</p>")
    dashboard.add_sivo_block("graph_block", sivo_graph, grid_area="graph")

    # Add a details panel that will react to the click on the map
    dashboard.add_details_panel("details_panel", title="Graph Details", placeholder="Click the circle in the graph to see details.", grid_area="details")


    # --- 5. Image Block ---
    # Using an image tag in an HTML block
    image_html = '''
    <div style="display: flex; flex-direction: column; align-items: center; justify-content: center; height: 100%;">
        <h3>Image Feature</h3>
        <img src="https://images.unsplash.com/photo-1550745165-9bc0b252726f?q=80&w=600&auto=format&fit=crop" style="max-width: 100%; height: auto; border-radius: 8px;" alt="Sample image">
    </div>
    '''
    dashboard.add_html_block("image_block", image_html, grid_area="image")


    # --- 6. Video Block ---
    # Using an iframe for a YouTube video
    video_html = '''
    <div style="display: flex; flex-direction: column; align-items: center; justify-content: center; height: 100%;">
        <h3>Video Feature</h3>
        <iframe width="100%" height="250" src="https://www.youtube.com/embed/dQw4w9WgXcQ?si=abcdefgh" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen style="border-radius: 8px;"></iframe>
    </div>
    '''
    dashboard.add_html_block("video_block", video_html, grid_area="video")

    # Export
    output_file = os.path.join(os.path.dirname(__file__), "output.html")
    dashboard.to_html(output_file)
    print(f"Successfully generated mixed features background dashboard: {output_file}")


if __name__ == "__main__":
    main()
