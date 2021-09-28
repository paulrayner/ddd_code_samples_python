import uuid
import datetime
from product import Product

# Contract represents an extended warranty for a covered product.
# A contract is in a PENDING state prior to the effective date,
# ACTIVE between effective and expiration dates, and EXPIRED after
# the expiration date.

class Contract:
  def __init__(self, purchase_price, product: Product, effective_date, expiration_date, purchase_date):
    self.id              = uuid.uuid1() # auto assigned unique id
    self.purchase_price  = purchase_price
    self.status          = "PENDING"
    self.product         = product
    self.effective_date  = effective_date
    self.expiration_date = expiration_date
    self.purchase_date   = purchase_date
    self.claims          = []

  def __eq__(self, other):
    if not isinstance(other, Contract):
        return NotImplemented

    return self.id == other.id
