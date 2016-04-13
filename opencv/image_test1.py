#__author__ = 'James'
#-*-coding:utf-8-*-

import numpy
import cv2
from matplotlib import pyplot

img = cv2.imread('github_test.jpg')
img = cv2.flip(img,0)
cv2.imwrite('github_test1.jpg',img)
# cv2.imshow('test1',img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
