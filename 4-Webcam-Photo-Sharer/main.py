import time

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder


Builder.load_file('frontend.kv')


class CameraScreen(Screen):

    def start(self):
        self.ids.camera.play = True
        self.ids.btn_start_stop.text = 'Stop Camera'
        self.ids.camera.texture = self.ids.camera._camera.texture

    def stop(self):
        self.ids.camera.play = False
        self.ids.btn_start_stop.text = 'Start Camera'
        self.ids.camera.texture = None

    def capture(self):
        file_path = f"files/{time.strftime('%Y%m%d-%H%M%S')}.png"
        self.ids.camera.export_to_png(file_path)
        self.manager.current = 'image_screen'

class FileSharer:

    def __init__(self, filepath, api_key):
        self.filepath = filepath
        self.api = api_key

    def share(self):
        pass


class ImageScreen(Screen):
    pass


class RootWidget(ScreenManager):
    pass


class MainApp(App):

    def build(self):
        return RootWidget()


MainApp().run()
