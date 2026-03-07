import unittest
from sivo.core.actions import SocialAction

class TestSocialAction(unittest.TestCase):
    def test_social_action(self):
        action = SocialAction(provider="twitter", url="https://x.com/SIVO")
        self.assertEqual(action.action_type, "social")
        self.assertEqual(action.provider, "twitter")
        self.assertEqual(action.url, "https://x.com/SIVO")

if __name__ == '__main__':
    unittest.main()
