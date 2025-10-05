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
paddleBack = 250
ball_speedx, ball_speedy = 5, 5
success, img = cap.read()
h, w, c = img.shape
ball_x, ball_y = w // 2, h // 2
left_cx, left_cy = 0, 0
right_cx, right_cy = 0, 0



while True:
    
    success, img = cap.read()
    img = cv.flip(img, 1)
    img = detector.findHands(img, draw=False)

    h, w, c = img.shape
    middle_x = w // 2
    middle_y = h // 2
    
    
    
    cv.line(img, (middle_x, 0), (middle_x, h), (0, 1, 0), 2)
    ball_x += ball_speedx
    ball_y += ball_speedy

    cv.circle(img, (int(ball_x), int(ball_y)), 15, (255,255,255), -1)
    if ball_x <= 0 or ball_x >= w - 15:
        ball_speedx *= -1
    if ball_y <= 0 or ball_y >= h - 15:
        ball_speedy *= -1
        

    if detector.results.multi_hand_landmarks:
        for i in range(len(detector.results.multi_hand_landmarks)):
            lmList = detector.findPosition(img, handNum=i, Draw=False)
        #if hand is there
            if len(lmList) != 0:
                HandSide = detector.results.multi_handedness[i].classification[0].label
                for id in range(0,5):
                    if lmList[tipIds[id]][2] < lmList[tipIds[id] - 2][2]:
                        paddleSpawn = False
                    else:
                        for id, lm in enumerate(lmList):
                            h, w, c = img.shape
                            cx, cy = lmList[14][1], lmList[14][2]
                            
                            if id == 6:
                                paddleSpawn = True
                                if paddleSpawn == True and HandSide == "Left":
                                    cx = middle_x - paddleBack
                                    cx = np.clip(cx, 0, w - 33)
                                    cy = np.clip(cy, 0, h - 118)
                                    img[cy:cy+114, cx:cx+33] = paddle1
                                    left_cx, left_cy = cx, cy
                                    
                                    
                                if paddleSpawn == True and HandSide == "Right":
                                    cx = middle_x + paddleBack
                                    cx = np.clip(cx, 0, w - 33)
                                    cy = np.clip(cy, 0, h - 118)
                                    img[cy:cy+118, cx:cx+33] = paddle2
                                    right_cx, right_cy = cx, cy
    if (ball_x - 15 <= left_cx + 33 and left_cy <= ball_y <= left_cy + 114):
        ball_speedx *= -1
    if (ball_x + 15 >= right_cx and right_cy <= ball_y <= right_cy + 118):
        ball_speedx *= -1
    

              







                        
                                    
                                    

                        
           
        
   
    
    cv.imshow(" Image", img)
    key = cv.waitKey(1) & 0xFF
    if key == ord('q'):   # press q to quit
        break
cap.release()
cv.destroyAllWindows()