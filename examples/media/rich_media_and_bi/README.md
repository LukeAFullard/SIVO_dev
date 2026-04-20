# Rich Media and BI Integration Example

This example demonstrates how to integrate external rich media (like Spotify playlists and Vimeo videos) and Business Intelligence (BI) dashboards (like Tableau) into a SIVO interactive SVG.

## What is being tested/demonstrated
*   **BI Dashboard Mapping:** We demonstrate mapping a specific SVG element to display a live Business Intelligence dashboard (Tableau) directly within an interactive sliding panel.
*   **Rich Media - Audio:** We map an SVG element to embed a Spotify playlist, enabling audio playback through the interactive panel.
*   **Rich Media - Video:** We map an SVG element to embed a Vimeo video, enabling video playback through the interactive panel.
*   **Panel Position:** A crucial aspect of this example is properly configuring the `panel_position` parameter. Because the media and BI embeds require a container to display in, setting the `panel_position` to `'right'` (or another valid panel position) is necessary instead of the default `'none'`.

## Example Code Snippets

```python
import os
from sivo import Sivo

def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    svg_path = os.path.join(base_dir, "sample.svg")

    app = Sivo.from_svg(svg_path)

    # 1. Map BI dashboard to a button
    # Note the panel_position="right", this ensures the Tableau iframe opens in a side panel.
    app.map(
        "dashboard_btn",
        tooltip="View Live Sales Data",
        panel_position="right",
        bi={
            "provider": "tableau",
            "dashboard_url": "https://public.tableau.com/views/SuperSampleSuperstore/SuperDescriptive?:showVizHome=no&:embed=true"
        }
    )

    # 2. Map Spotify playlist to another button
    app.map(
        "music_btn",
        tooltip="Listen to the Theme Song",
        panel_position="right",
        rich_media={
            "provider": "spotify",
            "media_url": "https://open.spotify.com/embed/track/3n3Ppam7vgaVa1iaRUc9Lp"
        }
    )

    # 3. Map Vimeo video to a polygon
    app.map(
        "video_btn",
        tooltip="Watch Intro Video",
        panel_position="right",
        rich_media={
            "provider": "vimeo",
            "media_url": "https://vimeo.com/76979871"
        }
    )

    output_path = os.path.join(base_dir, "interactive_rich_media.html")
    app.to_html(output_path)

if __name__ == "__main__":
    main()
```

## Running the Example

Run the `main.py` script to generate the `interactive_rich_media.html` file.
```bash
python3 main.py
```

Then open the generated HTML file in your web browser. Click the various SVG shapes to see the panel open with the integrated rich media or BI dashboard.