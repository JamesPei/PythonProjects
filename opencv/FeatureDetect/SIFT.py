#__author__ = 'James'
#-*-coding:utf-8-*-

import cv2
import numpy as np

def sift():
    img = cv2.imread('building.jpg')
    gray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    sift = cv2.SIFT()
    kp = sift.detect(gray,None)

    # computes the descriptors from the keypoints
    kp,des = sift.compute(gray,kp)
    # If you didn’t find keypoints, directly find keypoints and descriptors in a single step with the function
    # Here kp will be a list of keypoints and des is a numpy array of shape Number_of_Keypoints * 128.
    kp, des = sift.detectAndCompute(gray,None)

    # img=cv2.drawKeypoints(gray,kp)
    img=cv2.drawKeypoints(gray,kp, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

    cv2.imshow('sift_keypoints.jpg',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

sift()

