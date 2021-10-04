import unittest
import uuid
import copy
import datetime
from contract import Contract
from product import Product
from claim import Claim
from terms_and_conditions import TermsAndConditions

class TestContract(unittest.TestCase):

    def test_contract_is_set_up_correctly(self):
        product  = Product("dishwasher", "OEUOEU23", "Whirlpool", "7DP840CWDB0")
        terms_and_conditions  = TermsAndConditions(datetime.datetime(2010, 5, 7), datetime.datetime(2010, 5, 8), datetime.datetime(2013, 5, 8))
        contract = Contract(100.0, product, terms_and_conditions)

        self.assertTrue(hasattr(contract, "id"))
        self.assertEqual(contract.purchase_price, 100.0)
        self.assertEqual(contract.status, "PENDING")
        self.assertEqual(Product("dishwasher", "OEUOEU23", "Whirlpool", "7DP840CWDB0"), contract.product)
        self.assertEqual(contract.terms_and_conditions, terms_and_conditions)

    def test_contract_in_effect_for_dates(self):
        product  = Product("dishwasher", "OEUOEU23", "Whirlpool", "7DP840CWDB0")
        terms_and_conditions  = TermsAndConditions(datetime.datetime(2010, 5, 7), datetime.datetime(2010, 5, 8), datetime.datetime(2013, 5, 8))
        contract = Contract(100.0, product, terms_and_conditions)

        # Check (default) pending state
        self.assertFalse(contract.in_effect_for(datetime.datetime(2010, 5, 9)))

        # Check date range for active contract
        contract.status = "ACTIVE"
        self.assertFalse(contract.in_effect_for(datetime.datetime(2010, 5, 7)))
        self.assertTrue(contract.in_effect_for(datetime.datetime(2010, 5, 8)))
        self.assertTrue(contract.in_effect_for(datetime.datetime(2013, 5, 8)))
        self.assertFalse(contract.in_effect_for(datetime.datetime(2013, 5, 9)))

    def test_contract_limit_of_liability_no_claims(self):
        product  = Product("dishwasher", "OEUOEU23", "Whirlpool", "7DP840CWDB0")
        terms_and_conditions  = TermsAndConditions(datetime.datetime(2010, 5, 7), datetime.datetime(2010, 5, 8), datetime.datetime(2013, 5, 8))
        contract = Contract(100.0, product, terms_and_conditions)

        self.assertEqual(contract.limit_of_liability(), 80.0)

    def test_contract_limit_of_liability_multiple_claims(self):
        product  = Product("dishwasher", "OEUOEU23", "Whirlpool", "7DP840CWDB0")
        terms_and_conditions  = TermsAndConditions(datetime.datetime(2010, 5, 7), datetime.datetime(2010, 5, 8), datetime.datetime(2013, 5, 8))
        contract = Contract(100.0, product, terms_and_conditions)

        contract.claims.append(Claim(10.0, datetime.datetime(2010, 5, 8)))
        contract.claims.append(Claim(20.0, datetime.datetime(2010, 5, 8)))

        self.assertEqual(contract.limit_of_liability(), 50.0)

    def test_contract_extend_annual_subscription(self):
        product  = Product("dishwasher", "OEUOEU23", "Whirlpool", "7DP840CWDB0")
        terms_and_conditions  = TermsAndConditions(datetime.datetime(2010, 5, 7), datetime.datetime(2010, 5, 8), datetime.datetime(2013, 5, 8))
        contract = Contract(100.0, product, terms_and_conditions)

        contract.extend_annual_subscription()

        extended_terms_and_conditions  = TermsAndConditions(datetime.datetime(2010, 5, 7), datetime.datetime(2010, 5, 8), datetime.datetime(2014, 5, 8))
        self.assertEqual(extended_terms_and_conditions, contract.terms_and_conditions)

    # entities compare by unique IDs, not properties
    def test_contract_equality(self):
        product  = Product("dishwasher", "OEUOEU23", "Whirlpool", "7DP840CWDB0")
        terms_and_conditions  = TermsAndConditions(datetime.datetime(2010, 5, 7), datetime.datetime(2010, 5, 8), datetime.datetime(2013, 5, 8))

        contract1 = Contract(100.0, product, terms_and_conditions)
        contract2 = Contract(100.0, product, terms_and_conditions)
        contract3 = Contract(100.0, product, terms_and_conditions)

        expected_id = uuid.uuid1()
        contract1.id = expected_id
        contract2.id = expected_id
        self.assertEqual(contract1, contract2)

        contract3.id = uuid.uuid1()
        self.assertNotEqual(contract1, contract3)

if __name__ == '__main__':
    unittest.main()
