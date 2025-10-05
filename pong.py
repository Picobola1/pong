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
paddle1 = cv.imread("paddle1.png", cv.IMREAD_COLOR)
paddle2 = cv.imread("paddle2.png", cv.IMREAD_COLOR)
paddleSpawn = False
tipIds = [4,8,12,16,20]

while True:
    success, img = cap.read()
    img = cv.flip(img, 1)
    img = detector.findHands(img)
    if detector.results.multi_hand_landmarks:
        for i in range(len(detector.results.multi_hand_landmarks)):
            lmList = detector.findPosition(img, handNum=i, Draw=False)
        #if hand is there
            if len(lmList) != 0:
                
                for id in range(0,5):
                    if lmList[tipIds[id]][2] < lmList[tipIds[id] - 2][2]:
                        paddleSpawn = False
                    else:
                        for id, lm in enumerate(lmList):
                            h, w, c = img.shape
                            cx, cy = lmList[12][1], lmList[12][2]
                            
                            if id == 12:
                                paddleSpawn = True
                                if paddleSpawn == True:
                                    img[cy:cy+114, cx:cx+33] = paddle1

                        
           
        
   
    
    cv.imshow(" Image", img)
    key = cv.waitKey(1) & 0xFF
    if key == ord('q'):   # press q to quit
        break
cap.release()
cv.destroyAllWindows()