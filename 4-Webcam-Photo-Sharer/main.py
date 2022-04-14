from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder


Builder.load_file('frontend.kv')


class Webcam:

    def start(self):
        pass

    def stop(self):
        pass

    def capture(self):
        pass


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
