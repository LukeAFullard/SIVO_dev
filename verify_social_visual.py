import subprocess
import time
import os
from playwright.sync_api import sync_playwright

def run_test():
    server = subprocess.Popen(["python", "-m", "http.server", "8000", "--directory", "examples/9_social_embeds"])
    time.sleep(2)  # Wait for server to start

    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            context = browser.new_context()
            page = context.new_page()

            print("Loading page...")
            page.goto("http://localhost:8000/output.html", wait_until="networkidle")
            time.sleep(2)

            # Helper to trigger click and wait
            def trigger_click_and_screenshot(element_id, output_file):
                print(f"Triggering click for {element_id}...")
                page.evaluate(f"myChart.dispatchAction({{type: 'downplay', seriesIndex: 0}})")
                page.evaluate(f"myChart.trigger('click', {{componentType: 'series', name: '{element_id}'}})")
                time.sleep(4)  # Wait for info panel to slide in and iframe to load
                page.screenshot(path=output_file)
                print(f"Saved {output_file}")

            # Twitter/X
            trigger_click_and_screenshot("btn_twitter", "/home/jules/verification/social_twitter_new.png")

            # Instagram
            trigger_click_and_screenshot("btn_insta", "/home/jules/verification/social_insta_new.png")

            # TikTok
            trigger_click_and_screenshot("btn_tiktok", "/home/jules/verification/social_tiktok_new.png")

            # Facebook
            trigger_click_and_screenshot("btn_fb", "/home/jules/verification/social_fb_new.png")

            browser.close()
    finally:
        server.terminate()
        print("Done")

if __name__ == "__main__":
    run_test()
