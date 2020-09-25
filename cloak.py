import cv2 
import numpy as np
import time

cap = cv2.VideoCapture(0)
time.sleep(5)
background = 0
for i in range(30):
    ret, background = cap.read()

background =  cv2.flip(background, 1)

while(cap.isOpened()):
    ret, img= cap.read()
    img = cv2.flip(img, 1)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    value = (35,35)

    blurred = cv2.GaussianBlur(hsv, value, 0)

    lower_red = np.array([0,120,70])
    upper_red = np.array([10,255,255])

    mask1 = cv2.inRange(hsv, lower_red, upper_red)

    lower_red = np.array([170,120,70])
    upper_red = np.array([180,255,255])

    mask2 = cv2.inRange(hsv, lower_red, upper_red)

    mask = mask1+mask2
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, np.ones((8,8),np.uint8))

    img[np.where(mask==255)] = background[np.where(mask==255)]

    cv2.imshow('cloak', img)
    k = cv2.waitKey(10)
    if k == 27:
        break

cv2.destroyAllWindows()
cap.release()
