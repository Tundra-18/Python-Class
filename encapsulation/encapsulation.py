# #without encapsulation
# class BankAccount:
#     def __init__(self,balance):
#         self.balance = balance
#
# account = BankAccount(5000)
# print("Balance is",account.balance)
#
# account.balance = 6000
# print("Balance is",account.balance)

#with encapsulation
class BankAccount:
    def __init__(self,balance):
        self.__balance = balance
    def deposit(self,d_amount):
        self.__balance += d_amount
    def show_balance(self):
        print("Balance is", self.__balance)

account = BankAccount(5000)
account.show_balance()

account.deposit(2000)
account.show_balance()

account.__balance = 6000
account.show_balance()


