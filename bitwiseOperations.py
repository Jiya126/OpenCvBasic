import cv2
import numpy as np

imgB = cv2.imread('C:/Users/jiya/Pictures/references/pexels-dionizzio-geronimo-12642979.jpg')
imgT = cv2.imread('C:/Users/jiya/Pictures/rtNrs.png')

r,c,ch = imgT.shape
roi = imgB[0:r, 0:c]

imgTgr = cv2.cvtColor(imgT, cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(imgTgr, 19, 255, cv2.THRESH_BINARY)
maskInv = cv2.bitwise_not(mask)

img1 = cv2.bitwise_and(roi, roi, mask= maskInv)
img2 = cv2.bitwise_and(imgT, imgT, mask= mask)

ar = cv2.add(img1, img2)
imgB[0:r, 0:c] = ar

cv2.imshow('orig', imgB)
# cv2.imshow('original', imgT)
cv2.imshow('int', img1)
# cv2.imshow('live', mask)
cv2.imshow('live2', maskInv)
cv2.waitKey(0)
cv2.destroyAllWindows()