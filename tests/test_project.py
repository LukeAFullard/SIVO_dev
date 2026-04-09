import sys
import os
import unittest
import tempfile

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from sivo.core.project import SivoProject
from sivo import Sivo

class TestProject(unittest.TestCase):
    def test_project_initialization(self):
        project = SivoProject(initial_view_id="main_view")
        self.assertEqual(project.initial_view_id, "main_view")
        self.assertEqual(len(project.views), 0)

    def test_add_view(self):
        project = SivoProject("main_view")
        app = Sivo.from_string("<svg><rect id='r'/></svg>")
        project.add_view("main_view", app)
        self.assertIn("main_view", project.views)
        self.assertEqual(project.views["main_view"], app)

    def test_to_html(self):
        project = SivoProject("main_view")

        # Test exception when initial view is missing
        with self.assertRaises(ValueError):
            project.to_html()

        app1 = Sivo.from_string("<svg><rect id='r1'/></svg>")
        app2 = Sivo.from_string("<svg><rect id='r2'/></svg>")

        project.add_view("main_view", app1)
        project.add_view("secondary_view", app2)

        # Generate HTML as string
        html = project.to_html()
        self.assertIn("main_view", html)
        self.assertIn("secondary_view", html)

        # Generate HTML to file
        with tempfile.NamedTemporaryFile(suffix=".html", delete=False) as f:
            temp_name = f.name

        try:
            project.to_html(output_path=temp_name)
            with open(temp_name, "r") as f:
                content = f.read()
            self.assertIn("main_view", content)
            self.assertIn("secondary_view", content)
        finally:
            os.remove(temp_name)

if __name__ == '__main__':
    unittest.main()
