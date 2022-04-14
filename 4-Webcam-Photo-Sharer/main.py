from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from kivy.lang import Builder

from resources.camerascreen import CameraScreen
from resources.imagescreen import ImageScreen


Builder.load_file('resources/frontend.kv')


class RootWidget(ScreenManager):
    pass


class MainApp(App):

    def build(self):
        return RootWidget()


MainApp().run()
