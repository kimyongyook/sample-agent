import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from sample_agent import is_allowed_webhook


class WebhookAllowlistTests(unittest.TestCase):
    def test_allows_expected_webhook_url(self):
        self.assertTrue(is_allowed_webhook("https://hooks.example.com/events"))


if __name__ == "__main__":
    unittest.main()
