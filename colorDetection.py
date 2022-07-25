import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(1):
    ret, frame = cap.read()

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    up_blue = np.array([130,255,255])
    lo_blue = np.array([110,50,50])

    mask = cv2.inRange(hsv, lo_blue, up_blue)

    detect = cv2.bitwise_and(frame, frame, mask= mask)

    cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)
    cv2.imshow('blue', detect)

    k = cv2.waitKey(1) & 0xFF
    if k == ord('q'):
        break

cv2.destroyAllWindows()