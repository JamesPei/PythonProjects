#__author__ = 'James'
#-*-coding:utf8-*-

import cv2

#设置视频捕获
cap = cv2.VideoCapture(0)   #从摄像头或文件捕获视频，通过一个整数进行初始化，该整数为视频设备ID，如果仅有一个摄像头，那么该摄像头ID为0

#获取视频帧，应用高斯平滑，显示结果
while True:
    ret, im = cap.read()    #解码并返回下一视频帧，ret：判断视频帧是否成功读入的标志， im：实际读入的图像数组
    blur = cv2.GaussianBlur(im, (0,0), 5)   #用高斯滤波器对传入的图像进行滤波，需要为高斯函数设定滤波器尺寸（参数2）及标准差（参数3）
    cv2.imshow('camera blur', blur)
    if cv2.waitKey(10) == 27:   #等待用户按键，若按下Esc键则退出应用，若按下空格键，则保存该视频帧
        break
