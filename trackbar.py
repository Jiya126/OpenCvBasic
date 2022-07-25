import cv2
import numpy as np

def nill(x):
    pass

cv2.namedWindow('colors')
img = np.zeros((600,800,3), np.uint8)

cv2.createTrackbar('R', 'colors', 0, 255, nill)
cv2.createTrackbar('G', 'colors', 0, 255, nill)
cv2.createTrackbar('B', 'colors', 0, 255, nill)

switch = '1: ON \n 0: OFF'
cv2.createTrackbar(switch, 'colors', 0, 1, nill)


while(1):
    cv2.imshow('colors', img)

    r = cv2.getTrackbarPos('R', 'colors')
    g = cv2.getTrackbarPos('G', 'colors')
    b = cv2.getTrackbarPos('B', 'colors')
    s = cv2.getTrackbarPos(switch, 'colors')

    if s == 0:
        img[:,:] = (0,0,0)
    else:
        img[:,:] = (b,g,r)

    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break
    
cv2.destroyAllWindows()    