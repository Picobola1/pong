import cv2 as cv
import numpy as np
import mediapipe as mp
import random
import time
import HandTrackingModule as htm 


pTime = 0
cTime = 0
cap = cv.VideoCapture(0)
detector = htm.handDetector()
while True:
    success, img = cap.read()
    img = cv.flip(img, 1)
    img = detector.findHands(img)
    lmList = detector.findPosition(img)
    if len(lmList) != 0:
        print(lmList[8])
   
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv.putText(img,str(int(fps)), (10,70), cv.FONT_HERSHEY_PLAIN, 3, (255,0,255), 3 )
    cv.imshow(" Image", img)
    key = cv.waitKey(1) & 0xFF
    if key == ord('q'):   # press q to quit
        break
cap.release()
cv.destroyAllWindows()