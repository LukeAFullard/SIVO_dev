import sys
import os
import unittest
import tempfile

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from sivo.core.dashboard import SivoDashboard
from sivo import Sivo

class TestDashboard(unittest.TestCase):
    def test_dashboard_initialization(self):
        dash = SivoDashboard(title="My Dash", columns=4, template="sidebar_left")
        self.assertEqual(dash.title, "My Dash")
        self.assertEqual(dash.columns, 4)
        self.assertEqual(dash.template_name, "sidebar_left")
        self.assertEqual(len(dash.blocks), 0)

    def test_add_blocks(self):
        dash = SivoDashboard()
        sivo_app = Sivo.from_string("<svg><rect id='r'/></svg>")

        dash.add_sivo_block("block1", sivo_app, col_span=2, slot="header", grid_area="h")
        self.assertIn("block1", dash.blocks)
        self.assertEqual(dash.layout_order[0]["type"], "sivo")
        self.assertEqual(dash.layout_order[0]["id"], "block1")
        self.assertEqual(dash.layout_order[0]["col_span"], 2)
        self.assertEqual(dash.layout_order[0]["slot"], "header")
        self.assertEqual(dash.layout_order[0]["grid_area"], "h")

        dash.add_html_block("block2", "<div>Hello</div>", col_span=1, slot="main", grid_area="m")
        self.assertIn("block2", dash.html_blocks)
        self.assertEqual(dash.layout_order[1]["type"], "html")

        dash.add_details_panel("block3", title="Detail", placeholder="Wait", col_span=1, slot="side", grid_area="s")
        self.assertIn("block3", dash.details_panels)
        self.assertEqual(dash.details_panels["block3"]["title"], "Detail")
        self.assertEqual(dash.layout_order[2]["type"], "details")

        dash.add_metrics_panel("block4", title="Metr", metrics=["m1", "m2"], col_span=1, slot="main", grid_area="mt")
        self.assertIn("block4", dash.metrics_panels)
        self.assertEqual(dash.metrics_panels["block4"]["title"], "Metr")
        self.assertEqual(dash.layout_order[3]["type"], "metrics")

    def test_set_grid_layout(self):
        dash = SivoDashboard()
        dash.set_grid_layout(desktop='"h h" "m s"', mobile='"h" "m" "s"')
        self.assertEqual(dash.desktop_grid, '"h h" "m s"')
        self.assertEqual(dash.mobile_grid, '"h" "m" "s"')

    def test_to_html(self):
        dash = SivoDashboard()

        # Test empty dash exception
        with self.assertRaises(ValueError):
            dash.to_html()

        sivo_app = Sivo.from_string("<svg><rect id='r'/></svg>")
        dash.add_sivo_block("block1", sivo_app)
        dash.add_html_block("block2", "<p>hi</p>")

        # Test generating string
        html = dash.to_html()
        self.assertIn("block1", html)
        self.assertIn("block2", html)
        self.assertIn("<p>hi</p>", html)

        # Test generating to file
        with tempfile.NamedTemporaryFile(suffix=".html", delete=False) as f:
            temp_name = f.name

        try:
            dash.to_html(output_path=temp_name)
            with open(temp_name, "r") as f:
                content = f.read()
            self.assertIn("block1", content)
            self.assertIn("block2", content)
        finally:
            os.remove(temp_name)

if __name__ == '__main__':
    unittest.main()
