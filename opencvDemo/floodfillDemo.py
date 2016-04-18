#__author__ = 'James'
#-*-coding:utf-8-*-

import cv2
im = cv2.imread('python.jpg')
h, w = im.shape[:2]

#泛洪填充
diff = (6,6,6)
mask = zeros((h+2, w+2), uint8)

