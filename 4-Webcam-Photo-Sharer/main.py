import time
import webbrowser

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.core.clipboard import Clipboard

from filestack import Client

Builder.load_file('frontend.kv')


class CameraScreen(Screen):
    def start(self):
        """Starts camera and changes Button text"""

        self.ids.camera.play = True
        self.ids.btn_start_stop.text = 'Stop Camera'
        self.ids.camera.texture = self.ids.camera._camera.texture

    def stop(self):
        """Stops camera and changes Button text"""

        self.ids.camera.play = False
        self.ids.btn_start_stop.text = 'Start Camera'
        self.ids.camera.texture = None

    def capture(self):
        """Creates a filename with current time and captures and saves
        a image under that filename and path"""

        self.file_path = f"files/{time.strftime('%Y%m%d-%H%M%S')}.png"
        self.ids.camera.export_to_png(self.file_path)
        self.manager.current = 'image_screen'
        self.manager.current_screen.ids.img.source = self.file_path


class FileSharer:
    # Get api_key from www.filestack.com

    def __init__(self, filepath, api_key="AffkdoQtLQeqyulzBexkVz"):
        self.filepath = filepath
        self.api_key = api_key

    def share(self):
        """Uploads the filename from file_path to the filestack.com
        and returns back the url of the image"""

        client = Client(self.api_key)
        new_file_link = client.upload(filepath=self.filepath)
        return new_file_link.url


class ImageScreen(Screen):

    link_message = "Create a link first!"

    def create_link(self):
        """
        Accesses the photo file_path, uploads it to the filestack.com
        and inserts the link in the Label widget
        """

        _file_path = App.get_running_app().root.ids.camera_screen.file_path
        file_to_share = FileSharer(_file_path)
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


class RootWidget(ScreenManager):
    pass


class MainApp(App):

    def build(self):
        return RootWidget()


MainApp().run()
