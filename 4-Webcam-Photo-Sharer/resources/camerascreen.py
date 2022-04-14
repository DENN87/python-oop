import time
from kivy.uix.screenmanager import Screen


class CameraScreen(Screen):
    def start(self):
        """Starts camera and changes Button text"""

        self.ids.camera.opacity = 1
        self.ids.camera.play = True
        self.ids.btn_start_stop.text = 'Stop Camera'
        self.ids.camera.texture = self.ids.camera._camera.texture

    def stop(self):
        """Stops camera and changes Button text"""

        self.ids.camera.opacity = 0
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

