import os
from sivo import Sivo

def main():
    # 1. Create a pure SVG representation of a modern wood-burner and dry woodpile
    svg_content = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 600" width="100%" height="100%">
    <defs>
    </defs>

    <!-- Background Wall -->
    <rect width="800" height="600" fill="#2a3b4c" />

    <!-- Floor Tile -->
    <rect y="450" width="800" height="150" fill="#3a302a" />
    <path d="M0 450 L800 450" stroke="#221100" stroke-width="4" />

    <!-- Modern Sleek Wood-Burner (Removed ID to prevent ECharts overriding native styles) -->
    <g>
        <!-- Light Clean Smoke Animation -->
        <g opacity="0.5">
            <circle cx="400" cy="-10" r="20" fill="#f0f0f0" filter="blur(10px)">
                <animate attributeName="cy" values="140; -80" dur="3.5s" repeatCount="indefinite" />
                <animate attributeName="r" values="15; 40" dur="3.5s" repeatCount="indefinite" />
                <animate attributeName="opacity" values="0.5; 0" dur="3.5s" repeatCount="indefinite" />
                <animate attributeName="cx" values="400; 385; 415; 400" dur="3.5s" repeatCount="indefinite" />
            </circle>
            <circle cx="400" cy="-10" r="20" fill="#e0e0e0" filter="blur(12px)">
                <animate attributeName="cy" values="140; -80" dur="4.2s" begin="1.2s" repeatCount="indefinite" />
                <animate attributeName="r" values="18; 45" dur="4.2s" begin="1.2s" repeatCount="indefinite" />
                <animate attributeName="opacity" values="0.4; 0" dur="4.2s" begin="1.2s" repeatCount="indefinite" />
                <animate attributeName="cx" values="400; 420; 380; 400" dur="4.2s" begin="1.2s" repeatCount="indefinite" />
            </circle>
            <circle cx="400" cy="-10" r="20" fill="#f8f8f8" filter="blur(8px)">
                <animate attributeName="cy" values="140; -80" dur="3.8s" begin="2.0s" repeatCount="indefinite" />
                <animate attributeName="r" values="12; 35" dur="3.8s" begin="2.0s" repeatCount="indefinite" />
                <animate attributeName="opacity" values="0.6; 0" dur="3.8s" begin="2.0s" repeatCount="indefinite" />
                <animate attributeName="cx" values="400; 390; 410; 400" dur="3.8s" begin="2.0s" repeatCount="indefinite" />
            </circle>
            <circle cx="400" cy="-10" r="20" fill="#e8e8e8" filter="blur(14px)">
                <animate attributeName="cy" values="140; -80" dur="4.5s" begin="0.5s" repeatCount="indefinite" />
                <animate attributeName="r" values="16; 42" dur="4.5s" begin="0.5s" repeatCount="indefinite" />
                <animate attributeName="opacity" values="0.45; 0" dur="4.5s" begin="0.5s" repeatCount="indefinite" />
                <animate attributeName="cx" values="400; 410; 390; 400" dur="4.5s" begin="0.5s" repeatCount="indefinite" />
            </circle>
        </g>

        <!-- Flue Pipe -->
        <rect x="360" y="0" width="80" height="150" fill="#111" />
        <path d="M350 140 L450 140 L450 150 L350 150 Z" fill="#000" />

        <!-- Main Stove Body -->
        <rect x="250" y="150" width="300" height="250" rx="10" ry="10" fill="#222" />

        <!-- Glass Door -->
        <rect x="270" y="170" width="260" height="180" rx="5" ry="5" fill="#050505" />

        <!-- Burning Fire Inside -->
        <g transform="translate(400, 270)">
            <!-- Compact Fire Glow -->
            <circle cx="0" cy="0" r="30" fill="#ff7b00" opacity="0.6" />

            <!-- Clean Burning Logs -->
            <path d="M-40 30 L40 10 M-30 10 L30 30" stroke="#1a1a1a" stroke-width="12" stroke-linecap="round" />
            <path d="M-40 30 L40 10 M-30 10 L30 30" stroke="#333" stroke-width="6" stroke-linecap="round" />

            <!-- Clean Flames -->
            <path d="M-20 15 Q -10 -15 0 -35 Q 10 -15 20 15 Z" fill="#ffb732" opacity="0.9" />
            <path d="M-10 15 Q -5 -5 0 -20 Q 5 -5 10 15 Z" fill="#ffeeaa" opacity="0.9" />
        </g>

        <!-- Door Handle -->
        <rect x="535" y="240" width="10" height="40" rx="2" ry="2" fill="#silver" />

        <!-- Stove Legs / Base -->
        <rect x="300" y="400" width="200" height="50" fill="#111" />

        <!-- Invisible Hitbox for Glass -->
        <rect id="stove_glass" x="270" y="170" width="260" height="180" rx="5" ry="5" fill="transparent" stroke="transparent" />
    </g>

    <!-- Dry Woodpile (Removed ID to prevent ECharts overriding native styles) -->
    <g>
        <!-- Logs (golden brown, dry looking) -->
        <circle cx="650" cy="420" r="15" fill="#d4a373" stroke="#8b5a2b" stroke-width="2" />
        <circle cx="680" cy="420" r="15" fill="#d4a373" stroke="#8b5a2b" stroke-width="2" />
        <circle cx="710" cy="420" r="15" fill="#d4a373" stroke="#8b5a2b" stroke-width="2" />

        <circle cx="665" cy="395" r="15" fill="#d4a373" stroke="#8b5a2b" stroke-width="2" />
        <circle cx="695" cy="395" r="15" fill="#d4a373" stroke="#8b5a2b" stroke-width="2" />

        <circle cx="680" cy="370" r="15" fill="#d4a373" stroke="#8b5a2b" stroke-width="2" />

        <!-- Small Wood Rack -->
        <rect x="620" y="435" width="120" height="15" fill="#333" />
        <rect x="625" y="350" width="5" height="100" fill="#333" />
        <rect x="730" y="350" width="5" height="100" fill="#333" />

        <!-- Invisible hit box for interactivity -->
        <rect id="dry_woodpile_hitbox" x="610" y="340" width="130" height="110" fill="transparent" cursor="pointer" />
    </g>

    <text x="400" y="550" font-family="sans-serif" font-size="24" fill="#ffffff" text-anchor="middle" font-weight="bold">Modern Wood-Burner with Dry Wood</text>
    <text x="400" y="580" font-family="sans-serif" font-size="16" fill="#bbbbbb" text-anchor="middle">Hover over the woodpile or stove glass to see details</text>

