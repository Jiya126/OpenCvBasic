import cv2
import numpy as np

drawing = False
mode = True
ix,iy = -1,-1

def draw(event,x,y,flags,params):
    global drawing,mode,ix,iy
    ix,iy = x,y
    
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            if mode == True:
                cv2.rectangle(img, (ix,iy), (x,y), (0,255,0), -1)
            else:
                cv2.circle(img, (x,y), 5, (255,0,0), -1)
                
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        
        
img = np.zeros((512,512,3), np.uint8)
img[:,:] = (0,0,255)
cv2.namedWindow('imageColor')
cv2.setMouseCallback('imageColor', draw)

while(1):
    cv2.imshow('imageColor', img)
    k = cv2.waitKey(1) & 0xFF
    if k == ord('t'):
        mode = not mode
    elif k == 27:
        break
    
cv2.destroyAllWindows()