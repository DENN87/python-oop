import json

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

        response = {
            "word": word,
            "definition": definition.Definition(word).get()
        }

        wp.html = json.dumps(response)

        return wp


jp.Route("/api", Api.serve)
jp.justpy()
