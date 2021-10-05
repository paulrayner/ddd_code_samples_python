import unittest
import datetime
from terms_and_conditions import TermsAndConditions

class TestTermsAndConditions(unittest.TestCase):

    def test_terms_and_conditions_status(self):
        terms_and_conditions  = TermsAndConditions(datetime.date(2009, 5, 8), datetime.date(2010, 5, 8), datetime.date(2013, 5, 8))

        # Should be pending prior to effective date
        self.assertEqual(terms_and_conditions.status(datetime.date(2010, 5, 7)), "PENDING")
        self.assertEqual(terms_and_conditions.status(datetime.date(2010, 5, 8)), "ACTIVE")
        self.assertEqual(terms_and_conditions.status(datetime.date(2013, 5, 8)), "ACTIVE")
        self.assertEqual(terms_and_conditions.status(datetime.date(2013, 5, 9)), "EXPIRED")

    def test_terms_and_conditions_extend_annually(self):
        terms_and_conditions  = TermsAndConditions(datetime.date(2009, 5, 8), datetime.date(2010, 5, 8), datetime.date(2013, 5, 8))

        extended_terms_and_conditions = TermsAndConditions(datetime.date(2009, 5, 8), datetime.date(2010, 5, 8), datetime.date(2014, 5, 8))
        self.assertEqual(terms_and_conditions.annually_extended(), extended_terms_and_conditions)



    def test_terms_and_conditions_equality(self):
        terms_and_conditions  = TermsAndConditions(datetime.date(2009, 5, 8), datetime.date(2010, 5, 8), datetime.date(2013, 5, 8))

        # Should be equal based on properties
        self.assertEqual(TermsAndConditions(datetime.date(2009, 5, 8), datetime.date(2010, 5, 8), datetime.date(2013, 5, 8)), terms_and_conditions)

    def test_terms_and_conditions_inequality(self):
        terms_and_conditions  = TermsAndConditions(datetime.date(2009, 5, 8), datetime.date(2010, 5, 8), datetime.date(2013, 5, 8))

        # Demonstrate inequality by property
        self.assertNotEqual(TermsAndConditions(datetime.date(2009, 5, 5), datetime.date(2010, 5, 8), datetime.date(2013, 5, 8)), terms_and_conditions)
        self.assertNotEqual(TermsAndConditions(datetime.date(2009, 5, 8), datetime.date(2010, 5, 5), datetime.date(2013, 5, 8)), terms_and_conditions)
        self.assertNotEqual(TermsAndConditions(datetime.date(2009, 5, 8), datetime.date(2010, 5, 8), datetime.date(2013, 5, 5)), terms_and_conditions)

if __name__ == '__main__':
    unittest.main()
