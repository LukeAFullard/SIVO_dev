from playwright.sync_api import sync_playwright

def run_cuj(page):
    page.goto("file:///app/examples/mysite/title_page/subpage/air/science/index.html")
    page.wait_for_timeout(5000)

    # Take screenshot at the key moment
    page.screenshot(path="/home/jules/verification/screenshots/verification_updated.png", full_page=True)
    page.wait_for_timeout(1000)  # Hold final state for the video

if __name__ == "__main__":
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(
            record_video_dir="/home/jules/verification/videos"
        )
        page = context.new_page()
        try:
            run_cuj(page)
        finally:
            context.close()  # MUST close context to save the video
            browser.close()
