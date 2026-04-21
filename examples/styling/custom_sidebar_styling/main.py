from sivo import Sivo
import os

def main():
    print("Generating custom sidebar styling example...")

    # 1. Provide a base SVG string. We'll draw 2 simple rectangles representing different regions.
    svg_string = """
    <svg viewBox="0 0 800 600" xmlns="http://www.w3.org/2000/svg">
        <rect id="region_a" x="100" y="200" width="200" height="200" fill="#cbd5e1" stroke="#94a3b8" rx="8" />
        <rect id="region_b" x="500" y="200" width="200" height="200" fill="#cbd5e1" stroke="#94a3b8" rx="8" />
        <text x="200" y="300" text-anchor="middle" alignment-baseline="middle" font-family="sans-serif" font-size="24" fill="#334155" pointer-events="none">Region A</text>
        <text x="600" y="300" text-anchor="middle" alignment-baseline="middle" font-family="sans-serif" font-size="24" fill="#334155" pointer-events="none">Region B</text>
    </svg>
    """

    # 2. Define global CSS for the panel. This will be applied anytime the panel opens.
    global_panel_css = """
        /* This applies globally to the info-panel container */
        #info-panel {
            background: #f8fafc;
            border-left: 4px solid #3b82f6; /* Blue edge to show global style */
            font-family: "Courier New", Courier, monospace;
        }

        .info-panel-content h3 {
            color: #1d4ed8; /* Blue headers */
            text-transform: uppercase;
            letter-spacing: 1px;
        }
    """

    # 3. Initialize SIVO
    app = Sivo.from_string(
        svg_string,
        title="Custom Sidebar Styling",
        subtitle="Click Region A (global style) or Region B (element-specific override)",
        panel_css=global_panel_css, # Apply the global CSS
        default_panel_position="right"
    )

    # 4. Map Region A. It will inherit the global panel CSS.
    app.map(
        element_id="region_a",
        html="""
            <h3>Region A Info</h3>
            <p>This sidebar is using the <strong>global panel CSS</strong> defined during initialization.</p>
            <ul>
                <li>Light gray background</li>
                <li>Blue left border</li>
                <li>Blue, uppercase headers</li>
                <li>Monospace font</li>
            </ul>
        """,
        hover_color="#bae6fd" # Light blue hover
    )

    # 5. Define specific CSS for Region B's panel override.
    region_b_css = """
        /* Overrides the global style specifically when Region B is clicked */
        #info-panel {
            background: #1e293b !important; /* Dark slate */
            color: #f1f5f9; /* Light text */
            border-left: 4px solid #f59e0b !important; /* Orange edge */
            font-family: "Arial", sans-serif !important;
        }

        .info-panel-content h3 {
            color: #fcd34d !important; /* Orange headers */
            border-bottom: 1px solid #334155;
            padding-bottom: 10px;
        }

        /* Ensure close button is visible on dark background */
        .close-btn {
            background: rgba(255,255,255,0.1) !important;
            color: #cbd5e1 !important;
        }
        .close-btn:hover {
            background: rgba(255,255,255,0.2) !important;
            color: #ffffff !important;
        }
    """

    # 6. Map Region B. It will apply both the global and its own specific CSS, but because we used `!important` or specific selectors, it will override.
    app.map(
        element_id="region_b",
        html="""
            <h3>Region B Info</h3>
            <p>This sidebar is using an <strong>element-specific CSS override</strong>.</p>
            <ul>
                <li>Dark slate background</li>
                <li>Orange left border</li>
                <li>Orange, underlined headers</li>
                <li>Sans-serif font</li>
            </ul>
        """,
        hover_color="#fef08a", # Light yellow hover
        panel_css=region_b_css # Pass the specific CSS here
    )

    # 7. Generate HTML
    output_dir = os.path.dirname(os.path.abspath(__file__))
    output_file = os.path.join(output_dir, "custom_sidebar.html")
    app.to_html(output_path=output_file)

    print(f"✅ Success! Example generated at: {output_file}")
    print("Open the HTML file in a browser to see the custom sidebar styling.")

if __name__ == "__main__":
    main()
