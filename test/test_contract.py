import unittest
import uuid
import copy
import datetime
from contract import Contract
from product import Product

class TestContract(unittest.TestCase):

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

    def test_contract_equality(self):
        product  = Product("dishwasher", "OEUOEU23", "Whirlpool", "7DP840CWDB0")
        contract1 = Contract(100.0, product, datetime.datetime(2010, 5, 8), datetime.datetime(2013, 5, 8), datetime.datetime(2010, 5, 7))
        contract2 = Contract(100.0, product, datetime.datetime(2010, 5, 8), datetime.datetime(2013, 5, 8), datetime.datetime(2010, 5, 7))
        contract3 = Contract(100.0, product, datetime.datetime(2010, 5, 8), datetime.datetime(2013, 5, 8), datetime.datetime(2010, 5, 7))

        expected_id = uuid.uuid1()
        contract1.id = expected_id
        contract2.id = expected_id
        self.assertEqual(contract1, contract2)

        contract3.id = uuid.uuid1()
        self.assertNotEqual(contract1, contract3)

if __name__ == '__main__':
    unittest.main()
