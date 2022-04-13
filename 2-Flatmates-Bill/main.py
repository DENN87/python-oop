from fpdf import FPDF


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
        return round(self.days_in_house / (self.days_in_house + renter_2.days_in_house) * bill.amount, 2)


class PdfReport:
    """
    Creates a PDF file that contains data about
    the house mates such as their names, their
    due amount and the period of the bill.
    """

    def __init__(self, filename):
        self.filename = filename

    def generate_pdf(self, renter_1, renter_2, bill):
        pdf = FPDF(orientation='P', unit='pt', format='letter')
        pdf.add_page()

        # Insert title
        pdf.set_font(family='Helvetica', size=24, style='B')
        pdf.cell(w=0, h=80, txt="Housemates Bill", border=1, align="C", ln=1)

        # Insert Period label and value
        pdf.set_font(family='Helvetica', size=14, style='B')
        pdf.cell(w=100, h=30, txt="Period", border=1, align="C")
        pdf.cell(w=150, h=30, txt=bill.period, border=1, align="C", ln=1)

        # Insert Renters
        pdf.set_font(family='Helvetica', size=12, style='I')
        pdf.cell(w=100, h=20, txt=renter_1.name, border=1, align="C")
        pdf.cell(w=150, h=20, txt=str(renter_1.pays(bill, renter_2)), border=1, align="C", ln=1)

        pdf.cell(w=100, h=20, txt=renter_2.name, border=1, align="C")
        pdf.cell(w=150, h=20, txt=str(renter_2.pays(bill, renter_1)), border=1, align="C")

        # Write to file
        pdf.output(self.filename)


current_bill = Bill(700, "March 2022")
print(current_bill)

bob = HouseMate("Bob", 21)
anne = HouseMate("Anne", 27)

print(f"{bob} Sharing ${bob.pays(current_bill, anne)} of the total bill.")
print(f"{anne} Sharing ${anne.pays(current_bill, bob)} of the total bill.")


pdf_report = PdfReport("Report1.pdf")
pdf_report.generate_pdf(bob, anne, current_bill)
