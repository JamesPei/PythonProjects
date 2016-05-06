#__author__ = 'James'
#-*-coding:utf-8-*-

import cv2
from Hough_chem import probabilistic_hough_transform

for i in range(1,40):
    img = probabilistic_hough_transform('benzene01.jpg', i, 1)
    cv2.imwrite('./test_img/'+str(i)+'.jpg',img)