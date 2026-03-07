import unittest
from sivo.core.actions import PdfAction
from sivo.core.sivo import Sivo
from pydantic import ValidationError

class TestPdfEmbed(unittest.TestCase):

    def test_pdf_action_validation(self):
        # Valid URL
        action = PdfAction(pdf_url="https://example.com/file.pdf")
        self.assertEqual(action.action_type, "pdf")
        self.assertEqual(action.pdf_url, "https://example.com/file.pdf")

        # Missing URL should raise ValidationError
        with self.assertRaises(ValidationError):
            PdfAction()

    def test_pdf_mapping_in_sivo(self):
        svg_string = '''<svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg"><rect id="my-pdf" width="10" height="10"/></svg>'''
        sivo_app = Sivo.from_string(svg_string)

        # Map a PDF action
        sivo_app.map("my-pdf", pdf="https://example.com/sample.pdf")

        mapping = sivo_app.infographic.mappings["my-pdf"]

        self.assertEqual(mapping.id, "my-pdf")
        self.assertEqual(mapping.actions[0].action_type, "pdf")
        self.assertEqual(mapping.actions[0].pdf_url, "https://example.com/sample.pdf")

if __name__ == '__main__':
    unittest.main()
