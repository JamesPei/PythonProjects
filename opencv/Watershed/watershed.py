# __author__ = 'James'
# -*-coding:utf-8-*-

import numpy as np
import cv2
from matplotlib import pyplot as plt

def watershed_demo():
    img = cv2.imread('water_coins.jpg')
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(gray,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

    # noise removal
    kernel = np.ones((3,3),np.uint8)
    opening = cv2.morphologyEx(thresh,cv2.MORPH_OPEN,kernel, iterations = 2)

    # sure background area
    sure_bg = cv2.dilate(opening,kernel,iterations=3)

    # Finding sure foreground area
    # cv2.distanceTransform(src, distanceType, maskSize[, dst]) → dst
    # distanceType – Type of distance. It can be CV_DIST_L1, CV_DIST_L2 , or CV_DIST_C
    dist_transform = cv2.distanceTransform(opening,1,5) #Calculates the distance to the closest zero pixel for each pixel of the source image.
    ret, sure_fg = cv2.threshold(dist_transform,0.7*dist_transform.max(),255,0)

    # Finding unknown region
    sure_fg = np.uint8(sure_fg)
    unknown = cv2.subtract(sure_bg,sure_fg)

    # Marker labelling
    ret, markers = cv2.connectedComponents(sure_fg)

    # Add one to all labels so that sure background is not 0, but 1
    markers = markers+1

    # Now, mark the region of unknown with zero
    markers[unknown==255] = 0

    markers = cv2.watershed(img,markers)
    img[markers == -1] = [255,0,0]

    cv2.imshow('watershed', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

watershed_demo()