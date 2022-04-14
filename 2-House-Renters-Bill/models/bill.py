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
