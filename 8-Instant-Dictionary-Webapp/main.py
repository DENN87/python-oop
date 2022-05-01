import justpy as jp

from webapp.dictionary import Dictionary
from webapp.home import Home
from webapp.about import About


jp.Route(Dictionary.path, Dictionary.serve)
jp.Route(Home.path, Home.serve)
jp.Route(About.path, About.serve)

jp.justpy(port=8001)
