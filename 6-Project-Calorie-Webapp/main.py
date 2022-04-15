from flask.views import MethodView
from wtforms import Form, StringField, SubmitField
from flask import Flask, render_template, request

from calorie import Calorie
from temperature import Temperature


app = Flask(__name__)


class HomePage(MethodView):

    def get(self):
        return render_template('index.html')


class CaloriesFormPage(MethodView):

    def get(self):
        pass

    def post(self):
        pass


class CaloriesForm(Form):
    pass


app.add_url_rule('/', view_func=HomePage.as_view('home_page'))
app.add_url_rule('/calories-form', view_func=CaloriesFormPage.as_view('calories_form_page'))

if __name__ == "__main__":
    app.run(port=5000, debug=True)
