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
        calories_form = CaloriesForm()

        return render_template('calories_form_page.html',
                               calories_form=calories_form)

    def post(self):
        calories_form = CaloriesForm(request.form)

        temp = Temperature(calories_form.country.data, calories_form.city.data)

        calorie = Calorie(
            float(calories_form.weight.data),
            float(calories_form.height.data),
            float(calories_form.age.data),
            temp.get()
        )

        return render_template('calories_form_page.html',
                               calories_form=calories_form,
                               calories=calorie.calculate(),
                               result=True)


class CaloriesForm(Form):
    weight = StringField("Weight (kg):")
    height = StringField("Height (cm):")
    age = StringField("Age:")
    country = StringField("Country:", default="USA")
    city = StringField("City:", default="San Francisco")
    button = SubmitField("Calculate My Calories")


app.add_url_rule('/', view_func=HomePage.as_view('index'))
app.add_url_rule('/calories-form', view_func=CaloriesFormPage.as_view('calories_form_page'))

if __name__ == "__main__":
    app.run(port=5000, debug=True)
