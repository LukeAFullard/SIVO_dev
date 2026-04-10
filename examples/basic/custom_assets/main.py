import os
from sivo import Sivo

def main():
    svg_path = os.path.join(os.path.dirname(__file__), "sample.svg")

    sivo_app = Sivo.from_svg(svg_path)

    # Custom CSS and JS to inject into the HTML template
    # Note: If the panel is rendered inside a Shadow DOM, we can just inject
    # the <style> directly into the HTML payload, or rely on `panel_css` argument for the map

    html_payload = """
    <style>
        /* This style block will be safely injected inside the Shadow DOM */
        .custom-tooltip {
            background-color: #ff0055 !important;
            color: #fff !important;
            padding: 30px !important;
            border-radius: 20px !important;
            box-shadow: 0 10px 20px rgba(0,0,0,0.5) !important;
            font-size: 24px !important;
            text-align: center !important;
        }
        .custom-tooltip h3 {
            margin-top: 0 !important;
            color: #ffff00 !important;
            font-size: 32px !important;
            text-transform: uppercase !important;
        }
    </style>
    <div class='custom-tooltip'><h3>The Custom Sun</h3><p>Styled with VERY custom CSS to make it obvious!</p></div>
    """

    # We update the mapping to use the new payload with the inline styles for the shadow DOM
    sivo_app.map(
        element_id="sun",
        tooltip="The Custom Sun",
        html=html_payload,
        panel_position="overlay" # Explicitly show the HTML inside an overlay panel
    )

    # We can still inject global custom CSS for the main document if we need to style something outside the Shadow DOM
    custom_css = """
        /* Main document custom CSS */
        body {
            /* Example of styling the main window */
        }
    """

    custom_js = """
        console.log('Hello from custom injected JS!');
    """

    output_path = os.path.join(os.path.dirname(__file__), "output.html")
    sivo_app.to_html(output_path, custom_css=custom_css, custom_js=custom_js)
    print(f"Exported interactive HTML to {output_path}")

if __name__ == "__main__":
    main()
