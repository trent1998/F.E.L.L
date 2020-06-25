import numpy as np 
import cv2 
  
  
capture = cv2.VideoCapture(0) 
while(capture.isOpened()): 
      
    while True: 
          
        ret, img = capture.read() 
        cv2.imshow('img', img) 
        if cv2.waitKey(30) & 0xff == ord('x'): 
            break
              
    capture.release() 
    cv2.destroyAllWindows() 
else: 
    print("Camera is not connected") 


