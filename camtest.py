from picamera import PiCamera
import time

myCamera = PiCamera()

for i in range (10):
    myCamera.brightness = 50
    myCamera.capture('/home/pi/Desktop/image%s.jpg' % i)
    time.sleep(1)