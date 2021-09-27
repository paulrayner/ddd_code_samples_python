import unittest
from product import Product

class TestProduct(unittest.TestCase):

    def test_product_equality_by_properties(self):
        # A value object must be created whole
        product  = Product("dishwasher", "OEUOEU23", "Whirlpool", "7DP840CWDB0")

        # Should be equal based on properties
        self.assertEqual(Product("dishwasher", "OEUOEU23", "Whirlpool", "7DP840CWDB0"), product)

    def test_product_inequality_by_properties(self):
        product  = Product("dishwasher", "OEUOEU23", "Whirlpool", "7DP840CWDB0")

        self.assertNotEqual(Product("stove", "OEUOEU23", "Whirlpool", "7DP840CWDB0"), product)
        self.assertNotEqual(Product("dishwasher", "BEUOEU23", "Whirlpool", "7DP840CWDB0"), product)
        self.assertNotEqual(Product("dishwasher", "OEUOEU23", "Maytag", "7DP840CWDB0"), product)
        self.assertNotEqual(Product("dishwasher", "OEUOEU23", "Whirlpool", "99999999"), product)

if __name__ == '__main__':
    unittest.main()
