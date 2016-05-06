#__author__ = 'James'
#-*-coding:utf-8-*-

import cv2
import numpy as np
from matplotlib import pyplot as plt

def first_demo():
    img1 = cv2.imread('benzene4.jpg',0)          # queryImage
    img2 = cv2.imread('chemistry1.jpg',0)        # trainImage

    # Initiate ORB detector
    orb = cv2.ORB_create(nfeatures=500, edgeThreshold=24)

    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)
    print 'kp1_length:',len(kp1)
    # print 'kp1:',kp1
    print 'kp2_length:',len(kp2)
    # print 'kp2:',kp2

    # FLANN parameters
    FLANN_INDEX_LSH = 0
    index_params= dict(algorithm = FLANN_INDEX_LSH, table_number = 6, key_size = 12,multi_probe_level = 1)
    search_params = dict(checks=50)   # or pass empty dictionary

    flann = cv2.FlannBasedMatcher(index_params, search_params)

    matches = flann.knnMatch(np.asarray(des1,np.float32),np.asarray(des2,np.float32), k=2)

    # Need to draw only good matches, so create a mask
    matchesMask = [[0,0] for i in xrange(len(matches))]
    print '匹配数:',len(matches)
    # ratio test as per Lowe's paperbenzene-ring2.jpg
    for i,(m,n) in enumerate(matches):
        if m.distance < 0.7*n.distance:
            matchesMask[i]=[1,0]
    draw_params = dict(matchColor = (0,255,0),
                   singlePointColor = (255,0,0),
                   matchesMask = matchesMask,
                   flags = 0)
    img3 = cv2.drawMatchesKnn(img1,kp1,img2,kp2,matches,None,**draw_params)

    plt.imshow(img3,),plt.show()


def Homography():
    MIN_MATCH_COUNT = 10

    img1 = cv2.imread('benzene4.jpg',0)          # queryImage
    img2 = cv2.imread('chemistry1.jpg',0)          # trainImage

    # Initiate ORB detector
    orb = cv2.ORB_create(nfeatures=500, edgeThreshold=5)

    # find the keypoints and descriptors with ORB
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)
    print 'kp1_length:',len(kp1)
    print 'kp2_length:',len(kp2)

    # FLANN parameters
    FLANN_INDEX_LSH = 0
    index_params= dict(algorithm = FLANN_INDEX_LSH, table_number = 6, key_size = 12,multi_probe_level = 1)
    search_params = dict(checks=50)   # or pass empty dictionary

    flann = cv2.FlannBasedMatcher(index_params, search_params)
    matches = flann.knnMatch(np.asarray(des1,np.float32),np.asarray(des2,np.float32), k=2)
    print '匹配数:',len(matches)
    good = []
    for m,n in matches:
        if m.distance < 0.8*n.distance:
            good.append(m)

    if len(good)>MIN_MATCH_COUNT:
        src_pts = np.float32([kp1[m.queryIdx].pt for m in good]).reshape(-1,1,2)
        dst_pts = np.float32([kp2[m.trainIdx].pt for m in good]).reshape(-1,1,2)

        # cv2.findHomography(srcPoints, dstPoints[, method[, ransacReprojThreshold[, mask]]]) → retval, mask
        # ransacReprojThreshold –Maximum allowed reprojection error to treat a point pair as an inlier (used in the RANSAC method only)
        M, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC, 5.0)
        matchesMask = mask.ravel().tolist()

        h,w = img1.shape
        pts = np.float32([ [0,0],[0,h-1],[w-1,h-1],[w-1,0] ]).reshape(-1,1,2)
        dst = cv2.perspectiveTransform(pts,M)
        # cv2.polylines(img, pts, isClosed, color[, thickness[, lineType[, shift]]]) → img
        img2 = cv2.polylines(img2,[np.int32(dst)],True, 127, 3, cv2.LINE_AA)
    else:
        print "Not enough matches are found - %d/%d" % (len(good),MIN_MATCH_COUNT)
        matchesMask = None

    draw_params = dict( matchColor = (0,255,0), # draw matches in green color
                        singlePointColor = None,
                        matchesMask = matchesMask, # draw only inliers
                        flags = 2)
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,good,None,**draw_params)
    plt.imshow(img3, 'gray'),plt.show()

# first_demo()
Homography()