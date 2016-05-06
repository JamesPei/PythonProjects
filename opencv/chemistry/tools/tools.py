#__author__ = 'James'
#-*-coding:utf-8-*-

import cv2
import numpy as np

def erode(path, new_path=None, generate=False):

    img = cv2.imread(path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = thresholding_inv(gray)

    kernel = np.ones((5,5), np.uint8)
    erosion = cv2.erode(img, kernel, iterations = 1)

    if generate and new_path:    cv2.imwrite(new_path, erosion)
    else:   return erosion

# 二值图转换并做中值模糊
def thresholding_inv(gray):
    #由于轮廓检测算法需要从黑色的背景中搜索白色的轮廓，所有此处的 threshold 最后一项参数为 cv.CV_THRESH_BINARY_INV ，即反转黑白色。
    ret, bin = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)
    # 自适应阈值
    # bin = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 3, 2)
    # bin = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 3, 2)
    bin = cv2.medianBlur(bin, 3)

    return bin

if __name__=='__main__':
    img = cv2.imread('benzene3.jpg')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, bin = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)
    bin = cv2.resize(bin, (50,50))
    cv2.imwrite('benzene4.jpg', bin)
