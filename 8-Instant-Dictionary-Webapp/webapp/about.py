import justpy as jp
from webapp.layout import DefaultLayout


class About:
    path = "/about"

    def serve(self):
        wp = jp.QuasarPage(tailwind=True)

        lay_out = DefaultLayout(a=wp)

        container = jp.QPageContainer(a=lay_out)

        div = jp.Div(a=container, classes="bg-gray-200 h-screen")
        jp.Div(a=div, text="This is the About page!", classes="text-4xl p-2")
        jp.Div(a=div, text="""
            Bavaria ipsum dolor sit amet Radler Schneid vui huift vui ognudelt i mechad dee 
            Schwoanshaxn Zwedschgndadschi a bissal wos gehd ollaweil. Measi a ganze es i mog di fei aasgem, 
            Blosmusi. Schmankal zwoa Ramasuri Edlweiss. Wia vo de Weiznglasl wos, imma hogg di hera Guglhupf! Schorsch 
            Spotzerl schnacksln Weiznglasl vui gschmeidig a ganze auf der Oim, da gibt’s koa Sünd, etza! 
            """, classes="text-lg")

        return wp
