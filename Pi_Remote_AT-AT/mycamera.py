from picamera import PiCamera

class MyCamera:
    def __init__(self):
        self.camera = PiCamera()
        self.camera.resolution = (300,300)
        self.camera.framerate = 60
        self.camera.rotation = 180
        self.image = 0


    def start_stream(self):
        self.camera.start_preview()


    def stop_stream(self):
        self.camera.stop_preview()

    def take_picture(self):
        self.camera.capture('/home/pi/Desktop/image%s.jpg' % self.image)
        image += 1
    
    def add_text(self, text):
        self.camera.annotate_text = text