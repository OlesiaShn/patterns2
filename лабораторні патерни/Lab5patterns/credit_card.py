import hashlib

class CreditCard:
    def __init__(self, client: str, account_number: str, credit_limit: float, grace_period: int, cvv: str):
        self.client = client
        self.account_number = account_number
        self.credit_limit = credit_limit
        self.grace_period = grace_period
        self._cvv = self.encrypt(cvv)
    @property
    def cvv(self):
        return self.decrypt(self._cvv)

    @cvv.setter
    def cvv(self, value):
        self._cvv = self.encrypt(value)

    def encrypt(self, value: str) -> str:
        return hashlib.sha256(value.encode()).hexdigest()

    def decrypt(self, value: str) -> str:
        #просто повертає хеш
        return value

    def give_details(self) -> dict:
        return {
            "client": self.client,
            "account_number": self.account_number,
            "credit_limit": self.credit_limit,
            "grace_period": self.grace_period,
            "cvv": self._cvv
        }
