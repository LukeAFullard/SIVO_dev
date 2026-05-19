from playwright.sync_api import sync_playwright
import time

def verify():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("http://localhost:8080/index.html")
        time.sleep(2)

        # Click Suspended Sediment card
        page.locator("#card-card_sediment").click()
        time.sleep(1)

        # Click the state button
        page.locator("#card-sediment_btn_state").click()
        time.sleep(1)

        # Wait for the popup and the iframe to load
        page.wait_for_selector("#sivo-full-page-overlay")
        time.sleep(2)

        page.screenshot(path="verification_after_click.png")
        print("Screenshot saved to verification_after_click.png")

        browser.close()

if __name__ == "__main__":
    verify()
