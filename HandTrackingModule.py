import cv2 as cv
import numpy as np
import mediapipe as mp
import random


cap = cv.VideoCapture(0)
success, img = cap.read()
mpHands = mp.solutions.hands 
hands = mpHands.Hands()# defult parmeters




# run a web cam and anything while web cam is still going
while True:
   
    success, img = cap.read()
    flipped_img = cv.flip(img, 1) # Flip horizontally
    window_h, window_w, c = flipped_img.shape
    
    imgRgb = cv.cvtColor(flipped_img, cv.COLOR_BGR2RGB)
    results = hands.process(imgRgb)
    mpDraw = mp.solutions.drawing_utils
    
   

        
    #print(CoinRangeX,CoinRangeY)

    if results.multi_hand_landmarks:
        
        #get info from each hand/ loops thru each hand
        for handLms in results.multi_hand_landmarks:
            #not drawing on rgb img cuz we are not displaying the img
            # draw land marks of single hand
            mpDraw.draw_landmarks(flipped_img, handLms, mpHands.HAND_CONNECTIONS)
            for id, lm in enumerate(handLms.landmark):
                #print(id,lm)
                h, w, c = img.shape
                cx, cy = int(lm.x*w), int(lm.y*h)
                
                
                #print(id, cx, cy)
                if id == 8:
                     cv.circle(flipped_img, (cx,cy), 5, (255,255,255), cv.FILLED)
          

    cv.imshow(" Image", flipped_img)
    key = cv.waitKey(1) & 0xFF
    if key == ord('q'):   # press q to quit
        break