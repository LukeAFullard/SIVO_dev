import sys
import os
import shutil
from playwright.sync_api import sync_playwright

def verify_frontend():
    output_dir = "/home/jules/verification"
    os.makedirs(os.path.join(output_dir, "screenshots"), exist_ok=True)
    os.makedirs(os.path.join(output_dir, "videos"), exist_ok=True)

    file_path = os.path.abspath("examples/mysite/title_page/subpage/land/index.html")

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(record_video_dir=os.path.join(output_dir, "videos"))
        page = context.new_page()

        page.goto(f"file://{file_path}")
        page.wait_for_timeout(2000)

        screenshot_path = os.path.join(output_dir, "screenshots", "verification_updated.png")
        page.screenshot(path=screenshot_path, full_page=True)

        context.close()
        browser.close()

        video_files = [f for f in os.listdir(os.path.join(output_dir, "videos")) if f.endswith(".webm")]
        video_path = os.path.join(output_dir, "videos", video_files[0]) if video_files else None

        print(f"Screenshot saved to: {screenshot_path}")
        if video_path:
            print(f"Video saved to: {video_path}")

if __name__ == "__main__":
    verify_frontend()
