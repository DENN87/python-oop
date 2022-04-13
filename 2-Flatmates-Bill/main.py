class Bill:
    """
    Object that contains data about a bill, such as
    total amount and period of the bill.
    """

    def __init__(self, amount, period):
        self.amount = amount
        self.period = period

    def __repr__(self):
        return f"The bill for {self.period} was ${self.amount}"


class HouseMate:
    """
    Creates a house mate person who lives in the
    house and pays a share of the bill.
    """

    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house

    def __repr__(self):
        return f"{self.name} was in the house for {self.days_in_house} days."

    def pays(self, bill, renter_2):
        return (self.days_in_house / (self.days_in_house + renter_2.days_in_house)) * bill.amount

class PdfReport:
    """
    Creates a PDF file that contains data about
    the house mates such as their names, their
    due amount and the period of the bill.
    """

    def __init__(self, filename):
        self.filename = filename


current_bill = Bill(800, "March 2022")
print(current_bill)

bob = HouseMate("Bob", 15)
anne = HouseMate("Anne", 25)

print(f"{bob} Sharing ${bob.pays(current_bill, anne)} of the total bill.")
print(f"{anne} Sharing ${anne.pays(current_bill, bob)} of the total bill.")
