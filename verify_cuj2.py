import sys
import os
import time

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))

from playwright.sync_api import sync_playwright

def verify():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={'width': 1200, 'height': 800})

        url = f"file://{os.path.abspath('examples/mysite/title_page/subpage/air/help/index.html')}"
        page.goto(url)
        time.sleep(2)

        os.makedirs('/home/jules/verification/screenshots', exist_ok=True)

        page.screenshot(path='/home/jules/verification/screenshots/hover_glow_test_3.png')
        print("Screenshot saved to /home/jules/verification/screenshots/hover_glow_test_3.png")

        browser.close()

if __name__ == "__main__":
    verify()
