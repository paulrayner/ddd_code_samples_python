import unittest
import datetime
from contract import Contract
from product import Product
from claim import Claim
from claims_adjudication import ClaimsAdjudication
from terms_and_conditions import TermsAndConditions

class TestAdjudicateValidClaim(unittest.TestCase):

    def fake_contract(self):
        product  = Product("dishwasher", "OEUOEU23", "Whirlpool", "7DP840CWDB0")
        terms_and_conditions  = TermsAndConditions(datetime.datetime(2010, 5, 7), datetime.datetime(2010, 5, 8), datetime.datetime(2013, 5, 8))
        contract = Contract(100.0, product, terms_and_conditions)
        contract.status = "ACTIVE"
        return contract

    # Now that we have this logic moved to Contract, we could mock out contract.covers() and simplify these tests
    def test_adjudicate_valid_claim(self):
        contract = self.fake_contract()

        claim = Claim(79.0, datetime.datetime(2010, 5, 8))

        ClaimsAdjudication.adjudicate(contract, claim)
        self.assertEqual(len(contract.claims), 1)
        self.assertEqual(contract.claims[0].amount, 79.0)
        self.assertEqual(contract.claims[0].failure_date, datetime.datetime(2010, 5, 8))

    def test_adjudicate_claim_with_invalid_amount(self):
        contract = self.fake_contract()

        claim = Claim(81.0, datetime.datetime(2010, 5, 8))

        ClaimsAdjudication.adjudicate(contract, claim)
        self.assertEqual(len(contract.claims), 0)

    def test_adjudicate_claim_for_pending_contract(self):
        contract = self.fake_contract()
        contract.status = "PENDING"

        claim = Claim(79.0, datetime.datetime(2010, 5, 8))

        ClaimsAdjudication.adjudicate(contract, claim)
        self.assertEqual(len(contract.claims), 0)

    def test_adjudicate_claim_for_expired_contract(self):
        contract = self.fake_contract()
        contract.status = "EXPIRED"

        claim = Claim(79.0, datetime.datetime(2010, 5, 8))

        ClaimsAdjudication.adjudicate(contract, claim)
        self.assertEqual(len(contract.claims), 0)

    def test_adjudicate_claim_prior_to_effective_date(self):
        contract = self.fake_contract()

        claim = Claim(79.0, datetime.datetime(2010, 5, 5))

        ClaimsAdjudication.adjudicate(contract, claim)
        self.assertEqual(len(contract.claims), 0)

    def test_adjudicate_claim_after_expiration_date(self):
        contract = self.fake_contract()

        claim = Claim(79.0, datetime.datetime(2013, 5, 9))

        ClaimsAdjudication.adjudicate(contract, claim)
        self.assertEqual(len(contract.claims), 0)

if __name__ == '__main__':
    unittest.main()
