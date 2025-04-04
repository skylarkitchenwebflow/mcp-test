import unittest
from src.main import greet


class TestMain(unittest.TestCase):
    def test_greet(self):
        """Test the greet function with a sample name."""
        result = greet("World")
        self.assertEqual(result, "Hello, World!")


if __name__ == "__main__":
    unittest.main()
