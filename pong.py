import cv2 as cv
import random
import mediapipe as mp

cap = cv.VideoCapture(0)

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils
while True:
    success,img = cap.read()
    flipped_img = cv.flip(img, 1) # Flip horizontally
    imgRgb = cv.cvtColor(flipped_img, cv.COLOR_BGR2RGB )
    results = hands.process(imgRgb)
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            mpDraw.draw_landmarks(flipped_img, handLms)
            

    cv.imshow("Camera", flipped_img)
    key = cv.waitKey(1) & 0xFF
    if key == ord('q'):   # press q to quit
        break