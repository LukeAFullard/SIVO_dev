import os
from sivo import Sivo

def main():
    # Simple SVG with regions
    svg = """
    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 300 100">
        <circle id="sensor_1" cx="50" cy="50" r="40" fill="#ccc" />
        <circle id="sensor_2" cx="150" cy="50" r="40" fill="#ccc" />
        <circle id="sensor_3" cx="250" cy="50" r="40" fill="#ccc" />

        <text x="50" y="55" font-family="Arial" font-size="12" fill="black" text-anchor="middle" pointer-events="none">Sensor 1</text>
        <text x="150" y="55" font-family="Arial" font-size="12" fill="black" text-anchor="middle" pointer-events="none">Sensor 2</text>
        <text x="250" y="55" font-family="Arial" font-size="12" fill="black" text-anchor="middle" pointer-events="none">Sensor 3</text>
    </svg>
    """

    sivo_app = Sivo.from_string(svg, title="Live API Polling Example")

    # Map the sensors initially
    sivo_app.map("sensor_1", tooltip="Waiting for API data...")
    sivo_app.map("sensor_2", tooltip="Waiting for API data...")
    sivo_app.map("sensor_3", tooltip="Waiting for API data...")

    # Bind to a hypothetical REST API endpoint
    # This example assumes the API returns a JSON array:
    # [{"id": "sensor_1", "color": "red", "tooltip": "Alert!"}, ...]

    # Use a Data URI to simulate an API returning JSON data that SIVO can natively parse:
    # [{"id": "sensor_1", "color": "red", "tooltip": "Alert!"}, {"id": "sensor_2", "color": "orange", "tooltip": "Warning"}]
    mock_api_url = "data:application/json,%5B%7B%22id%22%3A%22sensor_1%22%2C%22color%22%3A%22red%22%2C%22tooltip%22%3A%22Alert%21%22%7D%2C%7B%22id%22%3A%22sensor_2%22%2C%22color%22%3A%22orange%22%2C%22tooltip%22%3A%22Warning%22%7D%5D"

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
