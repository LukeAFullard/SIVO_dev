import os
import sys

# Optional: Add src to path if running directly without pip install
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src')))

from sivo import Sivo

def main():
    print("Building Interactive Poster Infographic...")

    # 1. Create a tall, poster-style SVG
    svg_content = """
    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 2400" style="background-color: #f8fafc;">
        <!-- Background and Grid -->
        <rect width="1000" height="2400" fill="#f8fafc" />
        <pattern id="grid" width="40" height="40" patternUnits="userSpaceOnUse">
            <path d="M 40 0 L 0 0 0 40" fill="none" stroke="#e2e8f0" stroke-width="1"/>
        </pattern>
        <rect width="1000" height="2400" fill="url(#grid)" />

        <!-- Header Section -->
        <g id="header_section">
            <rect x="0" y="0" width="1000" height="300" fill="#0f172a" />
            <text x="500" y="150" font-family="'Helvetica Neue', Helvetica, Arial, sans-serif" font-size="64" font-weight="900" fill="#38bdf8" text-anchor="middle" letter-spacing="4">THE STATE OF DIGITAL MEDIA</text>
            <text x="500" y="220" font-family="'Helvetica Neue', Helvetica, Arial, sans-serif" font-size="28" font-weight="300" fill="#94a3b8" text-anchor="middle" letter-spacing="2">A 2024 Interactive Report</text>
            <!-- A subtle graphic in the header -->
            <path d="M 0,300 Q 250,250 500,300 T 1000,300" fill="none" stroke="#38bdf8" stroke-width="4" opacity="0.5"/>
        </g>

        <!-- Section 1: The Rise of Short-Form Video -->
        <g id="section_video" transform="translate(100, 400)">
            <rect x="0" y="0" width="800" height="400" rx="20" fill="#ffffff" stroke="#cbd5e1" stroke-width="2" filter="drop-shadow(0 10px 15px rgba(0,0,0,0.05))"/>
            <!-- Placeholder for Chart -->
            <rect x="50" y="100" width="300" height="250" rx="10" fill="#f1f5f9" />
            <path d="M 50,300 L 150,150 L 250,200 L 350,100" fill="none" stroke="#ef4444" stroke-width="8" stroke-linecap="round" stroke-linejoin="round"/>

            <text x="420" y="100" font-family="sans-serif" font-size="36" font-weight="800" fill="#1e293b">1. Short-Form Video Dominates</text>
            <text x="420" y="150" font-family="sans-serif" font-size="20" fill="#475569" font-style="italic">Engagement is up 400% YoY.</text>
            <foreignObject x="420" y="180" width="330" height="180">
                <div xmlns="http://www.w3.org/1999/xhtml" style="font-family: sans-serif; font-size: 16px; color: #64748b; line-height: 1.6;">
                    The landscape has shifted dramatically. Users now prefer bite-sized, high-impact content. Platforms prioritizing short-form algorithms are seeing unprecedented growth in daily active users.<br/><br/>
                    <b>Click this card to dive deep into the engagement analytics.</b>
                </div>
            </foreignObject>

            <!-- Interactive Play Button Graphic -->
            <circle cx="200" cy="225" r="40" fill="#ef4444" opacity="0.9"/>
            <polygon points="185,205 225,225 185,245" fill="#ffffff" />
        </g>

        <!-- Section 2: Audio Resurgence (Podcasts & Spatial) -->
        <g id="section_audio" transform="translate(100, 900)">
            <rect x="0" y="0" width="800" height="400" rx="20" fill="#ffffff" stroke="#cbd5e1" stroke-width="2" filter="drop-shadow(0 10px 15px rgba(0,0,0,0.05))"/>

            <text x="50" y="100" font-family="sans-serif" font-size="36" font-weight="800" fill="#1e293b">2. The Audio Resurgence</text>
            <text x="50" y="150" font-family="sans-serif" font-size="20" fill="#475569" font-style="italic">Podcasts and spatial audio go mainstream.</text>
            <foreignObject x="50" y="180" width="350" height="180">
                <div xmlns="http://www.w3.org/1999/xhtml" style="font-family: sans-serif; font-size: 16px; color: #64748b; line-height: 1.6;">
                    While screens demand attention, audio fits into the background of daily life. The rise of immersive spatial audio is creating entirely new revenue streams for creators.<br/><br/>
                    <b>Click here to explore listener demographics and revenue models.</b>
                </div>
            </foreignObject>

            <!-- Stylized Sound Wave Graphic -->
            <g transform="translate(500, 150)">
                <rect x="0" y="60" width="20" height="80" rx="10" fill="#8b5cf6" />
                <rect x="30" y="20" width="20" height="160" rx="10" fill="#a855f7" />
                <rect x="60" y="80" width="20" height="40" rx="10" fill="#d946ef" />
                <rect x="90" y="0" width="20" height="200" rx="10" fill="#8b5cf6" />
                <rect x="120" y="40" width="20" height="120" rx="10" fill="#a855f7" />
                <rect x="150" y="100" width="20" height="0" rx="10" fill="#d946ef" /> <!-- Fixed height 0 -->
            </g>
        </g>

        <!-- Section 3: The Creator Economy -->
        <g id="section_creators" transform="translate(100, 1400)">
            <rect x="0" y="0" width="800" height="400" rx="20" fill="#ffffff" stroke="#cbd5e1" stroke-width="2" filter="drop-shadow(0 10px 15px rgba(0,0,0,0.05))"/>

            <!-- Graphic: Network/Connections -->
            <circle cx="200" cy="200" r="100" fill="#fef3c7" />
            <circle cx="200" cy="200" r="40" fill="#f59e0b" />
            <circle cx="120" cy="150" r="20" fill="#fbbf24" />
            <circle cx="280" cy="150" r="20" fill="#fbbf24" />
            <circle cx="150" cy="280" r="30" fill="#fbbf24" />
            <circle cx="250" cy="280" r="25" fill="#fbbf24" />
            <path d="M 200,200 L 120,150 M 200,200 L 280,150 M 200,200 L 150,280 M 200,200 L 250,280" stroke="#f59e0b" stroke-width="4" stroke-dasharray="5,5"/>

            <text x="420" y="100" font-family="sans-serif" font-size="36" font-weight="800" fill="#1e293b">3. The Creator Middle Class</text>
            <text x="420" y="150" font-family="sans-serif" font-size="20" fill="#475569" font-style="italic">Monetization beyond the top 1%.</text>
            <foreignObject x="420" y="180" width="330" height="180">
                <div xmlns="http://www.w3.org/1999/xhtml" style="font-family: sans-serif; font-size: 16px; color: #64748b; line-height: 1.6;">
                    Direct-to-fan monetization tools (subscriptions, digital products) have matured. It is now possible to build a sustainable business with 1,000 true fans rather than 1,000,000 casual viewers.<br/><br/>
                    <b>Click to see the breakdown of creator revenue streams.</b>
                </div>
            </foreignObject>
        </g>

        <!-- Section 4: AI in Content Generation -->
        <g id="section_ai" transform="translate(100, 1900)">
            <rect x="0" y="0" width="800" height="400" rx="20" fill="#1e293b" stroke="#334155" stroke-width="2" filter="drop-shadow(0 10px 15px rgba(0,0,0,0.1))"/>

            <text x="50" y="100" font-family="sans-serif" font-size="36" font-weight="800" fill="#f8fafc">4. AI as a Co-Pilot</text>
            <text x="50" y="150" font-family="sans-serif" font-size="20" fill="#94a3b8" font-style="italic">Generative tools reshape the workflow.</text>
            <foreignObject x="50" y="180" width="400" height="180">
                <div xmlns="http://www.w3.org/1999/xhtml" style="font-family: sans-serif; font-size: 16px; color: #cbd5e1; line-height: 1.6;">
                    From scriptwriting to automated editing, AI is reducing production time by up to 60%. The focus is shifting from "how to make it" to "what to say."<br/><br/>
                    <b style="color: #38bdf8;">Click to view an interactive gallery of AI-generated assets.</b>
                </div>
            </foreignObject>

            <!-- Graphic: AI Sparkles / Brain -->
            <g transform="translate(600, 200)">
                <circle cx="0" cy="0" r="80" fill="#0f172a" stroke="#38bdf8" stroke-width="4"/>
                <path d="M -40,-20 Q 0,-60 40,-20 Q 60,20 20,40 Q -20,60 -40,20 Z" fill="none" stroke="#e0f2fe" stroke-width="2"/>
                <circle cx="0" cy="0" r="10" fill="#38bdf8" />
                <!-- Sparkles -->
                <path d="M 60,-60 L 70,-80 L 80,-60 L 100,-50 L 80,-40 L 70,-20 L 60,-40 L 40,-50 Z" fill="#38bdf8" />
                <path d="M -60,60 L -65,75 L -80,80 L -65,85 L -60,100 L -55,85 L -40,80 L -55,75 Z" fill="#38bdf8" />
            </g>
        </g>

        <!-- Footer -->
        <text x="500" y="2350" font-family="sans-serif" font-size="14" fill="#94a3b8" text-anchor="middle">Interactive Infographic built with SIVO. Data is illustrative.</text>

    </svg>
    """

    # 2. Custom CSS for a clean, modern poster feel
    custom_css = """
    body {
        background-color: #f1f5f9; /* Soft background around the poster */
    }

    /* Make the poster center aligned and add a shadow */
    #chart-container {
        display: flex;
        justify-content: center;
        padding: 40px 0;
        overflow-y: auto !important;
        align-items: flex-start !important;
    }

    /* Ensure the poster scrolls naturally */
    .sivo-canvas-wrapper {
        min-height: 2400px; /* Match SVG height */
        max-width: 1000px !important;
        margin: 0 auto;
        box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.25);
        border-radius: 8px;
        overflow: hidden;
    }

    /* Info Panel Styling (Clean, Light Theme) */
    #info-panel {
        background: rgba(255, 255, 255, 0.95) !important;
        backdrop-filter: blur(10px);
        color: #1e293b !important;
        border-left: 1px solid #e2e8f0 !important;
        box-shadow: -10px 0 25px rgba(0, 0, 0, 0.1) !important;
        font-family: 'Helvetica Neue', sans-serif !important;
    }

    .info-panel-header {
        border-bottom: 2px solid #f1f5f9 !important;
        padding: 20px !important;
    }

    .info-panel-content {
        padding: 24px !important;
    }

    .info-panel-content h3 {
        color: #0f172a;
        font-size: 1.8rem;
        font-weight: 800;
        margin-bottom: 1rem;
        border-bottom: none;
    }

    .info-panel-content h4 {
        color: #64748b;
        text-transform: uppercase;
        letter-spacing: 1px;
        font-size: 0.9rem;
        margin-top: 0;
    }

    .close-btn {
        color: #64748b !important;
        background: #f1f5f9 !important;
        border-radius: 50% !important;
    }
    .close-btn:hover {
        background: #e2e8f0 !important;
        color: #0f172a !important;
    }
    """

    # 3. Initialize Sivo
    # Using bounding_coords to ensure the aspect ratio of the tall poster is perfectly maintained
    sivo_app = Sivo.from_string(
        svg_content,
        title="Interactive Poster",
        theme="light",
        panel_width="40%",
        disable_zoom_controls=False,
        bounding_coords=[[0, 2400], [1000, 0]] # Map SVG 0,0 to bottom left lat/long logic if needed, but not strictly necessary for standard interactives. We'll omit bounding_coords to let ECharts auto-fit the SVG natively.
    )

    # We recreate the app without bounding coords so the SVG just fits the container natively
    sivo_app = Sivo.from_string(
        svg_content,
        title="The State of Digital Media",
        theme="light",
        panel_width="450px",
        bounding_coords=[[0, 2400], [1000, 0]]
    )

    # 4. Map Interactions to the Poster Sections

    # Section 1: Video -> ECharts Bar Race or detailed Line Chart
    sivo_app.map(
        element_id="section_video",
        tooltip="Click to view Engagement Analytics",
        hover_color="#f8fafc", # Subtle hover effect
        glow=True,
        html="""
        <h4>Deep Dive: Short-Form Video</h4>
        <h3>Engagement Trajectory</h3>
        <p>Short-form video has completely cannibalized traditional feed scrolling. Below is the comparative daily active user (DAU) engagement time across major platforms.</p>
        """,
        echarts_option={
            "tooltip": {"trigger": "axis"},
            "legend": {"data": ["TikTok", "Reels", "Shorts"]},
            "xAxis": {"type": "category", "data": ["2020", "2021", "2022", "2023", "2024"]},
            "yAxis": {"type": "value", "name": "Minutes / Day"},
            "series": [
                {"name": "TikTok", "type": "line", "smooth": True, "data": [45, 68, 85, 95, 110], "itemStyle": {"color": "#000000"}},
                {"name": "Reels", "type": "line", "smooth": True, "data": [10, 25, 45, 70, 90], "itemStyle": {"color": "#E1306C"}},
                {"name": "Shorts", "type": "line", "smooth": True, "data": [0, 15, 35, 60, 85], "itemStyle": {"color": "#FF0000"}}
            ],
            "backgroundColor": "transparent"
        }
    )

    # Section 2: Audio -> Embedded Podcast / Audio Player
    sivo_app.map(
        element_id="section_audio",
        tooltip="Click to explore Audio Insights",
        hover_color="#f8fafc",
        glow=True,
        html="""
        <h4>Deep Dive: Audio Resurgence</h4>
        <h3>The New Radio</h3>
        <p>Listen to an excerpt from our industry round-table discussing the monetization of spatial audio.</p>
        """,
        social={"provider": "website", "url": "https://open.spotify.com/embed/episode/7makk4oTQel546B0PZlVR5?utm_source=generator"} # Spotify embed example
    )

    # Section 3: Creators -> ECharts Pie / Treemap
    sivo_app.map(
        element_id="section_creators",
        tooltip="Click to view Revenue Streams",
        hover_color="#f8fafc",
        glow=True,
        html="""
        <h4>Deep Dive: The Creator Economy</h4>
        <h3>Revenue Diversification</h3>
        <p>The middle class of creators no longer relies solely on ad-sense. Direct support and digital products now make up the majority of income for creators with 10k-100k followers.</p>
        """,
        echarts_option={
            "tooltip": {"trigger": "item"},
            "series": [
                {
                    "name": "Revenue Source",
                    "type": "pie",
                    "radius": ["40%", "70%"],
                    "itemStyle": {"borderRadius": 10, "borderColor": '#fff', "borderWidth": 2},
                    "label": {"show": False},
                    "data": [
                        {"value": 40, "name": "Brand Deals", "itemStyle": {"color": "#f59e0b"}},
                        {"value": 30, "name": "Digital Products", "itemStyle": {"color": "#10b981"}},
                        {"value": 20, "name": "Subscriptions (Patreon, etc.)", "itemStyle": {"color": "#8b5cf6"}},
                        {"value": 10, "name": "Ad Revenue", "itemStyle": {"color": "#ef4444"}}
                    ]
                }
            ],
            "backgroundColor": "transparent"
        }
    )

    # Section 4: AI -> Image Gallery
    sivo_app.map(
        element_id="section_ai",
        tooltip="Click to view AI Gallery",
        hover_color="#334155", # Darker hover for the dark section
        glow=True,
        html="""
        <h4>Deep Dive: AI Co-Pilot</h4>
        <h3>Generative Asset Gallery</h3>
        <p>All images below were generated using prompt-based AI models, demonstrating the rapid advancement in visual fidelity.</p>
        """,
        gallery=[
            "https://images.unsplash.com/photo-1682687982501-1e58f813fb31?q=80&w=1200&auto=format&fit=crop", # Conceptual AI
            "https://images.unsplash.com/photo-1677442136019-21780ecad995?q=80&w=1200&auto=format&fit=crop",
            "https://images.unsplash.com/photo-1682687220742-aba13b6e50ba?q=80&w=1200&auto=format&fit=crop"
        ]
    )

    # 5. Add a "Floating" Action button at the top
    sivo_app.map(
        element_id="header_section",
        tooltip="Download Full PDF Report",
        url="https://example.com/report.pdf" # Navigates away
    )

    # Export
    output_path = os.path.join(os.path.dirname(__file__), "poster.html")
    sivo_app.to_html(output_path, custom_css=custom_css)

    print(f"Interactive Poster successfully generated at: {output_path}")

if __name__ == "__main__":
    main()
