import uuid
import datetime

from repair_po import RepairPO

class Claim:
  def __init__(self, amount, failure_date):
    self.amount       = amount
    self.failure_date = failure_date

        # autoassigned
    self.id           = uuid.uuid1()

  def __eq__(self, other):
    if not isinstance(other, Claim):
        return NotImplemented

    return self.id == other.id
