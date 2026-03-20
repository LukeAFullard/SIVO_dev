import os
from sivo import Sivo
from sivo.runtime.bundle_generator import generate_echarts_html

# CSS keyframes for our smoke animations to be injected via add_overlay
THICK_SMOKE_CSS = """
<style>
.smoke-container {
    width: 100%;
    height: 100%;
    position: relative;
    overflow: visible;
}
.smoke-plume {
    position: absolute;
    bottom: 0;
    left: 50%;
    transform: translateX(-50%);
    width: 60px;
    height: 60px;
    background: #111;
    border-radius: 50%;
    filter: blur(8px);
    opacity: 0;
    animation: thickSmokeRise 4s infinite;
}
.smoke-plume:nth-child(1) { animation-delay: 0s; left: 45%; }
.smoke-plume:nth-child(2) { animation-delay: 1.2s; left: 55%; width: 70px; height: 70px; background: #222;}
.smoke-plume:nth-child(3) { animation-delay: 2.4s; left: 48%; width: 55px; height: 55px; }

@keyframes thickSmokeRise {
    0% { transform: translate(-50%, 0) scale(1); opacity: 0.9; }
    50% { opacity: 0.7; }
    100% { transform: translate(-80%, -400px) scale(3.5); opacity: 0; }
}
</style>
<div class="smoke-container">
    <div class="smoke-plume"></div>
    <div class="smoke-plume"></div>
    <div class="smoke-plume"></div>
</div>
"""

LIGHT_SMOKE_CSS = """
<style>
.light-smoke-container {
    width: 100%;
    height: 100%;
    position: relative;
    overflow: visible;
}
.light-smoke-plume {
    position: absolute;
    bottom: 0;
    left: 50%;
    transform: translateX(-50%);
    width: 40px;
    height: 40px;
    background: #666;
    border-radius: 50%;
    filter: blur(10px);
    opacity: 0;
    animation: lightSmokeRise 5s infinite;
}
.light-smoke-plume:nth-child(1) { animation-delay: 0s; left: 48%; }
.light-smoke-plume:nth-child(2) { animation-delay: 1.5s; left: 52%; background: #777; }
.light-smoke-plume:nth-child(3) { animation-delay: 3s; left: 50%; width: 35px; height: 35px; }

@keyframes lightSmokeRise {
    0% { transform: translate(-50%, 0) scale(1); opacity: 0.4; }
    50% { opacity: 0.2; }
    100% { transform: translate(-30%, -350px) scale(2.5); opacity: 0; }
}
</style>
<div class="light-smoke-container">
    <div class="light-smoke-plume"></div>
    <div class="light-smoke-plume"></div>
    <div class="light-smoke-plume"></div>
</div>
"""

