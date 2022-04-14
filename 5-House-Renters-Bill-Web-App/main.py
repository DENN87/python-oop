from resources.bill import Bill
from resources.housemate import HouseMate
from resources.pdfreport import PdfReport


print("Welcome to House Invoice Generator ! \n")

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

print("Report generated successfully !")
