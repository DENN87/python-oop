import justpy as jp

class Home:
    path = "/"

    @classmethod
    def serve(cls, req):
        wp = jp.QuasarPage(tailwind=True)

        layout = jp.QLayout(a=wp, view="hHh lpR fFf")
        header = jp.QHeader(a=layout)
        toolbar = jp.QToolbar(a=header)

        drawer = jp.QDrawer(a=layout, show_if_above=True, v_mode="left", bordered=True)
        jp.QBtn(a=toolbar, dense=True, flat=True, round=True, icon="menu", click=cls.move_drawer, drawer=drawer)

        jp.QToolbarTitle(a=toolbar, text="Quick and Easy English Dictionary")

        container = jp.QPageContainer(a=layout)

        div = jp.Div(a=container, classes="bg-gray-200 h-screen")
        jp.Div(a=div, text="This is the Home page!", classes="text-4xl p-2")
        jp.Div(a=div, text="""
                    Home ipsum crackalackin black amet, sizzle adipiscing ass. Bizzle we gonna chung velizzle, pimpin' volutpizzle, suscipit brizzle, the bizzle vizzle, arcu. Pellentesque egizzle tortor. Sed erizzle. Fusce izzle pizzle dapibizzle turpizzle tempizzle for sure. Maurizzle pellentesque nibh bow wow wow izzle. Sizzle izzle tortor. 
                    """, classes="text-lg p-2")

        return wp

    @staticmethod
    def move_drawer(widget, msg):
        if widget.drawer.value:
            widget.drawer.value = False
        else:
            widget.drawer.value = True
