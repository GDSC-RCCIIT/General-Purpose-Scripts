import cv2
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.gridlayout import GridLayout
from kivy.clock import Clock
from kivy.graphics.texture import Texture
from datetime import datetime


class ControlPanel(GridLayout):

    # Function to save the images
    def save_image(self, event):
        frame = self.main_layout.frame
        now = datetime.now()
        date_time = now.strftime("%m-%d-%Y_%H-%M-%S")
        cv2.imwrite(date_time + ".png", frame)

    # Start recording the videos
    def start_video(self, event):
        self.start.disabled = True
        self.stop.disabled = False

        frame_w = int(self.main_layout.capture.get(3))
        frame_h = int(self.main_layout.capture.get(4))
        size = (frame_w, frame_h)
        now = datetime.now()
        date_time = now.strftime("%m-%d-%Y_%H-%M-%S")

        self.videowriter = cv2.VideoWriter(
            date_time + ".avi", cv2.VideoWriter_fourcc(*"MJPG"), 10, size
        )
        self.videoClock = Clock.schedule_interval(self.write_frame, 1 / 10)

    # Stop recording videos
    def stop_video(self, event):
        self.start.disabled = False
        self.stop.disabled = True
        self.videowriter.release()
        self.videoClock.release()

    # Write the video frame by frame
    def write_frame(self, event):
        self.videowriter.write(self.main_layout.frame)

    def __init__(self, main_layout, **kwargs):
        super(ControlPanel, self).__init__(**kwargs)
        self.videowriter = None
        self.rows = 1
        self.main_layout = main_layout
        self.click = Button(text="Click")
        self.start = Button(text="Video On")
        self.stop = Button(text="Video Off")
        self.video = False

        self.add_widget(self.click)
        self.add_widget(self.start)
        self.add_widget(self.stop)

        self.click.bind(on_press=self.save_image)
        self.start.bind(on_press=self.start_video)
        self.stop.bind(on_press=self.stop_video)


# Main layout of the app
class MainLayout(GridLayout):
    def update(self, event):
        retval, frame = self.capture.read()
        if retval:
            self.frame = frame
            flipped = frame[::-1]
            buf = flipped.tostring()
            texture = Texture.create(
                size=(frame.shape[1], frame.shape[0]), colorfmt="bgr"
            )
            texture.blit_buffer(buf, colorfmt="bgr", bufferfmt="ubyte")

            self.image.texture = texture

    def __init__(self, **kwargs):
        super(MainLayout, self).__init__(**kwargs)
        self.frame = None
        self.capture = cv2.VideoCapture(0)
        self.rows = 2
        self.image = Image()
        self.control = ControlPanel(self)
        self.add_widget(self.image)
        self.add_widget(self.control)
        Clock.schedule_interval(self.update, 1 / 30)


class TestApp(App):
    def build(self):
        return MainLayout()


app = TestApp()
app.run()
