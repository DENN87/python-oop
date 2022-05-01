import justpy as jp
import definition


class Dictionary:
    path = "/dictionary"

    @classmethod
    def serve(cls):
        wp = jp.QuasarPage(tailwind=True)
        div = jp.Div(a=wp, classes="bg-gray-200 h-screen")
        jp.Div(a=div, text="Quick and Easy English Dictionary", classes="text-4xl m-2 text-center p-5")
        jp.Div(a=div, text="Get the definition of any English word instantly as you type.",
               classes="text-m mx-2 text-center")

        input_div = jp.Div(a=div, classes="grid grid-cols-1 p-5")

        output_div = jp.Div(a=div, classes="justify-items-stretch m-2 p-2 text-lg border-2 h-40 ")
        input_box = jp.Input(a=input_div, placeholder="Type in a word here...",
                             outputdiv=output_div,
                             classes="m-2 bg-gray-100 border-2 border-gray-200 "
                                     "rounded focus:bg-white "
                                     "focus:outline-none "
                                     "focus:border-gray-500 py-2 px-4 w-48 justify-self-center")

        input_box.on('input', cls._get_definition)

        return wp

    @staticmethod  # simply behaves like a function, independent
    def _get_definition(widget, msg):
        defined = definition.Definition(widget.value).get()
        widget.outputdiv.text = " ".join(defined)

