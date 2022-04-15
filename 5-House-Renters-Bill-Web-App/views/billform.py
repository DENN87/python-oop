from flask import render_template
from flask.views import MethodView
from wtforms import StringField, SubmitField, Form


class BillFormPage(MethodView):

    def get(self):
        bill_form = BillForm()
        return render_template('bill_form.html',
                               bill_form=bill_form)


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

