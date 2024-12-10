from credit_card import CreditCard
from bank_info import BankInfo, BankCustomer, PersonalInfo
from decorators import PlatinumCreditCard, VIPCustomer

credit_card = CreditCard("Philip Davidson", "2205694786", 25000.0, 60, "265")
bank_info = BankInfo("Credo Bank", "Anna Senna", ["2578554067"])

personal_info = PersonalInfo(name="Anna Senna", age=24, address="29, Rockford Street, New York, NY 10117")
customer = BankCustomer(personal_info, bank_info)

platinum_card = PlatinumCreditCard(credit_card)
print("Platinum Credit Card Details:", platinum_card.give_details())

vip_customer = VIPCustomer(customer)
print("VIP Customer Details:", vip_customer.give_details())
