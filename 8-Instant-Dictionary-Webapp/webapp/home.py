import justpy as jp

from webapp.layout import DefaultLayout


class Home:
    path = "/"

    @classmethod
    def serve(cls, req):
        wp = jp.QuasarPage(tailwind=True)

        lay_out = DefaultLayout(a=wp)

        container = jp.QPageContainer(a=lay_out)

        div = jp.Div(a=container, classes="bg-gray-200 h-screen")
        jp.Div(a=div, text="This is the Home page!", classes="text-4xl p-2")
        jp.Div(a=div, text="""
                    Home ipsum crackalackin black amet, sizzle adipiscing ass. Bizzle we gonna chung velizzle, pimpin' volutpizzle, suscipit brizzle, the bizzle vizzle, arcu. Pellentesque egizzle tortor. Sed erizzle. Fusce izzle pizzle dapibizzle turpizzle tempizzle for sure. Maurizzle pellentesque nibh bow wow wow izzle. Sizzle izzle tortor. 
                    """, classes="text-lg p-2")

        return wp
