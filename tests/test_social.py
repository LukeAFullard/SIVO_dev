import unittest
from sivo.core.actions import SocialAction

class TestSocialAction(unittest.TestCase):
    def test_social_action(self):
        action = SocialAction(provider="wikipedia", url="https://en.wikipedia.org/wiki/Python_(programming_language)")
        self.assertEqual(action.action_type, "social")
        self.assertEqual(action.provider, "wikipedia")
        self.assertEqual(action.url, "https://en.wikipedia.org/wiki/Python_(programming_language)")

if __name__ == '__main__':
    unittest.main()
