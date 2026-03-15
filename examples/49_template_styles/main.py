from sivo import Sivo
import os

def generate_styled_templates():
    template_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "src", "sivo", "templates", "bento_grid_template.svg")
    output_dir = os.path.dirname(__file__)

    styles = ["dark_mode", "minimalist", "cyberpunk", "glassmorphism", "neon"]

    for style in styles:
        # 1. Initialize Sivo from an SVG template
        sivo_app = Sivo.from_svg(template_path)

        # 2. Apply the chosen global style preset
        sivo_app.apply_template_style(style)

        # Add a simple mapping just to prove interactivity works alongside the style
        sivo_app.map(
            element_id="bento-hero",
            tooltip=f"{style.capitalize()} Hero Section",
            html=f"<h3>{style.capitalize()}</h3><p>This is the {style} template style applied to the standard Bento Grid.</p>",
            glow=True
        )

        # 3. Export to interactive HTML bundle
        output_path = os.path.join(output_dir, f"{style}_styled.html")
        sivo_app.to_html(output_path)
        print(f"Generated: {output_path}")

if __name__ == "__main__":
    generate_styled_templates()