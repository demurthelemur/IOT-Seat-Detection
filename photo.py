import cv2
import time

def takePhoto():
  vid = cv2.VideoCapture(0) 
  time.sleep(5)
  result, image = vid.read()
  if result:
    cv2.imwrite("photo/Result.png", image)
  else:
    print("No image detected. Please! try again")

takePhoto()