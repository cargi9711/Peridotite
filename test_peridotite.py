import unittest
from peridotite import Peridotite

class TestPeridotite(unittest.TestCase):
    def test_describe(self):
        p = Peridotite("Test", "Minerals", 3.0)
        self.assertIn("density", p.describe())

if __name__ == "__main__":
    unittest.main()
