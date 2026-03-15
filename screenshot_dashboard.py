import os
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.set_viewport_size({"width": 375, "height": 667}) # iPhone size
    file_url = f"file://{os.path.abspath('examples/59_infographic_templates/dashboard_infographic.html')}"
    page.goto(file_url)
    page.wait_for_timeout(2000)
    page.screenshot(path="dashboard_screenshot_mobile.png")
    browser.close()
