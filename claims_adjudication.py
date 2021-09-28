import uuid
import datetime
from product import Product

# Adjudicate/adjudication - a judgment made on a claim to determine
# whether we are legally obligated to process the claim against the
# warranty. From Wikipedia (https://en.wikipedia.org/wiki/Adjudication):
#
# "Claims adjudication" is a phrase used in the insurance industry
# to refer to the process of paying claims submitted or denying them
# after comparing claims to the benefit or coverage requirements.

class ClaimsAdjudication:
  @classmethod
  def adjudicate(cls, contract, new_claim):
    claim_total = sum(claim.amount for claim in contract.claims)
    if((contract.purchase_price - claim_total) * 0.8 > new_claim.amount) and contract.status == "ACTIVE" and new_claim.failure_date >= contract.effective_date and new_claim.failure_date <= contract.expiration_date:
        contract.claims.append(new_claim)
