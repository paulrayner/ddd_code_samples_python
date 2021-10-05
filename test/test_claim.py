import uuid
import unittest
import datetime

from claim import Claim
from repair_po import RepairPO
from line_item import LineItem

class TestClaim(unittest.TestCase):

    def test_claim_is_set_up_correctly(self):
        repair_po = RepairPO()
        line_item1 = LineItem("PARTS", 45.0, "Replacement part for soap dispenser")
        line_item2 = LineItem("LABOR", 50.0, "1 hour repair")
        repair_po.line_items = [line_item1, line_item2]

        claim = Claim(100.0, datetime.date(2010, 5, 8))
        claim.repair_pos = [repair_po]

        self.assertEqual(claim.amount, 100.0)
        self.assertEqual(claim.failure_date, datetime.date(2010, 5, 8))
        self.assertEqual(claim.repair_pos[0].line_items[0].type, "PARTS")
        self.assertEqual(claim.repair_pos[0].line_items[0].amount, 45.0)
        self.assertEqual(claim.repair_pos[0].line_items[0].description, "Replacement part for soap dispenser")

    def test_claim_equality(self):
        claim1 = Claim(100.0, datetime.date(2010, 5, 8))
        claim2 = Claim(100.0, datetime.date(2010, 5, 8))
        claim3 = Claim(100.0, datetime.date(2010, 5, 8))

        expected_id = uuid.uuid1()
        claim1.id = expected_id
        claim2.id = expected_id
        self.assertEqual(claim1, claim2)

        claim3.id = uuid.uuid1()
        self.assertNotEqual(claim1, claim3)

if __name__ == '__main__':
    unittest.main()
