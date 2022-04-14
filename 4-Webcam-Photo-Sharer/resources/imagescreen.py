import webbrowser

from kivy.app import App
from kivy.core.clipboard import Clipboard
from kivy.uix.screenmanager import Screen

from .fileshare import FileShare

class ImageScreen(Screen):
    link_message = "Create a link first!"

    def create_link(self):
        """
        Accesses the photo file_path, uploads it to the filestack.com
        and inserts the link in the Label widget
        """

        _file_path = App.get_running_app().root.ids.camera_screen.file_path

        file_to_share = FileShare(_file_path)

        self.url = file_to_share.share()
        self.ids.img_link.text = self.url

    def copy_link(self):
        """Copy link to the clipboard for pasting"""

        try:
            Clipboard.copy(self.url)
        except:
            self.ids.img_link.text = self.link_message

    def open_link(self):
        """Open link in the browser"""

        try:
            webbrowser.open(self.url)
        except:
            self.ids.img_link.text = self.link_message


