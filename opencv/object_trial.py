#__author__ = 'James'
#-*-coding:utf-8-*-

import cv2
import numpy as np

cap = cv2.VideoCapture(0)  #必须显式的指定要开启的摄像头，如果只有一个设想头则设为0

while(1):
    # 获取每一帧
    ret, frame = cap.read()

    # 转换到HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # 设定蓝色的阈值
    lower_blue = np.array([110, 50, 50])
    upper_blue = np.array([130, 255, 255])

    # 根据阈值构建掩膜
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    # 对源图像和掩膜进行位运算
    res = cv2.bitwise_and(frame, frame, mask=mask)

    # 显示图像
    cv2.imshow('frame',frame)
    cv2.imshow('mask', mask)
    cv2.imshow('res', res)
    k = cv2.waitKey(5)&0xFF
    if k==27:
        break

cv2.destroyAllWindows()
