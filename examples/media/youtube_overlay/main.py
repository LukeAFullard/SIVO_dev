import os
from sivo import Sivo

def main():
    svg_path = os.path.join(os.path.dirname(__file__), "sample.svg")

    sivo_app = Sivo.from_svg(svg_path)

    # We map a video URL to the play button
    # SIVO natively handles video URLs by opening them in a beautiful, centered modal overlay
    # when the mapped SVG element is clicked.

    # We use youtube-nocookie.com to ensure playback works gracefully in embedded contexts without tracking issues
    video_url = "https://www.youtube-nocookie.com/embed/jNQXAC9IVRw?autoplay=1"

    sivo_app.map(
        element_id="play_button",
        tooltip="Click to watch video",
        video=video_url,
        hover_color="#CC0000",
        glow=True
    )

    sivo_app.map(
        element_id="play_icon",
        tooltip="Click to watch video",
        video=video_url,
        hover_color="#f0f0f0",
        glow=True
    )

    output_path = os.path.join(os.path.dirname(__file__), "output.html")
    sivo_app.to_html(output_path)
    print(f"Exported interactive HTML with built-in YouTube overlay to {output_path}")

if __name__ == "__main__":
    main()
