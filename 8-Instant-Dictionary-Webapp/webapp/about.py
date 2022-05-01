import justpy as jp


class About:
    path = "/about"

    def serve(self):
        wp = jp.QuasarPage(tailwind=True)
        div = jp.Div(a=wp, classes="bg-gray-200 h-screen")
        jp.Div(a=div, text="This is the About page!", classes="text-4xl m-2")
        jp.Div(a=div, text="""
            Bavaria ipsum dolor sit amet Radler Schneid vui huift vui ognudelt i mechad dee 
            Schwoanshaxn Zwedschgndadschi a bissal wos gehd ollaweil. Measi a ganze es i mog di fei aasgem, 
            Blosmusi. Schmankal zwoa Ramasuri Edlweiss. Wia vo de Weiznglasl wos, imma hogg di hera Guglhupf! Schorsch 
            Spotzerl schnacksln Weiznglasl vui gschmeidig a ganze auf der Oim, da gibt’s koa Sünd, etza! 
            """, classes="text-lg")

        return wp


jp.Route(About.path, About.serve)
jp.justpy(port=8001)
