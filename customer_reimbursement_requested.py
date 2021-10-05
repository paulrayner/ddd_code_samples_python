import uuid
import datetime
from dataclasses import dataclass

@dataclass(frozen=True)
class CustomerReimbursementRequested:
    contract_id: uuid
    rep_name: str
    reason: str
    occurred_on: datetime.date = datetime.date.today()
