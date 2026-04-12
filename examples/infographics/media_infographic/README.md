# Professional Media Infographic

This example demonstrates how to build a highly stylized, dark-themed interactive infographic using SIVO.
It showcases the combination of native SVG visual filters (like glows and gradients), custom CSS for glassmorphism UI, animated flow connections, and rich interactive node capabilities (embedded video, image galleries, and data visualization).

## What is being tested/demonstrated
1. **Dark Theme & Custom CSS**: A custom glassmorphism style is injected directly into the final bundle via the `custom_css` argument of `to_html()`. This targets the `#info-panel` to give it a sleek, blurred background matching the dark SVG aesthetic.
2. **Ambient Effects**: A subtle particle animation is layered under the visualization (`ambient_effect="particles"`).
3. **Animated Data Flow Connections**: Dynamic connections (`add_connection`) are drawn between nodes, simulating data telemetry moving between hubs using symbols and flow effects.
4. **Rich Content Mapping**: Nodes are mapped to different interactive payloads:
    * **Streaming Hub**: Renders a Lottie animation alongside a YouTube video embed.
    * **Core Datacenter**: Maps a complex nested ECharts pie chart with transparent background matching the theme.
    * **Content Studio**: Features a high-res image gallery.
5. **Guided Narrative Tour**: Implements `bind_tour` to step the user through the key nodes automatically.

## Running the Example
From the root of the repository, execute:
\`\`\`bash
PYTHONPATH=src python3 examples/infographics/media_infographic/main.py
\`\`\`
This will generate `media_dashboard.html` in the current folder.
