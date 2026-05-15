from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self):
        print("This is pay.")

class KBZPay(Payment):
    def pay(self):
        print("Paid with KBZPay")

class VisaCard(Payment):
    def pay(self):
        print("Paid with Visa Card")
k = KBZPay()
v = VisaCard()
k.pay()
v.pay()


