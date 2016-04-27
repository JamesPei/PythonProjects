#__author__ = 'James'
#-*-coding:utf-8

import numpy as np
import cv2

knn = cv2.KNearest()    # 如果是opencv3则在此处不同

def train(path):
    img = cv2.imread('digits.png')
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)