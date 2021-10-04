import datetime
from dataclasses import dataclass

@dataclass(frozen=True)
class TermsAndConditions:
    purchase_date: datetime
    effective_date: datetime
    expiration_date: datetime

    def status(self, date):
      if date < self.effective_date:
          return "PENDING"
      if date > self.expiration_date:
          return "EXPIRED"
      return "ACTIVE"

    def annually_extended(self):
      extended_expiration_date = datetime.datetime(self.expiration_date.year + 1, self.expiration_date.month, self.expiration_date.day)
      return TermsAndConditions(self.purchase_date, self.effective_date, extended_expiration_date)
