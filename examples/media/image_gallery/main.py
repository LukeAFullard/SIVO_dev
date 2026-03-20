import os
from sivo import Sivo

def main():
    svg_path = os.path.join(os.path.dirname(__file__), "sample.svg")

    sivo_app = Sivo.from_svg(svg_path)

    # Click the shape to open a beautiful image lightbox gallery
    sivo_app.map(
        element_id="play_button",
        tooltip="Click to view photo gallery",
        gallery=[
            "https://images.unsplash.com/photo-1506744626753-1fa44df14d28?q=80&w=1200&auto=format&fit=crop",
            "https://images.unsplash.com/photo-1472214103451-9374bd1c798e?q=80&w=1200&auto=format&fit=crop",
            "https://images.unsplash.com/photo-1469474968028-56623f02e42e?q=80&w=1200&auto=format&fit=crop"
        ],
        hover_color="#0066cc",
        glow=True
    )

    output_path = os.path.join(os.path.dirname(__file__), "output.html")
    sivo_app.to_html(output_path)
    print(f"Exported gallery interactive HTML to {output_path}")

if __name__ == "__main__":
    main()
