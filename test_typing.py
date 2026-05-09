from playwright.sync_api import sync_playwright

def test():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto("http://localhost:8080/annotator_template.html")
        page.evaluate('''
            window.parent = { pyodide: { FS: { syncfs: (b, cb) => cb() } }, showToast: () => {} };
        ''')
        page.click("summary", force=True)
        page.wait_for_timeout(500)

        # We will trigger the actual file upload with a mock image file
        import base64
        mock_png = base64.b64decode("iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAACklEQVR4nGMAAQAABQABDQottAAAAABJRU5ErkJggg==")
        with open("mock.png", "wb") as f:
            f.write(mock_png)

        # Force display of tools to be absolutely sure
        page.evaluate('''
            document.getElementById('tools').style.display = 'block';
            document.getElementById('canvas-container').style.display = 'block';
        ''')
        page.wait_for_timeout(500)

        page.click("#tool-rect", force=True)
        page.wait_for_timeout(500)

        canvas = page.locator("#draw-canvas")
        box = canvas.bounding_box()
        if box:
            page.mouse.move(box['x'] + 10, box['y'] + 10)
            page.mouse.down()
            page.mouse.move(box['x'] + 15, box['y'] + 15)
            page.mouse.up()

        page.wait_for_selector(".shape-item input")
        input_box = page.locator(".shape-item input").first

        # Focus and type one character at a time using keyboard to simulate real user
        input_box.focus()
        # Delete default text first
        input_box.press("Control+A")
        input_box.press("Backspace")

        page.keyboard.type("abc")
        page.wait_for_timeout(200)

        val = input_box.input_value()
        print(f"Text box value is: '{val}'")

test()
