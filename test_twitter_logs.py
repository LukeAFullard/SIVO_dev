from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        b = p.chromium.launch()
        page = b.new_page()
        page.on("console", lambda msg: print(f"Console: {msg.text}"))
        page.on("pageerror", lambda err: print(f"Error: {err}"))
        page.goto('http://localhost:8001/test_twitter_v2.html')
        page.wait_for_timeout(4000)
        b.close()

run()
