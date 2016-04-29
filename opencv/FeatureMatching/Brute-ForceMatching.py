#__author__ = 'James'
#-*-coding:utf-8-*-

import numpy as np
import cv2
from matplotlib import pyplot as plt

#用ORB描述符进行暴力匹配
def ORB_BF_Matching():
    img1 = cv2.imread('box.png',0)          # queryImage
    img2 = cv2.imread('box_in_scene.png',0) # trainImage

    # Initiate ORB detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with SIFT
    # cv2.ORB.detectAndCompute(image, mask[, descriptors[, useProvidedKeypoints]]) → keypoints, descriptors
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    # 第一个参数normType:指定要使用的距离测试类型，默认为cv2.Norm_L2.对于ORB,BRIEF,BRISK算法,要使用cv2.NORM_HAMMING
    # crossCheck默认为False,若设置为True则需双向匹配，否则只需单项匹配即可
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1,des2)

    # Sort them in the order of their distance.
    # The result of matches = bf.match(des1,des2) line is a list of DMatch objects. This DMatch object has following attributes:
    #   DMatch.distance - Distance between descriptors. The lower, the better it is
    #   DMatch.trainIdx - Index of the descriptor in train descriptors
    #   DMatch.queryIdx - Index of the descriptor in query descriptors
    #   DMatch.imgIdx - Index of the train image
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 10 matches.
    # cv2.drawMatches(img1, keypoints1, img2, keypoints2, matches1to2, outImg[, matchColor[, singlePointColor[, matchesMask[, flags]]]]]) → outImg
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None,flags=2)

    plt.imshow(img3),plt.show()

#SIFT描述符暴力匹配
def SIFT_BF_Matching():
    img1 = cv2.imread('box.png',0)          # queryImage
    img2 = cv2.imread('box_in_scene.png',0) # trainImage

    # Initiate SIFT detector
    sift = cv2.SIFT()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = sift.detectAndCompute(img1,None)
    kp2, des2 = sift.detectAndCompute(img2,None)

    # BFMatcher with default params
    bf = cv2.BFMatcher()
    matches = bf.knnMatch(des1,des2, k=2)

    # Apply ratio test
    # 比值测试，首先获得与A距离最近的点B(最近)和点C(次近),只有当B/C小于阈值（0.75）时才被认为是匹配，因为假设匹配是一一对应的，真正的匹配理想距离为0
    good = []
    for m,n in matches:
       if m.distance < 0.75*n.distance:
           good.append([m])

    # cv2.drawMatchesKnn expects list of lists as matches.
    img3 = cv2.drawMatchesKnn(img1, kp1, img2,kp2,good,flags=2)

    plt.imshow(img3),plt.show()

# ORB_BF_Matching()
SIFT_BF_Matching()