import uuid
import datetime
from dataclasses import dataclass

@dataclass(frozen=True)
class SubscriptionRenewed:
    contract_id: uuid
    reason: str
    occurred_on: datetime = datetime.date.today()
