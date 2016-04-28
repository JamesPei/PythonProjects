#__author__ = 'James'
#-*-coding:utf-8-*-

import numpy as np
import cv2
from matplotlib import pyplot as plt

def ORB():
    img = cv2.imread('test.jpg',0)

    # Initiate STAR detector
    # cv2.ORB([nfeatures[, scaleFactor[, nlevels[, edgeThreshold[, firstLevel[, WTA_K[, scoreType[, patchSize]]]]]]]]) → <ORB object>
    # nfeatures – The maximum number of features to retain 要保留特征的最大数目（默认500)
    # scoreType —　设置使用Harris打分还是使用FAST打分对特征进行排序(默认Harris)
    # WTA_K —　产生每个BRIEF描述符要使用的像素点的数目（默认为２,即一次选择两个点）
    orb = cv2.ORB(nfeatures=500)

    # find the keypoints with ORB
    kp = orb.detect(img,None)

    # compute the descriptors with ORB
    kp, des = orb.compute(img, kp)

    # draw only keypoints location,not size and orientation
    img2 = cv2.drawKeypoints(img,kp,color=(0,255,0), flags=0)
    print len(kp)
    plt.imshow(img2),plt.show()

ORB()