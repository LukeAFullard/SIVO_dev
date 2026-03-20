import os
from sivo import Sivo

# 1. Create a minimal SVG map
svg_content = """
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 600">
    <rect width="100%" height="100%" fill="#f8fafc" />
    <text x="400" y="50" font-family="sans-serif" font-size="24" text-anchor="middle" fill="#334155">Interactive Datacenter Map</text>

    <g id="servers">
        <rect id="server-alpha" x="200" y="200" width="150" height="200" rx="10" fill="#e2e8f0" stroke="#94a3b8" stroke-width="2" />
        <text x="275" y="300" font-family="sans-serif" font-size="16" text-anchor="middle" fill="#475569">Server Alpha</text>

        <rect id="server-beta" x="450" y="200" width="150" height="200" rx="10" fill="#e2e8f0" stroke="#94a3b8" stroke-width="2" />
        <text x="525" y="300" font-family="sans-serif" font-size="16" text-anchor="middle" fill="#475569">Server Beta</text>
    </g>
</svg>
"""

# 2. Define the Professional Custom CSS (Sleek Dark Glassmorphism Theme)
professional_css = """
/* 1. Global Canvas Background Overlay */
body {
    background-color: #f1f5f9; /* Soft background */
}

/* 2. Sleek Glassmorphism Info Panel */
#info-panel {
    background: rgba(15, 23, 42, 0.85) !important; /* Deep dark slate with transparency */
    backdrop-filter: blur(16px); /* Glass effect */
    -webkit-backdrop-filter: blur(16px);
    color: #f8fafc !important; /* High contrast text */
    border-left: 1px solid rgba(255, 255, 255, 0.1) !important;
    box-shadow: -10px 0 25px rgba(0, 0, 0, 0.2) !important;
}

/* 3. Panel Header refinements */
.info-panel-header {
    background: transparent !important;
    border-bottom: 1px solid rgba(255, 255, 255, 0.1) !important;
}

/* 4. Elegant Close Button */
.close-btn {
    background: rgba(255, 255, 255, 0.1) !important;
    color: #e2e8f0 !important;
    backdrop-filter: blur(4px);
}
.close-btn:hover {
    background: rgba(255, 255, 255, 0.2) !important;
    color: #ffffff !important;
    transform: scale(1.05);
}

/* 5. Modern Zoom Controls */
.zoom-btn {
    background: rgba(255, 255, 255, 0.9) !important;
    backdrop-filter: blur(4px);
    border: 1px solid rgba(0, 0, 0, 0.05) !important;
    color: #334155 !important;
    border-radius: 50% !important; /* Circular buttons */
    width: 40px !important;
    height: 40px !important;
    margin-bottom: 8px;
    box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06) !important;
}
.zoom-btn:hover {
    background: #ffffff !important;
    color: #0f172a !important;
    transform: translateY(-2px);
    box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05) !important;
}

/* 6. Formatting inside the panel content */
.info-panel-content h3 {
    margin-top: 0;
    color: #38bdf8; /* Bright blue accent */
    font-size: 1.5rem;
    font-weight: 600;
    letter-spacing: -0.025em;
}
.info-panel-content p {
    color: #cbd5e1; /* Softer text for body */
    line-height: 1.7;
}
.status-badge {
    display: inline-block;
    padding: 4px 12px;
    border-radius: 9999px;
    font-size: 0.875rem;
    font-weight: 500;
    background: rgba(34, 197, 94, 0.2);
    color: #4ade80;
    border: 1px solid rgba(34, 197, 94, 0.4);
    margin-bottom: 16px;
}
"""

def main():
    print("Building Professional Styling Example...")

    # Initialize Sivo
    sivo_app = Sivo.from_string(svg_content)

    # Map interactions
    sivo_app.map(
        element_id="server-alpha",
        tooltip="Server Alpha Details",
        html="""
        <h3>Server Alpha</h3>
        <span class="status-badge">● Online</span>
        <p>This server handles primary database routing and load balancing. Uptime is currently 99.99%.</p>
        <p><b>Load:</b> 45%</p>
        <p><b>Temp:</b> 42°C</p>
        """,
        color="#bae6fd", # Light blue highlight
        hover_color="#7dd3fc",
        glow=True
    )

    sivo_app.map(
        element_id="server-beta",
        tooltip="Server Beta Details",
        html="""
        <h3>Server Beta</h3>
        <span class="status-badge" style="background: rgba(239, 68, 68, 0.2); color: #f87171; border-color: rgba(239, 68, 68, 0.4);">● Warning</span>
        <p>This server is currently experiencing higher than normal latency. Investigation is ongoing.</p>
        <p><b>Load:</b> 92%</p>
        <p><b>Temp:</b> 75°C</p>
        """,
        color="#fecaca", # Light red highlight
        hover_color="#fca5a5",
        glow=True
    )

    # Generate the HTML, injecting the custom professional CSS
    output_path = os.path.join(os.path.dirname(__file__), "output.html")
    sivo_app.to_html(output_path, custom_css=professional_css)

    print(f"Interactive map successfully generated at: {output_path}")
    print("Open the HTML file in a web browser and click on the servers to see the custom professional glassmorphism panel.")

if __name__ == "__main__":
    main()
