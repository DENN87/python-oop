from flask.views import MethodView
from wtforms import Form, StringField, SubmitField
from flask import Flask, render_template

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

    def get(self):
        return render_template('results.html')


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
