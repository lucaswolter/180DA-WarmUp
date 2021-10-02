import cv2 as cv
import numpy as np
cap = cv.VideoCapture(0)

while(1):
    # Take each frame
    _, frame = cap.read()

    # Convert BGR to HSV
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    # define range of blue color in HSV
    lower_blue = np.array([115,50,50])
    upper_blue = np.array([125,255,255])

    # define range of blue color in BGR
    #lower_blue = np.array([0, 0, 255])
    #upper_blue = np.array([0, 0, 255])

    # Threshold the HSV image to get only blue colors
    mask = cv.inRange(hsv, lower_blue, upper_blue)
    
    x,y,w,h = cv.boundingRect(mask)
    rect = cv.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)

    cv.imshow('', rect)

    k = cv.waitKey(5) & 0xFF
    if k == 27:
        break
cv.destroyAllWindows()