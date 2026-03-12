import pytest
from playwright.sync_api import Page, expect
import os

@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        "ignore_https_errors": True
    }

def test_sivo_render(page: Page):
    """
    Test that a basic SIVO HTML output renders the ECharts canvas properly.
    """
    # Note: For this to work in a real environment, you must first generate `test_bind_data.html`
    # or serve it via an HTTP server. For the purposes of this scaffold, we check if the file exists
    # and load it directly.
    file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'test_bind_data.html'))

    if not os.path.exists(file_path):
        pytest.skip("Test HTML file not generated. Run `python examples/08_data_binding/main.py` first.")

    page.goto(f"file://{file_path}")

    # ECharts renders into a div with a specific id
    echarts_container = page.locator("#chart-container")
    expect(echarts_container).to_be_visible()

    # ECharts usually creates a canvas or SVG inside
    canvas = echarts_container.locator("div").first
    expect(canvas).to_be_visible()

    # Check if the wrapper container exists
    wrapper = page.locator("#chart-wrapper")
    expect(wrapper).to_be_attached()
