import justpy as jp

class Docs:
    path = "/"

    def serve(self):
        wp = jp.WebPage()

        div = jp.Div(a=wp, classes="bg-gray-200 h-screen p-5")

        jp.Div(a=div, text="English Dictionary API", classes="text-4xl text-center")
        jp.Div(a=div, text="Get definitions of words: ", classes="text-lg")
        jp.Hr(a=div)
        jp.Div(a=div, text="www.example.com/api?w=sun")
        jp.Hr(a=div)
        jp.Div(a=div, text="""
            {"word": "sun", "definition": ["Any star, especially when seen as the centre of any single solar system.", 
            "The particular star at the centre of our solar system, from which the Earth gets light and heat."]} 
            """)

        return wp
