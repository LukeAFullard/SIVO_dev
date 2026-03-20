import os
from sivo import Sivo

def main():
    # 1. Initialize Sivo with our SVG
    base_dir = os.path.dirname(os.path.abspath(__file__))
    svg_path = os.path.join(base_dir, "sample.svg")

    app = Sivo.from_svg(svg_path)

    # 2. Map BI dashboard to a button
    app.map(
        "dashboard_btn",
        tooltip="View Live Sales Data",
        bi={
            "provider": "metabase",
            "dashboard_url": "https://metabase.example.com/public/dashboard/xyz123"
        }
    )

    # 3. Map Spotify playlist to another button
    app.map(
        "music_btn",
        tooltip="Listen to the Theme Song",
        rich_media={
            "provider": "spotify",
            "media_url": "https://open.spotify.com/embed/track/3n3Ppam7vgaVa1iaRUc9Lp"
        }
    )

    # 4. Map Vimeo video to a polygon
    app.map(
        "video_btn",
        tooltip="Watch Intro Video",
        rich_media={
            "provider": "vimeo",
            "media_url": "https://vimeo.com/76979871"
        }
    )

    # Export to HTML
    output_path = os.path.join(base_dir, "interactive_rich_media.html")
    app.to_html(output_path)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    main()
