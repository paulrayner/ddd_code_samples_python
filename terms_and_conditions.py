import datetime
from dataclasses import dataclass

@dataclass(frozen=True)
class TermsAndConditions:
    purchase_date: datetime.date
    effective_date: datetime.date
    expiration_date: datetime.date

    def status(self, date):
      if date < self.effective_date:
          return "PENDING"
      if date > self.expiration_date:
          return "EXPIRED"
      return "ACTIVE"

    def annually_extended(self):
      extended_expiration_date = datetime.date(self.expiration_date.year + 1, self.expiration_date.month, self.expiration_date.day)
      return TermsAndConditions(self.purchase_date, self.effective_date, extended_expiration_date)
