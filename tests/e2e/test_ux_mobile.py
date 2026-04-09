import pytest
from playwright.sync_api import Page, expect
import os
import sys
import tempfile

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'src')))
from sivo import Sivo

def test_mobile_touch_interactions(browser):
    """
    Test touch events and resizing behavior on a simulated mobile device.
    """
    context = browser.new_context(
        viewport={'width': 375, 'height': 667},
        is_mobile=True,
        has_touch=True
    )
    page = context.new_page()

    app = Sivo.from_string("<svg><rect id='r1'/></svg>", default_panel_position="bottom")
    app.map("r1", html="<div id='p-r1'>Mobile Panel</div>")

    with tempfile.NamedTemporaryFile(suffix=".html", delete=False) as f:
        temp_name = f.name

    try:
        app.to_html(output_path=temp_name)
        page.goto(f"file://{temp_name}")

        wrapper = page.locator("#chart-wrapper")
        expect(wrapper).to_be_attached()

        page.wait_for_timeout(1000)

        # Simulate click
        page.evaluate("window.triggerElementClick('r1')")

        panel = page.locator("#p-r1")
        expect(panel).to_be_visible()

        # Test close button on mobile
        close_btn = page.locator("button[onclick='closePanel()']")
        expect(close_btn).to_be_visible()
        close_btn.click()

        # Panel should close
        expect(panel).not_to_be_visible()

    finally:
        os.remove(temp_name)
        context.close()
