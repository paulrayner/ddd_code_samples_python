import uuid
import datetime

from repair_po import RepairPO

# Claim represents a request for a benefit on an extended warranty.
# It contains a set of purchase orders that provide information about
# any repairs and associated costs that may have occurred for a claim.

class Claim:
  def __init__(self, amount, failure_date):
    self.id           = uuid.uuid1() # auto assigned unique id
    self.amount       = amount
    self.failure_date = failure_date

  def __eq__(self, other):
    if not isinstance(other, Claim):
        return NotImplemented

    return self.id == other.id
