from sivo import Sivo
import os

def generate_styled_templates():
    # Adjusted path to src/sivo/templates/3_2/bento_grid_template.svg relative to repo root.
    repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
    template_path = os.path.join(repo_root, "src", "sivo", "templates", "3_2", "bento_grid_template.svg")
    output_dir = os.path.dirname(__file__)

    styles = ["dark_mode", "minimalist", "cyberpunk", "glassmorphism", "neon"]

    for style in styles:
        # 1. Initialize Sivo from an SVG template. We set default_panel_position so that mapped html has a panel.
        sivo_app = Sivo.from_svg(template_path, default_panel_position="right")

        # 2. Apply the chosen global style preset
        sivo_app.apply_template_style(style)

        # Add a simple mapping just to prove interactivity works alongside the style
        sivo_app.map(
            element_id="bento-hero",
            tooltip=f"{style.capitalize()} Hero Section",
            html=f"<h3>{style.capitalize()}</h3><p>This is the {style} template style applied to the standard Bento Grid.</p>",
            glow=True,
            panel_position="right"
        )

        # 3. Export to interactive HTML bundle
        output_path = os.path.join(output_dir, f"{style}_styled.html")
        sivo_app.to_html(output_path)
        print(f"Generated: {output_path}")

if __name__ == "__main__":
    generate_styled_templates()