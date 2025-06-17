class CashPayment:
    def pay(self, amount):
        print(f"Paid {amount} with cash")

class CreditPayment:
    def pay(self, amount):
        print(f"Paid {amount} with credit")

class PaymentContext:
    def __init__(self, strategy):
        self.strategy = strategy

    def execute(self, amount):
        self.strategy.pay(amount)

# Penggunaan
context = PaymentContext(CreditPayment())
context.execute(100)
