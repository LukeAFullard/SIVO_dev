import pytest
from playwright.sync_api import Page, expect
import os
import sys
import tempfile

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'src')))
from sivo import Sivo
from sivo.core.project import SivoProject

def test_a11y_keyboard_navigation(page: Page):
    """
    Test keyboard navigation and a11y DOM elements.
    """
    app1 = Sivo.from_string("<svg><rect id='r1'/><rect id='r2'/></svg>", presentation_order=["r1", "r2"], default_panel_position="right")

    # Map a11y actions implicitly via map() arguments
    app1.map("r1", html="<div id='p-r1'>Panel 1</div>", aria_label="First Rect", role="button", tabindex="0")
    app1.map("r2", html="<div id='p-r2'>Panel 2</div>", aria_label="Second Rect", role="button", tabindex="0")

    with tempfile.NamedTemporaryFile(suffix=".html", delete=False) as f:
        temp_name = f.name

    try:
        app1.to_html(output_path=temp_name)
        page.goto(f"file://{temp_name}")

        # Wait for ECharts wrapper
        wrapper = page.locator("#chart-wrapper")
        expect(wrapper).to_be_attached()

        # Give some time for DOM generation
        page.wait_for_timeout(1000)

        # Check a11y container
        a11y_container = page.locator("#a11y-container")
        expect(a11y_container).to_be_attached()

        # Check ARIA roles and labels are generated
        r1_a11y = page.locator(".a11y-focus-target[aria-label='First Rect']")
        expect(r1_a11y).to_be_attached()

        r2_a11y = page.locator(".a11y-focus-target[aria-label='Second Rect']")
        expect(r2_a11y).to_be_attached()

        # Test keyboard navigation for presentation mode
        # Press ArrowRight
        page.keyboard.press("ArrowRight")
        page.wait_for_timeout(1000)
        # Should activate 'r1' panel
        panel_r1 = page.locator("#p-r1")
        expect(panel_r1).to_be_visible()

        # Press ArrowRight
        page.keyboard.press("ArrowRight")
        page.wait_for_timeout(1000)
        # Should activate 'r2' panel
        panel_r2 = page.locator("#p-r2")
        expect(panel_r2).to_be_visible()

        # Press ArrowLeft
        page.keyboard.press("ArrowLeft")
        page.wait_for_timeout(1000)
        # Should be back to 'r1' panel
        expect(panel_r1).to_be_visible()

        # Test Tabbing to a11y node and triggering click
        page.keyboard.press("Escape") # Close panel
        page.wait_for_timeout(1000)

        r1_a11y.focus()
        page.keyboard.press("Enter")
        page.wait_for_timeout(1000)
        expect(panel_r1).to_be_visible()

    finally:
        os.remove(temp_name)
