from flask import render_template, request
from flask.views import MethodView

from .billform import BillForm

from resources.bill import Bill
from resources.housemate import HouseMate
from resources.pdfreport import PdfReport, FileShare


class ResultsPage(MethodView):

    def post(self):
        bill_form = BillForm(request.form)

        the_bill = Bill(bill_form.amount.data, bill_form.period.data)

        renters = []

        renter_1 = HouseMate(bill_form.name1.data, bill_form.days_in_house1.data)
        renters.append(renter_1)

        renter_2 = HouseMate(bill_form.name2.data, bill_form.days_in_house2.data)
        renters.append(renter_2)

        renter_3 = HouseMate(bill_form.name3.data, bill_form.days_in_house3.data)
        renters.append(renter_3)

        # Creating instance of class PdfReport
        pdf_report = PdfReport("bill_results.pdf")

        # Generate PDF file with data
        pdf_report.generate_pdf(renters, the_bill)

        file_to_share = FileShare(pdf_report.filename)

        pdf_url = file_to_share.share()

        return render_template('results.html',
                               renter_1=renter_1,
                               amount_1=renter_1.pays(the_bill, renters),
                               renter_2=renter_2,
                               amount_2=renter_2.pays(the_bill, renters),
                               renter_3=renter_3,
                               amount_3=renter_3.pays(the_bill, renters),
                               pdf_url=pdf_url
                               )
