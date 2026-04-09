import pytest
from playwright.sync_api import Page, expect
import os
import sys
import tempfile

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'src')))
from sivo.core.project import SivoProject
from sivo import Sivo
from sivo.core.actions import DrillDownAction

def test_multi_view_project(page: Page):
    project = SivoProject(initial_view_id="view1")

    app1 = Sivo.from_string("<svg><rect id='r1'/></svg>")
    # Add drilldown action to app1 mapped to view2
    app1.map("r1", drill_to="view2")

    app2 = Sivo.from_string("<svg><rect id='r2'/></svg>")

    project.add_view("view1", app1)
    project.add_view("view2", app2)

    with tempfile.NamedTemporaryFile(suffix=".html", delete=False) as f:
        temp_name = f.name

    try:
        project.to_html(output_path=temp_name)
        page.goto(f"file://{temp_name}")

        # In a real environment, Playwright would wait for the ECharts canvas to be rendered.
        # Check if chart container exists.
        echarts_container = page.locator("#chart-container")
        expect(echarts_container).to_be_visible()

    finally:
        os.remove(temp_name)
