from playwright.sync_api import sync_playwright
import time

def verify():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.on("console", lambda msg: print(f"Browser console: {msg.type}: {msg.text}"))
        page.on("pageerror", lambda err: print(f"Browser error: {err}"))
        page.goto("http://localhost:8080/index.html")
        time.sleep(2)

        print("Clicking Sediment card")
        page.locator("#card-card_sediment").click()
        time.sleep(1)

        print("Clicking state button")
        page.locator("#card-sediment_btn_state").click()
        time.sleep(1)

        page.wait_for_selector("#sivo-full-page-overlay", timeout=5000)
        time.sleep(2)

        browser.close()

if __name__ == "__main__":
    verify()
