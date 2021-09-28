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
  def limit_of_liability(cls, contract):
    claim_total = sum(claim.amount for claim in contract.claims)
    return (contract.purchase_price - claim_total) * 0.8

  @classmethod
  def in_effect_for(cls, contract, failure_date):
    return contract.status == "ACTIVE" and failure_date >= contract.effective_date and failure_date <= contract.expiration_date

  @classmethod
  def adjudicate(cls, contract, new_claim):
    if(cls.limit_of_liability(contract) > new_claim.amount) and cls.in_effect_for(contract, new_claim.failure_date):
        contract.claims.append(new_claim)