def main():
    # 1. Create the Old Wood-Burner SVG (Lighter Background + HTML Smoke Target)
    svg_old = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 800" width="100%" height="100%">
        <defs>
            <linearGradient id="wallGradientOld" x1="0%" y1="0%" x2="0%" y2="100%">
                <stop offset="0%" stop-color="#7f8c8d" />
                <stop offset="100%" stop-color="#95a5a6" />
            </linearGradient>
            <linearGradient id="floorGradientOld" x1="0%" y1="0%" x2="0%" y2="100%">
                <stop offset="0%" stop-color="#8d6e63" />
                <stop offset="100%" stop-color="#a1887f" />
            </linearGradient>
            <radialGradient id="fireGlowOld" cx="50%" cy="50%" r="50%">
                <stop offset="0%" stop-color="#ff9800" stop-opacity="0.8"/>
                <stop offset="50%" stop-color="#ff5722" stop-opacity="0.5"/>
                <stop offset="100%" stop-color="#e64a19" stop-opacity="0"/>
            </radialGradient>
        </defs>

        <!-- Background / Room -->
        <rect x="0" y="0" width="1200" height="600" fill="url(#wallGradientOld)"/>
        <rect x="0" y="600" width="1200" height="200" fill="url(#floorGradientOld)"/>

        <!-- Floor trim -->
        <line x1="0" y1="600" x2="1200" y2="600" stroke="#5d4037" stroke-width="6"/>

        <!-- Window -->
        <rect x="150" y="150" width="200" height="250" fill="#b3e5fc" stroke="#5d4037" stroke-width="15"/>
        <line x1="250" y1="150" x2="250" y2="400" stroke="#5d4037" stroke-width="15"/>
        <line x1="150" y1="275" x2="350" y2="275" stroke="#5d4037" stroke-width="15"/>

        <!-- The Fireplace (Wood-burner) -->
        <!-- Placed at center: x=450 to 750 (width 300), y=400 to 650 -->

        <!-- Chimney pipe -->
        <rect x="560" y="0" width="80" height="400" fill="#333"/>

        <!-- Invisible Smoke Target Anchor (Right above the chimney) -->
        <rect id="smoke_target_old" x="550" y="-10" width="100" height="20" fill="transparent" stroke="none" />

        <!-- Stove body (W: 300, H: 220) -->
        <rect x="450" y="400" width="300" height="220" rx="15" ry="15" fill="#424242"/>
        <rect x="480" y="430" width="240" height="130" rx="8" ry="8" fill="#111"/>

        <!-- Fire -->
        <circle cx="600" cy="510" r="45" fill="url(#fireGlowOld)"/>
        <path d="M 570 540 Q 585 480 600 520 Q 615 460 630 520 Z" fill="#ff5722"/>
        <path d="M 585 540 Q 600 490 615 530 Z" fill="#ffeb3b"/>

        <!-- Legs -->
        <rect x="480" y="620" width="20" height="50" fill="#333"/>
        <rect x="700" y="620" width="20" height="50" fill="#333"/>

        <!-- Woodpile Logs and Graphics (Wet/Damp) -->
        <rect id="woodpile_area" x="840" y="450" width="260" height="170" fill="transparent" stroke="none" cursor="pointer"/>

        <g stroke="#3e2723" stroke-width="3">
            <circle cx="880" cy="590" r="22" fill="#8d6e63" pointer-events="none"/>
            <circle cx="928" cy="590" r="22" fill="#8d6e63" pointer-events="none"/>
            <circle cx="976" cy="590" r="22" fill="#8d6e63" pointer-events="none"/>
            <circle cx="1024" cy="590" r="22" fill="#8d6e63" pointer-events="none"/>
            <circle cx="1072" cy="590" r="22" fill="#8d6e63" pointer-events="none"/>

            <circle cx="904" cy="552" r="22" fill="#8d6e63" pointer-events="none"/>
            <circle cx="952" cy="552" r="22" fill="#8d6e63" pointer-events="none"/>
            <circle cx="1000" cy="552" r="22" fill="#8d6e63" pointer-events="none"/>
            <circle cx="1048" cy="552" r="22" fill="#8d6e63" pointer-events="none"/>

            <circle cx="928" cy="514" r="22" fill="#8d6e63" pointer-events="none"/>
            <circle cx="976" cy="514" r="22" fill="#8d6e63" pointer-events="none"/>
            <circle cx="1024" cy="514" r="22" fill="#8d6e63" pointer-events="none"/>

            <circle cx="952" cy="476" r="22" fill="#8d6e63" pointer-events="none"/>
            <circle cx="1000" cy="476" r="22" fill="#8d6e63" pointer-events="none"/>
        </g>

        <!-- Damp/Wet overlay text/indicator -->
        <text x="976" y="440" font-family="sans-serif" font-size="20" font-weight="bold" fill="#0277bd" text-anchor="middle" pointer-events="none">DAMP WOOD</text>
        <!-- Water droplets -->
        <path d="M 870 510 Q 875 520 870 525 Q 865 520 870 510 Z" fill="#29b6f6" pointer-events="none"/>
        <path d="M 1060 510 Q 1065 520 1060 525 Q 1055 520 1060 510 Z" fill="#29b6f6" pointer-events="none"/>
        <path d="M 940 435 Q 945 445 940 450 Q 935 445 940 435 Z" fill="#29b6f6" pointer-events="none"/>

        <!-- Button to switch to Modern View -->
        <g transform="translate(50, 50)" cursor="pointer">
            <rect width="250" height="50" rx="10" ry="10" fill="#4CAF50" stroke="#388E3C" stroke-width="3"/>
            <text x="125" y="32" font-family="sans-serif" font-size="18" fill="white" font-weight="bold" text-anchor="middle" pointer-events="none">Upgrade to Modern</text>
            <rect id="switch_to_modern" width="250" height="50" rx="10" ry="10" fill="transparent" stroke="none"/>
        </g>
    </svg>"""

    # 2. Create the Modern Wood-Burner SVG (Same Dimensions, Lighter Background, HTML Smoke Target)
    svg_modern = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 800" width="100%" height="100%">
        <!-- Background Wall -->
        <rect width="1200" height="600" fill="#e0e0e0" />

        <!-- Floor Tile -->
        <rect y="600" width="1200" height="200" fill="#d7ccc8" />
        <!-- Floor trim -->
        <path d="M0 600 L1200 600" stroke="#8d6e63" stroke-width="6" />

        <!-- Window (Clean modern look) -->
        <rect x="150" y="150" width="200" height="250" fill="#e1f5fe" stroke="#fff" stroke-width="10"/>
        <line x1="250" y1="150" x2="250" y2="400" stroke="#fff" stroke-width="10"/>
        <line x1="150" y1="275" x2="350" y2="275" stroke="#fff" stroke-width="10"/>

        <!-- The Fireplace (Wood-burner) -->
        <!-- Placed at exactly the same center: x=450 to 750 (width 300), y=400 to 650 -->

        <!-- Flue Pipe -->
        <rect x="560" y="0" width="80" height="400" fill="#1a1a1a" />
        <path d="M550 390 L650 390 L650 400 L550 400 Z" fill="#000" />

        <!-- Invisible Smoke Target Anchor (Right above the chimney) -->
        <rect id="smoke_target_modern" x="550" y="-10" width="100" height="20" fill="transparent" stroke="none" />

        <!-- Main Stove Body (Modern Sleek) W: 300, H: 220 -->
        <rect x="450" y="400" width="300" height="220" rx="5" ry="5" fill="#222" />

        <!-- Glass Door -->
        <rect x="470" y="420" width="260" height="160" rx="3" ry="3" fill="#050505" />

        <!-- Burning Fire Inside -->
        <g transform="translate(600, 520)">
            <circle cx="0" cy="0" r="35" fill="#ff7b00" opacity="0.7" />

            <path d="M-40 30 L40 10 M-30 10 L30 30" stroke="#1a1a1a" stroke-width="14" stroke-linecap="round" />
            <path d="M-40 30 L40 10 M-30 10 L30 30" stroke="#444" stroke-width="6" stroke-linecap="round" />

            <path d="M-20 15 Q -10 -20 0 -45 Q 10 -20 20 15 Z" fill="#ffb732" opacity="0.95" />
            <path d="M-10 15 Q -5 -5 0 -25 Q 5 -5 10 15 Z" fill="#ffeeaa" opacity="0.95" />
        </g>

        <!-- Door Handle -->
        <rect x="735" y="490" width="10" height="40" rx="2" ry="2" fill="silver" />

        <!-- Stove Base -->
        <rect x="500" y="620" width="200" height="50" fill="#111" />

        <!-- Invisible Hitbox for Glass -->
        <rect id="modern_stove_glass" x="470" y="420" width="260" height="160" rx="3" ry="3" fill="transparent" stroke="transparent" cursor="pointer" />

        <!-- Dry Woodpile -->
        <!-- Placed roughly where the wet one was: x=840 to 1100, y=450 to 620 -->
        <g stroke="#8b5a2b" stroke-width="2">
            <circle cx="880" cy="590" r="20" fill="#f4a460" pointer-events="none" />
            <circle cx="925" cy="590" r="20" fill="#f4a460" pointer-events="none" />
            <circle cx="970" cy="590" r="20" fill="#f4a460" pointer-events="none" />
            <circle cx="1015" cy="590" r="20" fill="#f4a460" pointer-events="none" />

            <circle cx="902" cy="554" r="20" fill="#f4a460" pointer-events="none" />
            <circle cx="947" cy="554" r="20" fill="#f4a460" pointer-events="none" />
            <circle cx="992" cy="554" r="20" fill="#f4a460" pointer-events="none" />

            <circle cx="925" cy="518" r="20" fill="#f4a460" pointer-events="none" />
            <circle cx="970" cy="518" r="20" fill="#f4a460" pointer-events="none" />
        </g>

        <!-- Clean Modern Wood Rack -->
        <rect x="830" y="612" width="220" height="8" fill="#444" />
        <rect x="840" y="500" width="6" height="120" fill="#444" />
        <rect x="1034" y="500" width="6" height="120" fill="#444" />

        <text x="940" y="480" font-family="sans-serif" font-size="20" font-weight="bold" fill="#388e3c" text-anchor="middle" pointer-events="none">DRY SEASONED WOOD</text>

        <rect id="modern_dry_woodpile" x="830" y="470" width="220" height="150" fill="transparent" cursor="pointer" />

        <!-- Button to switch to Old View -->
        <g transform="translate(50, 50)" cursor="pointer">
            <rect width="250" height="50" rx="10" ry="10" fill="#f44336" stroke="#c62828" stroke-width="3"/>
            <text x="125" y="32" font-family="sans-serif" font-size="18" fill="white" font-weight="bold" text-anchor="middle" pointer-events="none">Back to Old Fireplace</text>
            <rect id="switch_to_old" width="250" height="50" rx="10" ry="10" fill="transparent" stroke="none"/>
        </g>
    </svg>"""

    # 3. Create the Sivo applications
    app_old = Sivo.from_string(
        svg_old,
        theme="light",
        lock_zoom_out=True,
        transparent_template_lines=True,
        title="Old Wood-Burner (Damp Wood)",
        subtitle="Thick smoke due to poor combustion and wet wood."
    )

    # Inject thick smoke via HTML overlay
    app_old.add_overlay(element_id="smoke_target_old", html=THICK_SMOKE_CSS)

    app_modern = Sivo.from_string(
        svg_modern,
        theme="light",
        lock_zoom_out=True,
        transparent_template_lines=True,
        title="Modern Wood-Burner (Dry Wood)",
        subtitle="Clean burning with minimal smoke."
    )

    # Inject light smoke via HTML overlay
    app_modern.add_overlay(element_id="smoke_target_modern", html=LIGHT_SMOKE_CSS)


    # 4. Map interactivities for Old View
    app_old.map(
        element_id="woodpile_area",
        tooltip="Wet damp woodpile",
        markdown="This wood is damp and creates thick smoke when burned.",
        hover_color="rgba(41, 182, 246, 0.4)",
        glow=True,
        color="transparent",
        transparent_lines=True
    )

    app_old.map(
        element_id="switch_to_modern",
        tooltip="Click to upgrade to a modern wood-burner",
        explode_to="modern_view",
        explode_duration_ms=800,
        hover_color="rgba(0, 0, 0, 0.1)",
        color="transparent",
        transparent_lines=True
    )

    # 5. Map interactivities for Modern View
    app_modern.map(
        element_id="modern_dry_woodpile",
        tooltip="Dry Woodpile",
        markdown="""
### Dry Firewood
Properly seasoned wood burns efficiently and produces little smoke.
        """,
        hover_color="rgba(76, 175, 80, 0.3)",
        color="transparent",
        transparent_lines=True
    )

    app_modern.map(
        element_id="modern_stove_glass",
        tooltip="Modern Wood-Burner",
        markdown="Highly efficient with secondary combustion.",
        hover_color="rgba(0, 0, 0, 0.1)",
        color="transparent",
        transparent_lines=True
    )

    app_modern.map(
        element_id="switch_to_old",
        tooltip="Click to go back to the old wood-burner",
        explode_to="old_view",
        explode_duration_ms=800,
        hover_color="rgba(0, 0, 0, 0.1)",
        color="transparent",
        transparent_lines=True
    )

    # 6. Combine both views using the bundle generator
    views_data = {
        "old_view": app_old._get_view_data(),
        "modern_view": app_modern._get_view_data()
    }

    output_path = os.path.join(os.path.dirname(__file__), "index.html")

    # Generate the single bundled HTML file containing both views
    generate_echarts_html(
        views_data=views_data,
        initial_view="old_view",
        output_path=output_path
    )

    print(f"Generated combined drilldown example at {output_path}")

if __name__ == "__main__":
    main()
