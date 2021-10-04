import uuid
import datetime
from product import Product
from terms_and_conditions import TermsAndConditions

# Contract represents an extended warranty for a covered product.
# A contract is in a PENDING state prior to the effective date,
# ACTIVE between effective and expiration dates, and EXPIRED after
# the expiration date.

class Contract:
  def __init__(self, purchase_price, product: Product, terms_and_conditions: TermsAndConditions):
    self.id                   = uuid.uuid1() # auto assigned unique id
    self.purchase_price       = purchase_price
    self.status               = "PENDING"
    self.product              = product
    self.terms_and_conditions = terms_and_conditions
    self.claims               = []

  def covers(self, claim):
     return self.in_effect_for(claim.failure_date) and self.within_limit_of_liability(claim.amount)

  def within_limit_of_liability(self, amount):
     return amount < self.limit_of_liability()

  def in_effect_for(self, failure_date):
    return self.terms_and_conditions.status(failure_date) == "ACTIVE" and self.status == "ACTIVE"

  def limit_of_liability(self):
    LIABILITY_PERCENTAGE = 0.8
    claim_total = sum(claim.amount for claim in self.claims)
    return (self.purchase_price * LIABILITY_PERCENTAGE) - claim_total

  def extend_annual_subscription(self):
     self.terms_and_conditions = self.terms_and_conditions.annually_extended()

  def __eq__(self, other):
    if not isinstance(other, Contract):
        return NotImplemented

    return self.id == other.id
