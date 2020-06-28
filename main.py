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
    
    
    
    
# loop for accessing frames of the video
while True:
	frame = vs.read()
	frame = frame if args.get("video", None) is None else frame[1]
	if frame is None:
		break


