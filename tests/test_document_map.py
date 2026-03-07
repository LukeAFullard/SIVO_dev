import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from sivo.core.actions import DocumentAction, MapAction
from sivo.core.sivo import Sivo
from pydantic import ValidationError

class TestDocumentMapEmbed(unittest.TestCase):

    def test_document_action_validation(self):
        # Valid URL
        action = DocumentAction(document_url="https://example.com/file.pptx")
        self.assertEqual(action.action_type, "document")
        self.assertEqual(action.document_url, "https://example.com/file.pptx")

        # Missing URL should raise ValidationError
        with self.assertRaises(ValidationError):
            DocumentAction()

    def test_map_action_validation(self):
        action = MapAction(map_location="Eiffel Tower, Paris")
        self.assertEqual(action.action_type, "map")
        self.assertEqual(action.map_location, "Eiffel Tower, Paris")

        with self.assertRaises(ValidationError):
            MapAction()

    def test_mapping_in_sivo(self):
        svg_string = '''<svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
            <rect id="my-doc" width="10" height="10"/>
            <rect id="my-map" width="10" height="10"/>
        </svg>'''
        sivo_app = Sivo.from_string(svg_string)

        # Map actions
        sivo_app.map("my-doc", document="https://example.com/sample.pptx")
        sivo_app.map("my-map", map_location="Tokyo, Japan")

        doc_mapping = sivo_app.infographic.mappings["my-doc"]
        self.assertEqual(doc_mapping.id, "my-doc")
        self.assertEqual(doc_mapping.actions[0].action_type, "document")
        self.assertEqual(doc_mapping.actions[0].document_url, "https://example.com/sample.pptx")

        map_mapping = sivo_app.infographic.mappings["my-map"]
        self.assertEqual(map_mapping.id, "my-map")
        self.assertEqual(map_mapping.actions[0].action_type, "map")
        self.assertEqual(map_mapping.actions[0].map_location, "Tokyo, Japan")

if __name__ == '__main__':
    unittest.main()
