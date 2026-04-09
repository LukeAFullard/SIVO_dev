import pytest
from playwright.sync_api import Page, expect
import os
import sys
import tempfile

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'src')))
from sivo.core.dashboard import SivoDashboard
from sivo import Sivo

def test_dashboard_render(page: Page):
    """
    Test that a basic SIVO Dashboard renders its layout blocks properly.
    """
    dash = SivoDashboard(title="Test E2E Dash")
    app1 = Sivo.from_string("<svg><rect id='r'/></svg>")
    dash.add_sivo_block("block1", app1)
    dash.add_html_block("block2", "<div id='test-html'>Hello</div>")

    with tempfile.NamedTemporaryFile(suffix=".html", delete=False) as f:
        temp_name = f.name

    try:
        dash.to_html(output_path=temp_name)
        page.goto(f"file://{temp_name}")

        # Check if dashboard wrapper exists
        wrapper = page.locator(".dashboard-container")
        expect(wrapper).to_be_visible()

        # Check if the title rendered
        title = page.locator("h1", has_text="Test E2E Dash")
        expect(title).to_be_visible()

        # Check html block
        html_block = page.locator("#test-html")
        expect(html_block).to_have_text("Hello")

        # Check ECharts initialization logic is present
        echarts_container = page.locator("#container-block1")
        expect(echarts_container).to_be_visible()
    finally:
        os.remove(temp_name)
