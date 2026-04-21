# New Integrations Example

This example demonstrates how to integrate external media and forms directly into a Sivo interactive graphic. The embedded integrations showcase the ability to seamlessly connect third-party platforms directly to SVG elements, allowing for rich interactivity.

## What is being shown
The example contains an SVG (`example.svg`) with six distinct rectangular interactive areas mapped to a specific platform. Clicking on any of the corresponding elements will trigger an embedded view of that service in a side/overlay panel.

The integrations being showcased are:
- **Replit**: Embedded code workspace.
- **Twitch**: Live stream embed.
- **Pinterest**: Pin embed.
- **Apple Music**: Embedded music player.
- **Reddit**: Embedded post.
- **Google Forms**: Embedded user form.

## Key Code Snippets

```python
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
    # Replit requires ?embed=true for iframes
    app.map(
        "replit_box",
        replit="https://replit.com/@replit/Python?embed=true",
        panel_position="right",
        color="#ffa366"
    )

    # Twitch embed
    # Uses a real channel name
    app.map(
        "twitch_box",
        social={"provider": "twitch", "url": "https://www.twitch.tv/twitch"},
        panel_position="left",
        color="#a970ff"
    )

    # Pinterest embed
    # Sivo inserts URLs directly into iframes. Pinterest's iframe-compatible embed format is:
    app.map(
        "pinterest_box",
        social={"provider": "pinterest", "url": "https://assets.pinterest.com/ext/embed.html?id=244812929739519212"},
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
    # By using `embed.reddit.com`, the iframe respects embeddings without returning 403.
    # The native 'reddit' provider type natively swaps /comments/ for /embed/.
    app.map(
        "reddit_box",
        social={"provider": "reddit", "url": "https://embed.reddit.com/r/Python/comments/1f8z9r/why_is_python_so_popular/"},
        panel_position="right",
        color="#ff7b4d"
    )

    # Google Forms embed
    # A generic public form URL that exists, bypassing the 'file does not exist' error.
    app.map(
        "google_forms_box",
        external_form={"provider": "google_forms", "form_url": "https://docs.google.com/forms/d/e/1FAIpQLSeZr6hSDJXdfbnNQ2omeMYLd0SpLwABU3BYUK0mpEzuILdcBQ/viewform?embedded=true"},
        panel_position="right",
        color="#9873d3"
    )

    # Generate and save HTML
    app.to_html(output_path=output_path)

if __name__ == "__main__":
    main()
```

## Running the Example
From the root directory, simply run:

```bash
python3 examples/media/new_integrations/main.py
```

This will read the `example.svg` file, apply the configured integrations, and output a fully interactive `index.html` file into this directory. Open `index.html` in your browser to experience the integrations.
