import justpy as jp

class DefaultLayout(jp.QLayout):

    def __init__(self, view="hHh lpR fFf", **kwargs):
        super().__init__(view=view, **kwargs)

        header = jp.QHeader(a=self)
        toolbar = jp.QToolbar(a=header)

        drawer = jp.QDrawer(a=self, show_if_above=True, v_mode="left", bordered=True)

        scroller = jp.QScrollArea(a=drawer, classes="fit p-5")
        qlist = jp.QList(a=scroller)
        a_classes = "text-xl text-blue-400 hover:text-blue-700"
        jp.A(a=qlist, text="Home", href="/", classes=a_classes)
        jp.Br(a=qlist)
        jp.A(a=qlist, text="Dictionary", href="/dictionary", classes=a_classes)
        jp.Br(a=qlist)
        jp.A(a=qlist, text="About", href="/about", classes=a_classes)
        jp.Br(a=qlist)

        jp.QBtn(a=toolbar, dense=True, flat=True, round=True, icon="menu", click=self._move_drawer, drawer=drawer)

        jp.QToolbarTitle(a=toolbar, text="Quick and Easy English Dictionary")

    @staticmethod
    def _move_drawer(widget, msg):
        if widget.drawer.value:
            widget.drawer.value = False
        else:
            widget.drawer.value = True
