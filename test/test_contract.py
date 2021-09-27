import unittest
import copy
import datetime
from contract import Contract
from product import Product

class TestClaimsAdjudication(unittest.TestCase):

    def test_contract_is_set_up_correctly(self):
        product  = Product("dishwasher", "OEUOEU23", "Whirlpool", "7DP840CWDB0")
        contract = Contract(100.0, product, datetime.datetime(2010, 5, 8), datetime.datetime(2013, 5, 8), datetime.datetime(2010, 5, 7))

        self.assertTrue(hasattr(contract, "id"))
        self.assertEqual(contract.purchase_price, 100.0)
        self.assertEqual(contract.status, "PENDING")
        self.assertEqual(Product("dishwasher", "OEUOEU23", "Whirlpool", "7DP840CWDB0"), contract.product)
        self.assertEqual(contract.purchase_date, datetime.datetime(2010, 5, 7))
        self.assertEqual(contract.effective_date, datetime.datetime(2010, 5, 8))
        self.assertEqual(contract.expiration_date, datetime.datetime(2013, 5, 8))

if __name__ == '__main__':
    unittest.main()
