import os
from sivo import Sivo

def main():
    # Setup paths
    base_dir = os.path.dirname(os.path.abspath(__file__))
    svg_path = os.path.join(base_dir, "example.svg")
    output_path = os.path.join(base_dir, "index.html")

    # Initialize Sivo app
    app = Sivo.from_svg(svg_path, default_panel_position="right")

    # Replit embed
    app.map(
        "replit_box",
        replit="https://replit.com/@replit/Python",
        panel_position="right",
        color="#ffa366"
    )

    # Twitch embed
    app.map(
        "twitch_box",
        social={"provider": "twitch", "url": "https://www.twitch.tv/ninja"},
        panel_position="left",
        color="#a970ff"
    )

    # Pinterest embed
    app.map(
        "pinterest_box",
        social={"provider": "pinterest", "url": "https://www.pinterest.com/pin/123456789/"},
        panel_position="right",
        color="#ff4d6a"
    )

    # Apple Music embed
    app.map(
        "apple_music_box",
        social={"provider": "apple_music", "url": "https://music.apple.com/us/album/thriller/269572838"},
        panel_position="bottom",
        color="#ff7384"
    )

    # Reddit embed
    app.map(
        "reddit_box",
        social={"provider": "reddit", "url": "https://www.reddit.com/r/Python/comments/1f8z9r/why_is_python_so_popular/"},
        panel_position="right",
        color="#ff7b4d"
    )

    # Google Forms embed
    app.map(
        "google_forms_box",
        external_form={"provider": "google_forms", "form_url": "https://docs.google.com/forms/d/e/1FAIpQLSe-0ABCDEF/viewform?embedded=true"},
        panel_position="right",
        color="#9873d3"
    )

    # Generate and save HTML
    html_content = app.to_html(output_path=output_path)
    print(f"Generated interactive graphic at: {output_path}")

if __name__ == "__main__":
    main()
