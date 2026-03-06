import os
from sivo import Sivo

def main():
    svg_path = os.path.join(os.path.dirname(__file__), "sample.svg")

    sivo_app = Sivo.from_svg(svg_path)

    # We will map a click on the play button to display a YouTube video in the info panel.
    # We can embed the iframe directly in the html mapped parameter.

    youtube_html = """
    <div style="text-align: center; width: 100%;">
        <h3 style="margin-top: 0; margin-bottom: 10px; color: #333;">SIVO Introduction</h3>
        <iframe width="100%" height="200" src="https://www.youtube.com/embed/dQw4w9WgXcQ?autoplay=1"
        title="YouTube video player" frameborder="0"
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
        allowfullscreen></iframe>
        <p style="margin-top: 10px; font-size: 14px; color: #666;">
            Watch this amazing video right inside your SVG dashboard!
        </p>
    </div>
    """

    sivo_app.map(
        element_id="play_button",
        tooltip="Click to watch video",
        html=youtube_html,
        hover_color="#CC0000",
        glow=True
    )

    # Also map the play icon so clicking it does the same
    sivo_app.map(
        element_id="play_icon",
        tooltip="Click to watch video",
        html=youtube_html,
        hover_color="#f0f0f0",
        glow=True
    )

    output_path = os.path.join(os.path.dirname(__file__), "output.html")
    sivo_app.to_html(output_path)
    print(f"Exported interactive HTML with YouTube overlay to {output_path}")

if __name__ == "__main__":
    main()
