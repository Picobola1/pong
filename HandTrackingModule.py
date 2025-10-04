import cv2 as cv
import numpy as np
import mediapipe as mp
import random
import time

class handDetector():
    def __init__(self, mode=False,maxHands = 2, detectionCon = 0.5, trackCon = 0.5):
        # make object and each object will have its own variable
        self.mode = mode
        self.maxHands = maxHands
        self.detectionCon = detectionCon
        self.trackCon = trackCon
        self.mpHands = mp.solutions.hands 
        self.hands = self.mpHands.Hands(self.mode,self.maxHands,self.detectionCon, self.trackCon)# defult parmeters
        self.mpDraw = mp.solutions.drawing_utils

    def findHands(self,img,draw = True):

        imgRgb = cv.cvtColor(flipped_img, cv.COLOR_BGR2RGB)
        results = self.hands.process(imgRgb)

        if results.multi_hand_landmarks:
        #get info from each hand/ loops thru each hand
            for handLms in results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(flipped_img, handLms, self.mpHands.HAND_CONNECTIONS)
                # for id, lm in enumerate(handLms.landmark):
                #     #print(id,lm)
                #     h, w, c = img.shape
                #     cx, cy = int(lm.x*w), int(lm.y*h)
                #     cv.circle(flipped_img, (cx,cy), 5, (255,255,255), cv.FILLED)
                # #print(id, cx, cy)
                # #if id == 8:


cap = cv.VideoCapture(0)
success, img = cap.read()



   
    success, img = cap.read()
    flipped_img = cv.flip(img, 1) # Flip horizontally
    window_h, window_w, c = flipped_img.shape
    
    
    
    
   

        
    #print(CoinRangeX,CoinRangeY)

    
                     

    cv.imshow(" Image", flipped_img)
    key = cv.waitKey(1) & 0xFF
    if key == ord('q'):   # press q to quit
        break

def main()
    pTime = 0
    cTime = 0
    while True:
        success, img = cap.read()
        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime
        cv.putText(flipped_img,str(int(fps)), (10,70), cv.FONT_HERSHEY_PLAIN, 3, (255,0,255), 3 )

if __name__ == "__main__":
    main()