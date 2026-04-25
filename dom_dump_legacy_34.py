from playwright.sync_api import sync_playwright

def run(page):
    page.goto("file:///app/examples/advanced/34_dashboard_fade_in/dashboard_fade.html")
    page.wait_for_timeout(500)
    page.screenshot(path="/tmp/legacy_34_start.png")

    page.wait_for_timeout(5000)
    page.screenshot(path="/tmp/legacy_34_end.png")

if __name__ == "__main__":
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()
        try:
            run(page)
        finally:
            context.close()
            browser.close()
