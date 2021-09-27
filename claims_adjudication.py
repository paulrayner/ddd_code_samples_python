import uuid
import datetime
from product import Product

class ClaimsAdjudication:
  def adjudicate(contract, new_claim):
    claim_total = sum(claim.amount for claim in contract.claims)
    if((contract.purchase_price - claim_total) * 0.8 > new_claim.amount) and contract.status == "ACTIVE" and new_claim.failure_date >= contract.effective_date and new_claim.failure_date <= contract.expiration_date:
        contract.claims.append(new_claim)
