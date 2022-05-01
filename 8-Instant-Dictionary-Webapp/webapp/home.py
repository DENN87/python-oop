import justpy as jp

class Home:
    path = "/"

    def serve(self):
        wp = jp.QuasarPage(tailwind=True)
        div = jp.Div(a=wp, classes="bg-gray-200 h-screen")
        jp.Div(a=div, text="This is the Home page!", classes="text-4xl m-2")
        jp.Div(a=div, text="""
                    Home ipsum crackalackin black amet, sizzle adipiscing ass. Bizzle we gonna chung velizzle, pimpin' volutpizzle, suscipit brizzle, the bizzle vizzle, arcu. Pellentesque egizzle tortor. Sed erizzle. Fusce izzle pizzle dapibizzle turpizzle tempizzle for sure. Maurizzle pellentesque nibh bow wow wow izzle. Sizzle izzle tortor. 
                    """, classes="text-lg")

        return wp
