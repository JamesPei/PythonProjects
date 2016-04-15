#__author__ = 'James'
#-*-coding:utf-8-*-

import cv2
import numpy as np

img1 = cv2.imread('test.jpg')
img2 = cv2.imread('python.jpg')
# px = img[100,100]
# print px

# blue = img[100,100,0]
# print blue

# img[100,100] = [255,255,255]
# print img[100,100]
# print img.shape
# print img.size
# print img.dtype

# a = img[100:120,100:120]
# img[150:170,150:170] = a
# cv2.imwrite('test.jpg',img)

# dst = cv2.addWeighted(img1, 0.5, img2, 0.5, 0)
# cv2.imshow('dst',dst)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

#图片平滑过度
# cv2.namedWindow('image',cv2.WINDOW_NORMAL)
# for i in range(1000):
#     s = i/1000.0
#     dst = cv2.addWeighted(img1, s, img2, 1.0-s, 0)
#     cv2.imshow('image',dst)
#     cv2.waitKey(1)
# cv2.destroyAllWindows()

# 按位运算
# Load two images
def bitwise():
    img1 = cv2.imread('messi.jpg')
    img2 = cv2.imread('python.jpg')
    e1 = cv2.getTickCount()

    # I want to put logo on top-left corner, So I create a ROI
    rows,cols,channels = img2.shape
    roi = img1[0:rows, 0:cols]

    # Now create a mask of logo and create its inverse mask also
    img2gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
    # cv2.threshold(src, thresh, maxval, type[, dst]) → retval, dst
    ret, mask = cv2.threshold(img2gray, 230, 255, cv2.THRESH_BINARY_INV)     #Applies a fixed-level threshold to each array element.
    mask_inv = cv2.bitwise_not(mask)

    # Now black-out the area of logo in ROI
    img1_bg = cv2.bitwise_and(roi,roi,mask = mask_inv)

    # Take only region of logo from logo image.
    img2_fg = cv2.bitwise_and(img2,img2,mask = mask)

    # Put logo in ROI and modify the main image
    dst = cv2.add(img1_bg,img2_fg)
    img1[0:rows, 0:cols] = dst

    e2 =cv2.getTickCount()
    t = (e2- e1)/cv2.getTickFrequency()
    print t
    cv2.imshow('res',img1)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

bitwise()
