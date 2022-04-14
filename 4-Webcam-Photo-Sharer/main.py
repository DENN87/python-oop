import time

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

from filestack import Client

Builder.load_file('frontend.kv')


class CameraScreen(Screen):

    def __init__(self, **kw):
        super().__init__(**kw)
        self.file_path = None

    def start(self):
        self.ids.camera.play = True
        self.ids.btn_start_stop.text = 'Stop Camera'
        self.ids.camera.texture = self.ids.camera._camera.texture

    def stop(self):
        self.ids.camera.play = False
        self.ids.btn_start_stop.text = 'Start Camera'
        self.ids.camera.texture = None

    def capture(self):
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
        client = Client(self.api_key)
        new_file_link = client.upload(filepath=self.filepath)
        return new_file_link.url


class ImageScreen(Screen):
    """
    Accesses the photo file_path, uploads it to the filestack.com
    and inserts the link in the Label widget
    """
    def create_link(self):
        _file_path = App.get_running_app().root.ids.camera_screen.file_path
        file_to_share = FileSharer(_file_path)
        url = file_to_share.share()
        self.ids.img_link.text = url


class RootWidget(ScreenManager):
    pass


class MainApp(App):

    def build(self):
        return RootWidget()


MainApp().run()
