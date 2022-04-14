from flask.views import MethodView
from wtforms import Form, StringField, SubmitField
from flask import Flask, render_template, request

from resources.bill import Bill
from resources.housemate import HouseMate
from resources.pdfreport import PdfReport

app = Flask(__name__)

class HomePage(MethodView):

    def get(self):
        return render_template('index.html')


class BillFormPage(MethodView):

    def get(self):
        bill_form = BillForm()
        return render_template('bill_form.html',
                               bill_form=bill_form)


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

        return render_template('results.html',
                               renter_1=renter_1,
                               amount_1=renter_1.pays(the_bill, renters),
                               renter_2=renter_2,
                               amount_2=renter_2.pays(the_bill, renters),
                               renter_3=renter_3,
                               amount_3=renter_3.pays(the_bill, renters),
                               )


class BillForm(Form):
    amount = StringField("Bill Amount: ")
    period = StringField("Bill Period: ")

    name1 = StringField("Name: ")
    days_in_house1 = StringField("Days in the house: ")

    name2 = StringField("Name: ")
    days_in_house2 = StringField("Days in the house: ")

    name3 = StringField("Name: ")
    days_in_house3 = StringField("Days in the house: ")

    button = SubmitField("Calculate")


app.add_url_rule('/', view_func=HomePage.as_view('index'))
app.add_url_rule('/bill', view_func=BillFormPage.as_view('bill_form'))
app.add_url_rule('/results', view_func=ResultsPage.as_view('results'))

app.run()
