import os
from sivo import Sivo

def main():
    svg_path = os.path.join(os.path.dirname(__file__), "sample.svg")

    sivo_app = Sivo.from_svg(svg_path)

    sivo_app.map(
        element_id="sun",
        tooltip="The Custom Sun",
        html="<div class='custom-tooltip'><h3>The Custom Sun</h3><p>Styled with custom CSS!</p></div>"
    )

    # Custom CSS and JS to inject into the HTML template
    custom_css = """
        .custom-tooltip {
            background-color: #333;
            color: #fff;
            padding: 10px;
            border-radius: 8px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.3);
        }
        .custom-tooltip h3 {
            margin-top: 0;
            color: #f1c40f;
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
