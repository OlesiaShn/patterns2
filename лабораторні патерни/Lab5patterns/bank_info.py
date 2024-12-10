from dataclasses import dataclass
from typing import List

class BankInfo:
    def __init__(self, bank_name: str, holder_name: str, accounts_number: List[str]):
        self.bank_name = bank_name
        self.holder_name = holder_name
        self.accounts_number = accounts_number
        self.credit_history = {}

    def transaction_list(self, account_number: str) -> List[str]:
        return ["Transaction 1", "Transaction 2", "Transaction 3"]


@dataclass
class PersonalInfo:
    name: str
    age: int
    address: str


class BankCustomer:
    def __init__(self, personal_info: PersonalInfo, bank_details: BankInfo):
        self.personal_info = personal_info
        self.bank_details = bank_details

    def give_details(self) -> dict:
        return {
            "personal_info": self.personal_info,
            "bank_info": {
                "bank_name": self.bank_details.bank_name,
                "holder_name": self.bank_details.holder_name,
                "accounts_number": self.bank_details.accounts_number,
                "credit_history": self.bank_details.credit_history,
                "transactions": {acc: self.bank_details.transaction_list(acc) for acc in self.bank_details.accounts_number}
            }
        }
