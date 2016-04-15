#__author__ = 'James'
#-*-coding:utf-8-*-

import cv2
import numpy as np
from matplotlib import pyplot as plt

# img = cv2.imread('messi.jpg', 0)
# rows,cols = img.shape

# 缩放
# res = cv2.resize(img,None,fx=2, fy=2, interpolation = cv2.INTER_CUBIC)
#OR
# height, width = img.shape[:2]
# res = cv2.resize(img,(2*width, 2*height), interpolation = cv2.INTER_CUBIC)

#平移
# M = np.float32([[1,0,100],[0,1,50]])
# dst = cv2.warpAffine(img,M,(cols,rows))

# 旋转
# M = cv2.getRotationMatrix2D((cols/2,rows/2),45,1)
# dst = cv2.warpAffine(img,M,(cols,rows))

# while(1):
#     # cv2.imshow('res',res)
#     cv2.imshow('img',img)
#     cv2.imshow('dst',dst)
#
#     if cv2.waitKey(1) & 0xFF == 27:
#         break
#
# cv2.destroyAllWindows()

# 仿设变换
# img1 = cv2.imread('messi.jpg')
# rows,cols,ch = img1.shape
# pts1 = np.float32([[50,50],[200,50],[50,200]])
# pts2 = np.float32([[1,100],[200,50],[20,250]])
#
# M = cv2.getAffineTransform(pts1,pts2)
# dst = cv2.warpAffine(img1,M,(cols,rows))
# img = img1

#透视变换
img = cv2.imread('sd.jpg')
rows,cols,ch = img.shape
pts1 = np.float32([[164,16],[422,15],[150,317],[430, 320]])
pts2 = np.float32([[0,0],[280,0],[0,300],[280,300]])
M = cv2.getPerspectiveTransform(pts1, pts2)

dst = cv2.warpPerspective(img, M, (325,300))

plt.subplot(121),plt.imshow(img),plt.title('Input')
plt.subplot(122),plt.imshow(dst),plt.title('Output')
plt.show()



