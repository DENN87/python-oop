class Bill:

    def __init__(self, amount, period):
        self.amount = amount
        self.period = period

    def __repr__(self):
        return f"The bill for {self.period} was {self.amount}$"


bill = Bill(3000, "March 2022")
print(bill)


class HouseMate:

    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house

    def __repr__(self):
        return f"{self.name} was in the house for {self.days_in_house} days."


mate_1 = HouseMate("Bob", 15)
print(mate_1)
