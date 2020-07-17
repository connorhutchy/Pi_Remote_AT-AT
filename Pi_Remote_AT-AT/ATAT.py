from motorcontrol import MotorControl
from mycamera import MyCamera
import threading
import sys

#main file to run for ATAT control
        
def Camera():
    camera = MyCamera()
    camera.start_stream()

def Control():
    control = MotorControl()
    control.start()


threads = []
startCamera = threading.Thread(target=Camera)
startControl = threading.Thread(target=Control)

threads.append(startCamera)
threads.append(startControl)
startCamera.daemon = True

for thread in threads:
    thread.start()

while True:
    if not startControl.is_alive():
        sys.exit()
        break
        
