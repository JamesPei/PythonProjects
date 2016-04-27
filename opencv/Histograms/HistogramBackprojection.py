#__author__ = 'James'
#-*-coding:utf-8

import cv2
import numpy as np
from matplotlib import pyplot as plt

#numpy中的反向投影算法
def numpy_histogram_backprojection():
    #roi is the object or region of object we need to find
    roi = cv2.imread('rose_red.png')
    hsv = cv2.cvtColor(roi,cv2.COLOR_BGR2HSV)

    #target is the image we search in
    target = cv2.imread('rose.png')
    hsvt = cv2.cvtColor(target,cv2.COLOR_BGR2HSV)

    # Find the histograms using calcHist. Can be done with np.histogram2d also
    M = cv2.calcHist([hsv],[0, 1], None, [180, 256], [0, 180, 0, 256] )
    I = cv2.calcHist([hsvt],[0, 1], None, [180, 256], [0, 180, 0, 256] )

    # Find the ratio R = M/I. Then backproject R, ie use R as palette and
    # create a new image with every pixel as its corresponding probability of being target
    R = M/I

    h,s,v = cv2.split(hsvt)
    B = R[h.ravel(),s.ravel()]
    B = np.minimum(B,1)
    B = B.reshape(hsvt.shape[:2])

    # apply a convolution with a circular disc, B = D*B, where D is the disc kernel.
    disc = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
    cv2.filter2D(B,-1,disc,B)
    B = np.uint8(B)
    cv2.normalize(B,B,0,255,cv2.NORM_MINMAX)

    #Now the location of maximum intensity gives us the location of object. If we
    # are expecting a region in the image, thresholding for a suitable value gives a nice result.
    ret,thresh = cv2.threshold(B,50,255,0)

#opencv中的反向投影
def opencv_histogram_backprojection():
    roi = cv2.imread('messi_roi.png')
    hsv = cv2.cvtColor(roi,cv2.COLOR_BGR2HSV)

    target = cv2.imread('messi.jpg')
    hsvt = cv2.cvtColor(target,cv2.COLOR_BGR2HSV)

    # calculating object histogram
    roihist = cv2.calcHist([hsv],[0, 1], None, [180, 256], [0, 180, 0, 256])

    # normalize histogram and apply backprojection
    #归一化:原始图像，结果图像，映射到结果图像中的最小值，最大值，归一化类型
    #NORM_MINMAX 对数组的所有值进行转化，使它们线性映射到最小值和最大值之间
    #归一化后的直方图便于显示，归一化后就成了0－255之间的数了
    cv2.normalize(roihist,roihist,0,255,cv2.NORM_MINMAX)
    #Calculates the back projection of a histogram:cv2.calcBackProject(images, channels, hist, ranges, scale[, dst]) → dst
    dst = cv2.calcBackProject([hsvt],[0,1],roihist,[0,180,0,256],1)

    # Now convolute with circular disc
    # Returns a structuring element of the specified size and shape for morphological operations.
    # cv2.getStructuringElement(shape, ksize[, anchor]) → retval
    disc = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
    # Convolves an image with the kernel
    cv2.filter2D(dst,-1,disc,dst)

    # threshold and binary AND
    ret,thresh = cv2.threshold(dst,50,255,0)
    # Creates one multichannel array out of several single-channel ones
    thresh = cv2.merge((thresh,thresh,thresh))
    res = cv2.bitwise_and(target,thresh)

    res = np.hstack((target,thresh,res))
    cv2.imwrite('messi_res.jpg',res)

opencv_histogram_backprojection()

