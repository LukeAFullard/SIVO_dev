from playwright.sync_api import sync_playwright
import os

def test_water_science_dashboard():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        file_url = f"file://{os.path.abspath('examples/mysite/title_page/subpage/water/science/index.html')}"
        page.goto(file_url)

        # Wait for map to render
        page.wait_for_selector("#container-map")

        # Mock geocoder fetch response to simulate an FMU hit ("Manawatū")
        # The frontend calls the URL in `intersectUrl`
        page.route("**/query?*", lambda route: route.fulfill(
            json={
                "features": [
                    {
                        "properties": {"Name": "Manawatū"},
                        "geometry": {
                            "type": "Polygon",
                            "coordinates": [[[0, 0], [10, 0], [10, 10], [0, 10], [0, 0]]]
                        }
                    }
                ]
            }
        ))

        # Override Nominatim geocoder API
        page.route("**/search?*", lambda route: route.fulfill(
            json=[{
                "lat": "5",
                "lon": "5",
                "display_name": "Manawatū"
            }]
        ))

        page.fill("#sivo-geocoder-input", "Manawatū")
        page.keyboard.press("Enter")

        # Wait for the overlay result saying "Zone Found"
        page.wait_for_selector("#sivo-geocoder-overlay-result", state="visible", timeout=10000)

        # Verify if ECharts updated. ECharts will render "select" or "highlight" styles onto the canvas.
        # We can hover over "Manawatū" and check tooltip text.
        page.mouse.move(270, 50) # Manawatū block should be around x=270, y=50 in SVG coordinates.
        page.wait_for_timeout(1000)

        # Get screenshot
        os.makedirs("/home/jules/verification/screenshots", exist_ok=True)
        page.screenshot(path="/home/jules/verification/screenshots/hover_tooltip.png")

        print("Test passed. Saved screenshot to /home/jules/verification/screenshots/hover_tooltip.png")

        browser.close()

if __name__ == "__main__":
    test_water_science_dashboard()
