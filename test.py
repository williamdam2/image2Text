import cv2
import numpy as np

frame = cv2.imread("anh.jpg")
hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
lower_yellow = np.array([25,100,100])
upper_yellow  = np.array([35,255,255])

mask = cv2.inRange(hsv, lower_yellow, upper_yellow)
res = cv2.bitwise_and(frame,frame, mask= mask)

#cv2.imshow('frame',frame)
#cv2.imshow('res',res)
cv2.imshow('mask',mask)

cv2.waitKey(0)
cv2.destroyAllWindows()

frame = cv2.imread("2.2.jpg")
hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
lower_red = np.array([0,100,100])
upper_red  = np.array([12,255,255])

mask = cv2.inRange(hsv, lower_red, upper_red)
res = cv2.bitwise_and(frame,frame, mask= mask)

#cv2.imshow('frame',frame)
#cv2.imshow('res',res)
cv2.imshow('mask',mask)

cv2.waitKey(0)
cv2.destroyAllWindows()