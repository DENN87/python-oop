from flask import render_template, request
from flask.views import MethodView
from wtforms import StringField, Form, SubmitField

from models.calorie import Calorie
from models.temperature import Temperature

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
