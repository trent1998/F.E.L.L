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



import numpy as np 
import cv2 
  
#parentheses in next line will contain video name when determined
cap = cv2.VideoCapture() 
  
fgbg = cv2.createBackgroundSubtractorMOG2() 
  
while(1): 
    ret, frame = cap.read() 
    
    fgmask = fgbg.apply(frame) 
  
    cv2.imshow('frame', fgmask)   
    k = cv2.waitKey(30) & 0xff
    if k == 27: 
        break
  
cap.release() 
cv2.destroyAllWindows()


