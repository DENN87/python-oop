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

    def pays(self, bill, renters_list):
        days = [r.days_in_house for r in renters_list]
        to_pay = self.days_in_house / sum(days) * bill.amount

        return round(to_pay, 2)
