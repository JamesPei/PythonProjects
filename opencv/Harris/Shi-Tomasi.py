#__author__ = 'James'
#-*-coding:utf-8-*-

import numpy as np
import cv2
from matplotlib import pyplot as plt

def Shi_Tomasi_detect():
    img = cv2.imread('chemistry1.jpg')
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    #cv2.goodFeaturesToTrack(image, maxCorners, qualityLevel, minDistance[, corners[, mask[, blockSize[, useHarrisDetector[, k]]]]]) → corners
    #maxCorners – Maximum number of corners to return
    #qualityLevel – Parameter characterizing the minimal accepted quality of image corners.The parameter value is multiplied by the
    # best corner quality measure, which is the minimal eigenvalue or the Harris function response .
    # The corners with the quality measure less than the product are rejected. For example, if the best corner has the quality measure = 1500,
    # and the qualityLevel=0.01 , then all the corners with the quality measure less than 15 are rejected
    # minDistance – Minimum possible Euclidean distance between the returned corners.
    corners = cv2.goodFeaturesToTrack(gray,10,0.01,10)
    corners = np.int0(corners)

    for i in corners:
        x,y = i.ravel()
        cv2.circle(img,(x,y),3,255,-1)

    plt.imshow(img),plt.show()

Shi_Tomasi_detect()