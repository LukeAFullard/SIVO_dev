import os
from sivo import Sivo

def main():
    # Simple SVG representing a basic dashboard status panel
    svg = """
    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 300 100">
        <!-- Status Indicator Dot -->
        <circle id="status_dot" cx="30" cy="50" r="15" fill="#9ca3af" />

        <!-- Static Label -->
        <text x="60" y="55" font-family="Arial" font-size="16" fill="#374151" pointer-events="none">System Status Connection</text>
    </svg>
    """

    sivo_app = Sivo.from_string(svg, title="Live API Binding Test")

    # Map the status dot initially
    # We turn off the glow and hover_color so it doesn't confusingly "highlight" when hovered
    sivo_app.map(
        "status_dot",
        tooltip="Waiting for live connection...",
        glow=False,
        hover_color="transparent"
    )

    # Use a Data URI to return a static JSON array that confirms data was received and parsed natively
    # Returns: [{"id": "status_dot", "color": "#10b981", "tooltip": "Connected: Data successfully received and processed."}]
    mock_api_url = "data:application/json,%5B%7B%22id%22%3A%22status_dot%22%2C%22color%22%3A%22%2310b981%22%2C%22tooltip%22%3A%22Connected%3A%20Data%20successfully%20received%20and%20processed.%22%7D%5D"

    # Bind the mock API endpoint with a 3-second delay to show the "before" and "after" state
    sivo_app.bind_api(
        url=mock_api_url,
        polling_interval_ms=3000,
        method="GET"
    )

    output_path = os.path.join(os.path.dirname(__file__), "live_api_example.html")
    sivo_app.to_html(output_path)
    print(f"Live API Polling example generated at {output_path}")

if __name__ == "__main__":
    main()
