#__author__ = 'James'
#-*-coding:utf-8-*-

import cv2
from matplotlib import pyplot as plt

def ORB_corner_detect(nfeatures=500, edgeThreshold=24, WTA_K=2):
    img = cv2.imread('benzene4.jpg',0)

    # Initiate STAR detector
    # cv2.ORB_create([nfeatures[, scaleFactor[, nlevels[, edgeThreshold[, firstLevel[, WTA_K[, scoreType[, patchSize]]]]]]]]) → <ORB object>
    # nfeatures – The maximum number of features to retain 要保留特征的最大数目（默认500)
    # scoreType —　设置使用Harris打分还是使用FAST打分对特征进行排序(默认Harris)
    # WTA_K —　产生每个BRIEF描述符要使用的像素点的数目（默认为２,即一次选择两个点）
    orb = cv2.ORB_create(nfeatures=nfeatures, edgeThreshold=edgeThreshold, WTA_K=WTA_K)

    # find the keypoints with ORB
    kp = orb.detect(img,None)

    # compute the descriptors with ORB
    kp, des = orb.compute(img, kp)
    print str(edgeThreshold)+':',len(kp)
    # # draw only keypoints location,not size and orientation
    # img2 = cv2.drawKeypoints(img,kp, None, color=(0,255,0), flags=0)
    #
    # plt.imshow(img2),plt.show()

if __name__=='__main__':
    for i in range(1,100):
        ORB_corner_detect(edgeThreshold=i)
    # ORB_corner_detect(edgeThreshold=41)