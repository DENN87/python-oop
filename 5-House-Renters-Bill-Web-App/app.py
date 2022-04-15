from flask import Flask

from views.home import HomePage
from views.billform import BillFormPage
from views.results import ResultsPage

app = Flask(__name__)

app.add_url_rule('/', view_func=HomePage.as_view('index'))
app.add_url_rule('/bill', view_func=BillFormPage.as_view('bill_form'))
app.add_url_rule('/results', view_func=ResultsPage.as_view('results'))

app.run()
