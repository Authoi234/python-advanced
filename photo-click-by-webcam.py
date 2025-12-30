from cv2 import *
from cv2 import VideoCapture
from cv2 import imshow
from cv2 import imwrite
from cv2 import waitKey
from cv2 import destroyWindow
import time


cam = VideoCapture(0)
time.sleep(2)

ret, frame = cam.read()

if ret:
    imshow("Captured", frame)         
    imwrite("captured_image.png", frame)  
    waitKey(0)                      
    destroyWindow("Captured")       
else:
    print("Failed to capture image.")

cam.release() 