</svg>"""

    # 2. Save the SVG file
    svg_path = "examples/64_modern_wood_burner/modern_wood_burner.svg"
    with open(svg_path, "w") as f:
        f.write(svg_content)

    # 3. Initialize Sivo
    app = Sivo.from_svg(
        svg_path,
        disable_zoom_controls=True,
        title="Modern Wood-Burner",
        subtitle="Clean burning example"
    )

    # 4. Map the dry woodpile to an interactive tooltip
    app.map(
        "dry_woodpile_hitbox",
        tooltip="Dry Woodpile",
        markdown="""
### Dry Firewood
This wood has been properly seasoned and dried (moisture content below 20%).

Benefits of dry wood:
* **Clean Burn**: Produces very little smoke.
* **High Efficiency**: Generates more heat since energy isn't wasted boiling off water.
* **Less Creosote**: Prevents dangerous buildup in the chimney.
        """,
        hover_color="rgba(46, 204, 113, 0.3)", # Light green highlight on hover
        color="transparent" # Keep the hitbox invisible by default
    )

    # Map the stove glass for information
    app.map(
        "stove_glass",
        tooltip="Modern Wood-Burner",
        markdown="""
### Modern Wood-Burner
This is a modern, highly efficient wood-burner.

* **Clean Air Approved**: Meets modern emission standards.
* **Secondary Combustion**: Re-burns exhaust gases to maximize heat and minimize smoke.
        """,
        hover_color="rgba(255, 255, 255, 0.2)",
        color="transparent" # Keep the hitbox invisible by default
    )

    # 5. Save the interactive HTML
    html_path = "examples/64_modern_wood_burner/index.html"
    with open(html_path, "w") as f:
        f.write(app.to_html())

    print(f"Modern wood-burner example generated at {html_path}")

if __name__ == "__main__":
    main()
