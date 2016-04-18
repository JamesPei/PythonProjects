#__author__ = 'James'
#-*-coding:utf-8-*-

import cv2

im = cv2.imread('python.jpg') #读取图片,返回的是一个标准的NumPy数组，该方法会根据文件后缀自动转换图像
h, w = im.shape[:2] #宽，高
print h,w

#cv2.imwrite('python_logo.png', im)  #保存图像
#opencv默认为BGR通道。颜色空间的转换可以使用cvtColor()函数来实现
gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)  #创建灰度图像

# 计算积分图像
intim = cv2.integral(gray)  #创建一幅图像，该图像的每个像素值是原图上方和左边强度值相加的结果，这对于快速评估特征是一个非常有用的技巧
#归一化并保存
intim = (255.0*intim)/intim.max()
cv2.imwrite('result.jpg', intim)






