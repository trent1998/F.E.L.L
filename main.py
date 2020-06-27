import numpy as np 
import cv2 
  
  
#parentheses in next line will contain video name when determined
cap = cv2.VideoCapture() 
  
fgbg = cv2.createBackgroundSubtractorKNN() 
  
while(True): 
    ret, frame = cap.read() 
    
    fgmask = fgbg.apply(frame) 
  
    cv2.imshow('frame', fgmask)   
    k = cv2.waitKey(30) & 0xff
    if k == 27: 
        break
  
cap.release() 
cv2.destroyAllWindows()
