#__author__ = 'James'
#-*-coding:utf-8

import cv2

img = cv2.imread('tj.jpg')
imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(imgray,127,255,0)
image, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

#To draw all the contours in an image:
img = cv2.drawContours(img, contours, -1, (0,255,0), 3)

#To draw an individual contour, say 4th contour:
# img = cv2.drawContours(img, contours, 3, (0,255,0), 3)

#But most of the time, below method will be useful:
# cnt = contours[4]
# img = cv2.drawContours(img, [cnt], 0, (0,255,0), 3)

name = 'test'
cv2.namedWindow(name)
cv2.imshow(name, img)
cv2.waitKey(0)
cv2.destroyAllWindows()