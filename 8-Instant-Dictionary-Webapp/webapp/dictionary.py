import justpy as jp
import sys
from pathlib import Path
sys.path.append(str(Path('.').absolute().parent))

import definition


class Dictionary:
    path = "/dictionary"

    @classmethod
    def serve(cls):
        wp = jp.QuasarPage(tailwind=True)
        div = jp.Div(a=wp, classes="bg-gray-200 h-screen")
        jp.Div(a=div, text="Quick and Easy English Dictionary", classes="text-4xl m-2")
        jp.Div(a=div, text="Get the definition of any English word instantly as you type.", classes="text-m mx-2")

        input_div = jp.Div(a=div, classes="grid grid-cols-2")
        input_box = jp.Input(a=input_div, placeholder="Type in a word here...",
                             classes="m-2 bg-gray-100 border-2 border-gray-200 "
                                     "rounded focus:bg-white "
                                     "focus:outline-none "
                                     "focus:border-gray-500 py-2 px-4")

        output_div = jp.Div(a=div, classes="m-2 p-2 text-lg border-2 h-40")
        jp.Button(a=input_div, text="Get Definition", classes="border-2",
                  click=cls._get_definition, outputdiv=output_div, inputbox=input_box)

        return wp

    @staticmethod  # simply behaves like a function, independent
    def _get_definition(widget, msg):
        defined = definition.Definition(widget.inputbox.value).get()
        widget.outputdiv.text = " ".join(defined)

