#__author__ = 'James'
#-*-coding:utf-8

import cv2
import numpy as np
from matplotlib import pyplot as plt

def get_historgam():
    img = cv2.imread('test.jpg',0)
    cdf = draw_histogram(img)
    #构建Numpy掩膜数组，cdf为原数组，当数组元素为０时掩盖（计算时被忽略)
    cdf_m = np.ma.masked_equal(cdf,0)
    cdf_m = (cdf_m - cdf_m.min())*255/(cdf_m.max()-cdf_m.min())
    #对被掩盖的数组赋值，此处赋０
    cdf = np.ma.filled(cdf_m,0).astype('uint8')

    img2 = cdf[img]
    # cv2.imwrite('test2.jpg',img2)
    draw_histogram(img2)

def draw_histogram(img = None):
    #flatten()将数组变为一维
    hist,bins = np.histogram(img.flatten(),256,[0,256])
    #计算累计分布图
    #Return the cumulative sum of the elements along a given axis. a=array([[1, 2, 3],[4, 5, 6]]),np.cumsum(a)=array([ 1,  3,  6, 10, 15, 21])
    cdf = hist.cumsum()
    cdf_normalized = cdf * hist.max()/ cdf.max()

    plt.plot(cdf_normalized, color = 'b')
    plt.hist(img.flatten(),256,[0,256], color = 'r')
    plt.xlim([0,256])
    plt.legend(('cdf','histogram'), loc = 'upper left')
    plt.show()

    return cdf

def opencv_histogram(img=None):
    img = cv2.imread('test.jpg',0)
    equ = cv2.equalizeHist(img)
    #stacking images side-by-side
    #hstack():Take a sequence of arrays and stack them horizontally to make a single array. Rebuild arrays divided by hsplit.
    res = np.hstack((img,equ))
    cv2.imwrite('res.png',res)

def CLAHE():
    img = cv2.imread('test.jpg',0)
    # create a CLAHE object (Arguments are optional).
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
    cl1 = clahe.apply(img)

    cv2.imwrite('clahe_2.jpg',cl1)

# opencv_histogram()
# get_historgam()
CLAHE()