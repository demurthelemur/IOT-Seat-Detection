import cv2
import time

def takePhoto():
  vid = cv2.VideoCapture(0) 
  time.sleep(2)
  result, image = vid.read()
  if result:
    print("New photo taken")
    cv2.imwrite("photo/Result.png", image)
    return True
  else:
    print("No image detected. Please! try again")
    return False