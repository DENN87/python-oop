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

    def pays(self, bill, renters_list):
        days = [r.days_in_house for r in renters_list]
        to_pay = self.days_in_house / sum(days) * bill.amount

        return round(to_pay, 2)


class PdfReport:
    """
    Creates a PDF file that contains data about
    the house mates such as their names, their
    due amount and the period of the bill.
    """

    def __init__(self, filename):
        self.filename = filename

    def generate_pdf(self, renters_list, bill):
        pdf = FPDF(orientation='P', unit='pt', format='letter')
        pdf.add_page()
        pdf.set_fill_color(228, 233, 190)

        # Adding a image
        pdf.image(name="files/house.png", x=532, y=40, w=50, h=50)

        # Insert Line
        pdf.set_line_width(2)
        pdf.line(30, 30, 582, 30)
        pdf.set_line_width(0)

        # Insert title
        pdf.set_font(family='Helvetica', size=24, style='B')
        pdf.cell(w=0, h=80, txt="ROOM RENTAL INVOICE", border=0, align="L", ln=1)

        # Insert Invoice Number & Period
        pdf.set_left_margin(382)
        pdf.set_font(family='Helvetica', size=12, style='B')
        pdf.cell(w=100, h=20, txt="Invoice #", border=1, align="L", fill=1)
        pdf.set_font(family='Helvetica', size=12)
        pdf.cell(w=100, h=20, txt="1000003", border=1, align="L", ln=1)
        pdf.set_font(family='Helvetica', size=12, style='B')
        pdf.cell(w=100, h=20, txt="Invoice date", border=1, align="L", fill=1)
        pdf.set_font(family='Helvetica', size=12)
        pdf.cell(w=100, h=20, txt=bill.period, border=1, align="L", ln=1)
        pdf.set_left_margin(28.35)
        pdf.ln()

        # Insert Line
        pdf.set_line_width(2)
        pdf.line(30, 220, 582, 220)
        pdf.set_line_width(0)

        # PDF Body
        pdf.ln()
        pdf.ln()
        pdf.ln()
        pdf.ln()

        # Define cell column names
        pdf.set_font(family='Helvetica', size=12, style='B')
        pdf.cell(w=100, h=20, txt="Renter Name", border=1, align="C", fill=1)
        pdf.cell(w=250, h=20, txt="Room Description", border=1, align="C", fill=1)
        pdf.cell(w=100, h=20, txt="Days Rented", border=1, align="C", fill=1)
        pdf.cell(w=0, h=20, txt="Total ($)", border=1, align="C", fill=1, ln=1)

        # Insert Renters details
        for renter in renters_list:
            pdf.set_font(family='Helvetica', size=12, style='I')
            pdf.cell(w=100, h=20, txt=renter.name, border=1, align="C")
            pdf.cell(w=250, h=20, txt="Shared House", border=1, align="C")
            pdf.cell(w=100, h=20, txt=str(renter.days_in_house), border=1, align="C")
            pdf.cell(w=0, h=20, txt=str(renter.pays(bill, renters_list)), border=1, align="C", ln=1)

        # Total Bill amount
        pdf.set_font(family='Helvetica', size=12, style='B')
        pdf.cell(w=100, h=20, txt="", border=0, align="C")
        pdf.cell(w=250, h=20, txt="", border=0, align="C")
        pdf.cell(w=100, h=20, txt="Total ($)", border=1, align="C", fill=1)
        pdf.cell(w=0, h=20, txt=str(bill.amount), border=1, align="C", fill=1, ln=1)

        # Write to file
        pdf.output(self.filename)


# Main block
print("Welcome to Invoice Generator ! \n")

# Get House Bill details
bill_amount = int(input("What was the bill amount: "))
bill_period = input("What was the bill period: ")

# Get number of renters
renters_number = int(input("Enter the number of renters you had: "))

# Collect each renter details and create instances of class HouseMate
renters = []
for renter in range(renters_number):
    print(f"\nEnter details for Renter {renter + 1}")
    name = input("What is the name: ")
    days = int(input("How many days lived in: "))
    renters.append(HouseMate(name, days))

# Creating instance of class Bill
current_bill = Bill(bill_amount, bill_period)

# Creating instance of class PdfReport
pdf_report = PdfReport("Report1.pdf")

# Generate PDF file with data
pdf_report.generate_pdf(renters, current_bill)
