#__author__ = 'James'
#-*-coding:utf-8-*-

import numpy as np
import cv2
from matplotlib import pyplot as plt

# load the image and convert it to grayscale
image = cv2.imread("./BarcodeDetect/barcode.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# compute the Scharr gradient magnitude representation of the images in both the x and y direction
# Calculates the first x- or y- image derivative using Scharr operator:cv2.Scharr(src, ddepth, dx, dy[, dst[, scale[, delta[, borderType]]]]) → dst
gradX = cv2.Sobel(gray, ddepth = cv2.CV_32F, dx = 1, dy = 0, ksize = -1)    #对x方向求导，卷积核３＊３
gradY = cv2.Sobel(gray, ddepth = cv2.CV_32F, dx = 0, dy = 1, ksize = -1)    #对y方向求导，卷积核３＊３

# subtract the y-gradient from the x-gradient,通过这一步减法操作，最终得到包含高水平梯度和低竖直梯度的图像区域。
gradient = cv2.subtract(gradX, gradY)   #Calculates the per-element difference between two arrays or array and a scalar.
gradient = cv2.convertScaleAbs(gradient)    #Scales, calculates absolute values, and converts the result to 8-bit.

# blur and threshold the image,通过去噪仅关注条形码区域
blurred = cv2.blur(gradient, (9, 9))    #使用9*9的内核对梯度图进行平均模糊，这将有助于平滑梯度表征的图形中的高频噪声。
(_, thresh) = cv2.threshold(blurred, 225, 255, cv2.THRESH_BINARY)   #梯度图中任何小于等于255的像素设为0（黑色），其余设为255（白色）

# construct a closing kernel and apply it to the thresholded image
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (21, 7)) #使用cv2.getStructuringElement构造一个长方形内核。这个内核的宽度大于长度，因此我们可以消除条形码中垂直条之间的缝隙。
closed = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)  #这里进行形态学操作，将上一步得到的内核应用到我们的二值图中，以此来消除竖杠间的缝隙。cv2.MORPH_CLOSE:先膨胀再腐蚀

# perform a series of erosions and dilations
closed = cv2.erode(closed, None, iterations = 4)
closed = cv2.dilate(closed, None, iterations = 4)

# find the contours in the thresholded image, then sort the contours by their area, keeping only the largest one
(img, cnts, hierarchy) = cv2.findContours(closed.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
c = sorted(cnts, key = cv2.contourArea, reverse = True)[0]

# compute the rotated bounding box of the largest contour
rect = cv2.minAreaRect(c)
box = np.int0(cv2.boxPoints(rect))
# draw a bounding box arounded the detected barcode and display the image
cv2.drawContours(image, [box], -1, (0, 255, 0), 3)

name = 'test'
cv2.namedWindow(name)
cv2.imshow(name, image)
cv2.waitKey(0)
cv2.destroyAllWindows()

