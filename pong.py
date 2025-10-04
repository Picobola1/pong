import cv2 as cv
import numpy as np
import mediapipe as mp
import random
import time
import HandTrackingModule as htm 
import os


pTime = 0
cTime = 0
cap = cv.VideoCapture(0)
detector = htm.handDetector()

tipIds = [4,8,12,16,20]

while True:
    success, img = cap.read()
    img = cv.flip(img, 1)
    img = detector.findHands(img)
    lmList = detector.findPosition(img)
    #if hand is there
    if len(lmList) != 0:

        for id in range(0,5):

            if lmList[tipIds[id]][2] < lmList[tipIds[id] - 2][2]:
                print("all fingers are open")
            else:
                print("all fingers closes IN FIST")
           
        
   
    
    cv.imshow(" Image", img)
    key = cv.waitKey(1) & 0xFF
    if key == ord('q'):   # press q to quit
        break
cap.release()
cv.destroyAllWindows()