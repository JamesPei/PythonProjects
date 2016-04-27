#__author__ = 'James'
#-*-coding:utf-8

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('test.jpg',0)

#使用opencv统计直方图,注意:OpenCV 的函数比np.histogram快40倍，因此尽量使用opencv的函数
#cv2.calcHist(images, channels, mask, histSize, ranges[, hist[, accumulate]]) → hist¶
hist = cv2.calcHist([img],[0],None,[256],[0,256])   #除了mask其它都需要加[]
# print len(hist)

#使用Numpy统计直方图,效率不如opencv
#img.ravel():将图像转换为一维数组.It is equivalent to reshape(-1, order=order).
# hist,bins = np.histogram(img.ravel(),256,[0,256])

#绘制直方图
# plt.hist(img.ravel(), 256, [0, 256])
# plt.show()

#绘制多通道直方图
image = cv2.imread('test.jpg')
color=('b','g','r')
#对一个列表或数组既要遍历索引又要遍历元素时使用内置的enumerate会更加直接，
# enumerate会将数组或列表组成一个索引序列，使获取索引和索引内容时更加方便
for i, col in enumerate(color):
    histr = cv2.calcHist([image], [i], None, [256], [0,256])
    #Plot lines and/or markers to the Axes. args is a variable length argument,
    # allowing for multiple x, y pairs with an optional format string
    plt.plot(histr, color = col)
    plt.xlim([0, 256])  #Get or set the x limits of the current axes.
# plt.show()


#使用掩膜
# create a mask
mask = np.zeros(img.shape[:2], np.uint8)    #一个与原图同样大小的掩膜
mask[100:300, 100:400] = 255
#Calculates the per-element bit-wise conjunction of two arrays or an array and a scalar.
masked_img = cv2.bitwise_and(img,img,mask = mask)

# Calculate histogram with mask and without mask
# Check third argument for mask
hist_full = cv2.calcHist([img],[0],None,[256],[0,256])
hist_mask = cv2.calcHist([img],[0],mask,[256],[0,256])

plt.subplot(221), plt.imshow(img, 'gray')
plt.subplot(222), plt.imshow(mask,'gray')
plt.subplot(223), plt.imshow(masked_img, 'gray')
plt.subplot(224), plt.plot(hist_full), plt.plot(hist_mask)
plt.xlim([0,256])

plt.show()
