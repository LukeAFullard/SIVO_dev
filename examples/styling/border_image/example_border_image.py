import os
from sivo import Sivo

def create_border_image_example():
    # Simple SVG template
    svg_str = '''
    <svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
        <rect id="main_content" x="20" y="20" width="60" height="60" fill="rgba(255, 255, 255, 0.5)" rx="5" cursor="pointer"/>
        <text x="50" y="55" font-size="8" text-anchor="middle" font-family="sans-serif" pointer-events="none">Click Me!</text>
    </svg>
    '''

    # Initialize Sivo
    app = Sivo.from_string(svg_str, theme='light')

    # Add background image (covers the entire canvas)
    app.add_background_image(
        url="https://images.unsplash.com/photo-1557683316-973673baf926?auto=format&fit=crop&q=80&w=1000",
        opacity=0.6,
        grayscale=False
    )

    # Add a border image along the left hand side, 10% wide
    app.add_border_image(
        url="https://images.unsplash.com/photo-1579546929518-9e396f3cc809?auto=format&fit=crop&q=80&w=200",
        position="left",
        width="10%",
        opacity=1.0,
        grayscale=False
    )

    # Map click event to open a side panel
    # Note: Default panel_position is None, so we must explicitly set it to 'right' (or 'left', 'bottom', etc.)
    app.map(
        element_id="main_content",
        html="<h2>Panel Content</h2><p>This side panel was opened by clicking the main content area.</p>",
        panel_position="right",
        tooltip="Click to open panel"
    )

    # Save to HTML in the same directory as this script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    output_path = os.path.join(script_dir, "border_image_demo.html")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(app.to_html())

    print(f"Created example at {output_path}")

if __name__ == "__main__":
    create_border_image_example()
