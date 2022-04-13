class Bill:

    def __init__(self, amount, period):
        self.amount = amount
        self.period = period

    def __repr__(self):
        return f"The bill for {self.period} was {self.amount}$"


bill = Bill(3000, "March 2022")
print(bill)

