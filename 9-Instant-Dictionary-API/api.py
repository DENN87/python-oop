import justpy as jp
import definition

class Api:
    """
    Handles requests at /api?w=word
    """
    @classmethod
    def serve(cls, req):
        wp = jp.WebPage()
        word = req.query_params.get('w')
        wp.html = {'word': word.title(),
                   'definition': definition.Definition(word.title()).get()}

        return wp


jp.Route("/api", Api.serve)
jp.justpy()
