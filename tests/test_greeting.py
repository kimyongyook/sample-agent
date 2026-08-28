import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from sample_agent import greeting


class GreetingTests(unittest.TestCase):
    def test_greeting_normalizes_surrounding_whitespace(self):
        self.assertEqual(greeting("  POC  "), "Hello, POC!")

    def test_greeting_rejects_empty_name(self):
        with self.assertRaises(ValueError):
            greeting("  ")


if __name__ == "__main__":
    unittest.main()

