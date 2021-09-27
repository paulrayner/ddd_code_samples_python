import uuid

class LineItem:
  def __init__(self, type, amount, description):
    self.type = type
    self.amount = amount
    self.description = description
