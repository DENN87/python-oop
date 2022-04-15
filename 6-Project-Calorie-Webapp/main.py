from flask import Flask

from views.caloriesform import CaloriesFormPage
from views.homepage import HomePage

app = Flask(__name__)


app.add_url_rule('/', view_func=HomePage.as_view('index'))
app.add_url_rule('/calories-form', view_func=CaloriesFormPage.as_view('calories_form_page'))

if __name__ == "__main__":
    app.run(port=5000, debug=True)
