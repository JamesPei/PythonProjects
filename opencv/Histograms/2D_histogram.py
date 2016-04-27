#__author__ = 'James'
#-*-coding:utf-8

import cv2
from matplotlib import pyplot as plt

#opencv中的2D直方图
def opencv_2D_histogram():
    img = cv2.imread('test.jpg')
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    hist = cv2.calcHist([hsv], [0, 1], None, [180, 256], [0, 180, 0, 256])

#numpy中的2D直方图
# def numpy_2D_histogram():
#     img = cv2.imread('home.jpg')
#     hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
#     hist, xbins, ybins = np.histogram2d(h.ravel(),s.ravel(),[180,256],[[0,180],[0,256]])

#绘制2D直方图
def draw_2D_histogram():
    img = cv2.imread('bmw.jpg')
    hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    hist = cv2.calcHist([hsv], [0, 1], None, [180, 256], [0, 180, 0, 256] )

    plt.imshow(hist,interpolation = 'nearest')
    plt.show()

#opencv风格的2D直方图


draw_2D_histogram()
