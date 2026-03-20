import os
from sivo import Sivo

def main():
    # 1. Initialize Sivo with our SVG
    base_dir = os.path.dirname(os.path.abspath(__file__))
    svg_path = os.path.join(base_dir, "sample.svg")

    app = Sivo.from_svg(svg_path)

    # 2. Map actions to elements
    # Add Google Analytics event to box1
    app.map(
        "box1",
        tooltip="Click to track event",
        html="<h3>Google Analytics</h3><p>Clicking this fires a Google Analytics event (if gtag is loaded).</p>",
        analytics={
            "provider": "google_analytics",
            "event_name": "clicked_box1",
            "payload": {"source": "sivo_demo"}
        }
    )

    # Add a public API fetch to circle1 (e.g., retrieving a public JSON file or sheet proxy)
    app.map(
        "circle1",
        tooltip="Click to fetch live data",
        datasource={
            "provider": "google_sheets",
            "api_endpoint": "https://jsonplaceholder.typicode.com/users/1"
        }
    )

    # 3. Export to HTML
    output_path = os.path.join(base_dir, "interactive_analytics_data.html")
    app.to_html(output_path)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    main()
