import sys
sys.path.insert(0, 'src')
from sivo.core.sivo import Sivo
import os

def main():
    svg_str = """<svg viewBox="0 0 1200 800" xmlns="http://www.w3.org/2000/svg">
        <defs>
            <linearGradient id="wallGradient" x1="0%" y1="0%" x2="0%" y2="100%">
                <stop offset="0%" stop-color="#2c3e50" />
                <stop offset="100%" stop-color="#34495e" />
            </linearGradient>
            <linearGradient id="floorGradient" x1="0%" y1="0%" x2="0%" y2="100%">
                <stop offset="0%" stop-color="#3e2723" />
                <stop offset="100%" stop-color="#4e342e" />
            </linearGradient>
            <radialGradient id="fireGlow" cx="50%" cy="50%" r="50%">
                <stop offset="0%" stop-color="#ff9800" stop-opacity="0.8"/>
                <stop offset="50%" stop-color="#ff5722" stop-opacity="0.5"/>
                <stop offset="100%" stop-color="#e64a19" stop-opacity="0"/>
            </radialGradient>
        </defs>

        <!-- Background / Room -->
        <rect x="0" y="0" width="1200" height="600" fill="url(#wallGradient)"/>
        <rect x="0" y="600" width="1200" height="200" fill="url(#floorGradient)"/>

        <!-- Window -->
        <rect x="100" y="100" width="200" height="250" fill="#87ceeb" stroke="#5d4037" stroke-width="15"/>
        <line x1="200" y1="100" x2="200" y2="350" stroke="#5d4037" stroke-width="15"/>
        <line x1="100" y1="225" x2="300" y2="225" stroke="#5d4037" stroke-width="15"/>

        <!-- The Fireplace (Wood-burner) -->

        <!-- Thick Dark Smoke Animation -->
        <g opacity="0.85">
            <!-- Central thick plumes -->
            <circle cx="660" cy="-20" r="50" fill="#1a1a1a" filter="blur(15px)">
                <animate attributeName="cy" values="400; -150" dur="3.5s" repeatCount="indefinite" />
                <animate attributeName="r" values="30; 120" dur="3.5s" repeatCount="indefinite" />
                <animate attributeName="opacity" values="0.9; 0" dur="3.5s" repeatCount="indefinite" />
                <animate attributeName="cx" values="660; 610; 710; 660" dur="3.5s" repeatCount="indefinite" />
            </circle>
            <circle cx="660" cy="-20" r="50" fill="#2a2a2a" filter="blur(20px)">
                <animate attributeName="cy" values="400; -150" dur="4.5s" begin="1.2s" repeatCount="indefinite" />
                <animate attributeName="r" values="40; 140" dur="4.5s" begin="1.2s" repeatCount="indefinite" />
                <animate attributeName="opacity" values="0.8; 0" dur="4.5s" begin="1.2s" repeatCount="indefinite" />
                <animate attributeName="cx" values="660; 720; 600; 660" dur="4.5s" begin="1.2s" repeatCount="indefinite" />
            </circle>
            <circle cx="660" cy="-20" r="50" fill="#0f0f0f" filter="blur(18px)">
                <animate attributeName="cy" values="400; -150" dur="3.8s" begin="0.5s" repeatCount="indefinite" />
                <animate attributeName="r" values="35; 130" dur="3.8s" begin="0.5s" repeatCount="indefinite" />
                <animate attributeName="opacity" values="0.95; 0" dur="3.8s" begin="0.5s" repeatCount="indefinite" />
                <animate attributeName="cx" values="660; 630; 690; 660" dur="3.8s" begin="0.5s" repeatCount="indefinite" />
            </circle>
            <!-- Secondary wider plumes -->
            <circle cx="660" cy="-20" r="60" fill="#333333" filter="blur(25px)">
                <animate attributeName="cy" values="400; -150" dur="5s" begin="2.0s" repeatCount="indefinite" />
                <animate attributeName="r" values="45; 160" dur="5s" begin="2.0s" repeatCount="indefinite" />
                <animate attributeName="opacity" values="0.7; 0" dur="5s" begin="2.0s" repeatCount="indefinite" />
                <animate attributeName="cx" values="660; 710; 610; 660" dur="5s" begin="2.0s" repeatCount="indefinite" />
            </circle>
            <circle cx="660" cy="-20" r="45" fill="#222222" filter="blur(12px)">
                <animate attributeName="cy" values="400; -150" dur="3.2s" begin="2.8s" repeatCount="indefinite" />
                <animate attributeName="r" values="25; 100" dur="3.2s" begin="2.8s" repeatCount="indefinite" />
                <animate attributeName="opacity" values="0.85; 0" dur="3.2s" begin="2.8s" repeatCount="indefinite" />
                <animate attributeName="cx" values="660; 600; 700; 660" dur="3.2s" begin="2.8s" repeatCount="indefinite" />
            </circle>
            <circle cx="660" cy="-20" r="55" fill="#151515" filter="blur(22px)">
                <animate attributeName="cy" values="400; -150" dur="4.2s" begin="1.8s" repeatCount="indefinite" />
                <animate attributeName="r" values="35; 150" dur="4.2s" begin="1.8s" repeatCount="indefinite" />
                <animate attributeName="opacity" values="0.9; 0" dur="4.2s" begin="1.8s" repeatCount="indefinite" />
                <animate attributeName="cx" values="660; 680; 640; 660" dur="4.2s" begin="1.8s" repeatCount="indefinite" />
            </circle>
        </g>

        <!-- Chimney pipe -->
        <rect x="630" y="0" width="60" height="400" fill="#212121"/>

        <!-- Stove body -->
        <rect x="560" y="400" width="200" height="180" rx="20" ry="20" fill="#424242"/>
        <rect x="580" y="420" width="160" height="100" rx="10" ry="10" fill="#111"/>

        <!-- Fire -->
        <circle cx="660" cy="470" r="35" fill="url(#fireGlow)"/>
        <path d="M 635 500 Q 645 460 655 490 Q 665 440 675 490 Q 685 460 685 500 Z" fill="#ff5722"/>
        <path d="M 645 500 Q 655 470 665 495 Q 675 470 675 500 Z" fill="#ffeb3b"/>

        <!-- Legs -->
        <rect x="580" y="580" width="15" height="40" fill="#212121"/>
        <rect x="725" y="580" width="15" height="40" fill="#212121"/>

        <!-- Woodpile Logs and Graphics -->
        <!-- Use an explicit rect as the mapped element so Echarts doesn't overlay white on a g tag -->
        <rect id="woodpile_area" x="840" y="380" width="260" height="240" fill="transparent" stroke="none"/>

        <circle cx="880" cy="580" r="20" fill="#795548" stroke="#3e2723" stroke-width="3" pointer-events="none"/>
        <circle cx="925" cy="580" r="20" fill="#795548" stroke="#3e2723" stroke-width="3" pointer-events="none"/>
        <circle cx="970" cy="580" r="20" fill="#795548" stroke="#3e2723" stroke-width="3" pointer-events="none"/>
        <circle cx="1015" cy="580" r="20" fill="#795548" stroke="#3e2723" stroke-width="3" pointer-events="none"/>
        <circle cx="1060" cy="580" r="20" fill="#795548" stroke="#3e2723" stroke-width="3" pointer-events="none"/>

        <circle cx="902" cy="545" r="20" fill="#795548" stroke="#3e2723" stroke-width="3" pointer-events="none"/>
        <circle cx="947" cy="545" r="20" fill="#795548" stroke="#3e2723" stroke-width="3" pointer-events="none"/>
        <circle cx="992" cy="545" r="20" fill="#795548" stroke="#3e2723" stroke-width="3" pointer-events="none"/>
        <circle cx="1037" cy="545" r="20" fill="#795548" stroke="#3e2723" stroke-width="3" pointer-events="none"/>

        <circle cx="925" cy="510" r="20" fill="#795548" stroke="#3e2723" stroke-width="3" pointer-events="none"/>
        <circle cx="970" cy="510" r="20" fill="#795548" stroke="#3e2723" stroke-width="3" pointer-events="none"/>
        <circle cx="1015" cy="510" r="20" fill="#795548" stroke="#3e2723" stroke-width="3" pointer-events="none"/>

        <circle cx="947" cy="475" r="20" fill="#795548" stroke="#3e2723" stroke-width="3" pointer-events="none"/>
        <circle cx="992" cy="475" r="20" fill="#795548" stroke="#3e2723" stroke-width="3" pointer-events="none"/>

        <circle cx="970" cy="440" r="20" fill="#795548" stroke="#3e2723" stroke-width="3" pointer-events="none"/>

        <!-- Damp/Wet overlay text/indicator -->
        <text x="970" y="400" font-family="sans-serif" font-size="20" font-weight="bold" fill="#81d4fa" text-anchor="middle" pointer-events="none">DAMP WOOD</text>
        <!-- Some water droplets -->
        <path d="M 870 510 Q 875 520 870 525 Q 865 520 870 510 Z" fill="#4fc3f7" pointer-events="none"/>
        <path d="M 1050 510 Q 1055 520 1050 525 Q 1045 520 1050 510 Z" fill="#4fc3f7" pointer-events="none"/>
        <path d="M 940 415 Q 945 425 940 430 Q 935 425 940 415 Z" fill="#4fc3f7" pointer-events="none"/>
    </svg>"""

    app = Sivo.from_string(
        svg_str,
        theme="dark",
        lock_zoom_out=True,
        transparent_template_lines=True
    )

    app.infographic.title = "Cartoon Wood-Burner Room"
    app.infographic.subtitle = "Hover over the damp woodpile; thick dark smoke rising from the fire."

    # Using map on the invisible rect with transparent_lines=True to ensure ECharts doesn't color it white
    app.map(
        element_id="woodpile_area",
        tooltip="Wet damp woodpile - needs to dry before burning!",
        hover_color="rgba(129, 212, 250, 0.4)",
        glow=True,
        color="transparent",
        transparent_lines=True
    )

    output_path = os.path.join(os.path.dirname(__file__), "index.html")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(app.to_html())

    print(f"Generated example at {output_path}")

if __name__ == "__main__":
    main()
