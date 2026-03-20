import os
import sys

# Optional: Add src to path if running directly without pip install
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src')))

from sivo import Sivo

def main():
    print("Building Professional Media Infographic...")

    # 1. Create a modern, complex SVG map
    svg_content = """
    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 800">
        <!-- Background Dark Gradient -->
        <defs>
            <linearGradient id="bg-grad" x1="0%" y1="0%" x2="100%" y2="100%">
                <stop offset="0%" stop-color="#0f172a" />
                <stop offset="100%" stop-color="#1e293b" />
            </linearGradient>
            <filter id="glow" x="-20%" y="-20%" width="140%" height="140%">
                <feGaussianBlur stdDeviation="5" result="blur" />
                <feComposite in="SourceGraphic" in2="blur" operator="over" />
            </filter>
        </defs>
        <rect width="100%" height="100%" fill="url(#bg-grad)" />

        <!-- Header Text -->
        <text x="600" y="80" font-family="Arial, sans-serif" font-size="36" font-weight="bold" fill="#f8fafc" text-anchor="middle" letter-spacing="2">GLOBAL MEDIA NETWORK</text>
        <text x="600" y="120" font-family="Arial, sans-serif" font-size="18" fill="#94a3b8" text-anchor="middle">Interactive Infrastructure Overview</text>

        <!-- Nodes (Datacenters/Hubs) -->
        <g id="hubs">
            <!-- Hub 1: Video Delivery (Lottie/YouTube) -->
            <circle id="hub-video" cx="300" cy="350" r="60" fill="#1e293b" stroke="#38bdf8" stroke-width="3" filter="url(#glow)"/>
            <text x="300" y="440" font-family="sans-serif" font-size="18" font-weight="bold" fill="#e2e8f0" text-anchor="middle">Streaming Hub</text>
            <text x="300" y="465" font-family="sans-serif" font-size="14" fill="#94a3b8" text-anchor="middle">Video &amp; Animation</text>

            <!-- Hub 2: Core Data Center (Charts/Stats) -->
            <rect id="hub-core" x="520" y="350" width="160" height="120" rx="15" fill="#1e293b" stroke="#8b5cf6" stroke-width="3" filter="url(#glow)"/>
            <text x="600" y="505" font-family="sans-serif" font-size="18" font-weight="bold" fill="#e2e8f0" text-anchor="middle">Core Datacenter</text>
            <text x="600" y="530" font-family="sans-serif" font-size="14" fill="#94a3b8" text-anchor="middle">Analytics Engine</text>

            <!-- Hub 3: Content Studio (Images/Gallery) -->
            <polygon id="hub-studio" points="900,300 970,420 830,420" fill="#1e293b" stroke="#f59e0b" stroke-width="3" filter="url(#glow)"/>
            <text x="900" y="465" font-family="sans-serif" font-size="18" font-weight="bold" fill="#e2e8f0" text-anchor="middle">Content Studio</text>
            <text x="900" y="490" font-family="sans-serif" font-size="14" fill="#94a3b8" text-anchor="middle">Photography &amp; Art</text>
        </g>
    </svg>
    """

    # 2. Professional Glassmorphism CSS for the Sidebar
    professional_css = """
    /* Global Background Canvas */
    body {
        background-color: #0f172a;
    }

    /* Sleek Glassmorphism Info Panel */
    #info-panel {
        background: rgba(15, 23, 42, 0.75) !important;
        backdrop-filter: blur(20px);
        -webkit-backdrop-filter: blur(20px);
        color: #f8fafc !important;
        border-left: 1px solid rgba(255, 255, 255, 0.1) !important;
        box-shadow: -15px 0 30px rgba(0, 0, 0, 0.5) !important;
        font-family: 'Inter', sans-serif !important;
    }

    /* Elegant Close Button */
    .close-btn {
        background: rgba(255, 255, 255, 0.1) !important;
        color: #e2e8f0 !important;
        backdrop-filter: blur(5px);
        border-radius: 50% !important;
        transition: all 0.3s ease;
    }
    .close-btn:hover {
        background: rgba(56, 189, 248, 0.5) !important;
        color: #ffffff !important;
        transform: scale(1.1) rotate(90deg);
    }

    /* Modern Zoom Controls */
    .zoom-btn {
        background: rgba(15, 23, 42, 0.8) !important;
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
        color: #e2e8f0 !important;
        border-radius: 50% !important;
        width: 45px !important;
        height: 45px !important;
        margin-bottom: 10px;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.3) !important;
        transition: all 0.3s ease;
    }
    .zoom-btn:hover {
        background: rgba(56, 189, 248, 0.8) !important;
        color: #ffffff !important;
        transform: translateY(-2px);
        border-color: rgba(56, 189, 248, 0.5) !important;
    }

    /* Content Typography & Styling */
    .info-panel-content h3 {
        color: #f8fafc;
        font-size: 1.8rem;
        font-weight: 700;
        margin-bottom: 0.5rem;
        border-bottom: 2px solid rgba(255, 255, 255, 0.1);
        padding-bottom: 0.5rem;
    }
    .info-panel-content p {
        color: #cbd5e1;
        line-height: 1.6;
        font-size: 1.05rem;
    }



    /* Fix Guided Tour text color in dark theme */
    #tour-container {
        color: #1e293b !important;
    }
    #tour-container p {
        color: #334155 !important;
    }
    #tour-container h2, #tour-container h3 {
        color: #0f172a !important;
    }

    /* Tour Navigation Buttons */
    .tour-nav button {
        background: rgba(56, 189, 248, 0.2) !important;
        border: 1px solid rgba(56, 189, 248, 0.5) !important;
        color: #38bdf8 !important;
        border-radius: 8px !important;
        padding: 8px 16px !important;
        font-weight: 600 !important;
        transition: all 0.2s !important;
    }
    .tour-nav button:hover {
        background: rgba(56, 189, 248, 0.8) !important;
        color: #ffffff !important;
        box-shadow: 0 0 15px rgba(56, 189, 248, 0.5) !important;
    }
    """

    # 3. Initialize Sivo with Ambient Effects and Dark Theme
    sivo_app = Sivo.from_string(
        svg_content,
        title="Media Analytics Dashboard",
        theme="dark",
        ambient_effect="particles", # Gives a high-tech floating particle background
        panel_width="35%",
        disable_zoom_controls=False
    )

    # 4. Map Interactive Behaviors to Nodes

    # Hub 1: Streaming Hub -> Lottie Animation & YouTube Embed
    sivo_app.map(
        element_id="hub-video",
        tooltip="Global Streaming Operations",
        html="""
        <h3>Streaming Hub</h3>
        <p>Distributing high-definition video and interactive animations to over 150 regions worldwide with sub-20ms latency.</p>
        <p style="color:#38bdf8; font-weight:bold;">Status: Operational (99.99% Uptime)</p>
        """,
        lottie={
            "lottie_url": "https://assets3.lottiefiles.com/packages/lf20_UJNc2t.json", # Server/tech animation
            "loop": True,
            "autoplay": True
        },
        social={"provider": "website", "url": "https://www.youtube.com/watch?v=aqz-KE-bpKQ"}, # Example tech video
        color="#0ea5e9",
        hover_color="#38bdf8",
        glow=True
    )

    # Hub 2: Core Datacenter -> Nested Chart Dashboard & Markdown Data
    sivo_app.map(
        element_id="hub-core",
        tooltip="Central Analytics Engine",
        html="""
        <h3>Core Datacenter</h3>
        <p>The nerve center of our media network. Processing petabytes of user telemetry, engagement metrics, and content metadata.</p>
        """,
        echarts_option={
            "title": {"text": "Traffic Distribution (PB)", "textStyle": {"color": "#f8fafc"}},
            "tooltip": {"trigger": "item"},
            "series": [
                {
                    "name": "Traffic",
                    "type": "pie",
                    "radius": ["40%", "70%"],
                    "itemStyle": {"borderRadius": 10, "borderColor": '#1e293b', "borderWidth": 2},
                    "data": [
                        {"value": 1048, "name": "Video", "itemStyle": {"color": "#38bdf8"}},
                        {"value": 735, "name": "Images", "itemStyle": {"color": "#f59e0b"}},
                        {"value": 580, "name": "Audio", "itemStyle": {"color": "#8b5cf6"}},
                        {"value": 484, "name": "Web", "itemStyle": {"color": "#10b981"}},
                        {"value": 300, "name": "API", "itemStyle": {"color": "#64748b"}}
                    ]
                }
            ],
            "backgroundColor": "transparent"
        },
        color="#6d28d9",
        hover_color="#8b5cf6",
        glow=True
    )

    # Hub 3: Content Studio -> High-Res Image Gallery
    sivo_app.map(
        element_id="hub-studio",
        tooltip="Creative Production Assets",
        html="""
        <h3>Content Studio</h3>
        <p>Our centralized repository for high-resolution photography, promotional artwork, and creative campaign assets.</p>
        <p><i>Click the images below to view full-screen.</i></p>
        """,
        gallery=[
            "https://images.unsplash.com/photo-1600132806370-bf17e65e942f?q=80&w=1200&auto=format&fit=crop", # Media production
            "https://images.unsplash.com/photo-1598899134739-24c46f58b8c0?q=80&w=1200&auto=format&fit=crop", # Movie set
            "https://images.unsplash.com/photo-1492691527719-9d1e07e534b4?q=80&w=1200&auto=format&fit=crop"  # Photographer
        ],
        color="#d97706",
        hover_color="#f59e0b",
        glow=True
    )

    # 5. Add Dynamic Data Flow Connections (Animated Lines)
    sivo_app.add_connection("hub-video", "hub-core", label="Telemetry Data", flow_effect=True, effect_symbol='circle', effect_size=6, color="#38bdf8")
    sivo_app.add_connection("hub-studio", "hub-core", label="Asset Sync", flow_effect=True, effect_symbol='arrow', effect_size=8, color="#f59e0b")

    # 6. Build a Guided Narrative Tour
    tour_steps = [
        {
            "content": "<h2>Welcome to the Global Media Network</h2><p>This interactive dashboard visualizes our infrastructure. Click <b>Next</b> to begin the tour.</p>",
        },
        {
            "content": "<h3>1. The Core Datacenter</h3><p>Everything routes through here. It handles complex analytics and traffic distribution. <br><br><i>Click the node after the tour to view live metrics!</i></p>",
            "zoom_to": "hub-core",
            "zoom_level": 1.5,
            "show_tooltips": ["hub-core"],
            "colors": {"hub-core": "#a78bfa"} # Highlight color during tour
        },
        {
            "content": "<h3>2. Streaming Hub</h3><p>This node manages high-bandwidth video delivery. We utilize advanced edge-caching here.</p>",
            "zoom_to": "hub-video",
            "zoom_level": 1.8,
            "show_tooltips": ["hub-video"],
            "colors": {"hub-core": "#1e293b", "hub-video": "#7dd3fc"}
        },
        {
            "content": "<h3>3. Content Studio</h3><p>Where creative assets are ingested, processed, and distributed to the CDN.</p>",
            "zoom_to": "hub-studio",
            "zoom_level": 1.8,
            "show_tooltips": ["hub-studio"],
            "colors": {"hub-video": "#1e293b", "hub-studio": "#fcd34d"}
        },
        {
            "content": "<h2>Explore Freely</h2><p>The tour is complete. Feel free to click around the nodes to view YouTube embeds, Galleries, Lottie animations, and ECharts.</p>",
            "colors": {"hub-studio": "#1e293b"}
        }
    ]
    sivo_app.bind_tour(tour_steps)

    # 7. Export the polished interactive bundle
    output_path = os.path.join(os.path.dirname(__file__), "media_dashboard.html")
    sivo_app.to_html(output_path, custom_css=professional_css)

    print(f"Interactive Media Dashboard successfully generated at: {output_path}")

if __name__ == "__main__":
    main()
