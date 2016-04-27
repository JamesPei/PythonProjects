# __author__ = 'James'
# -*-coding:utf-8-*-

import cv2
import cv
import numpy as np


def Hough_circle_transform():
    img = cv2.imread('opencv.jpg', 0)
    img = cv2.medianBlur(img, 5)
    cimg = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)

    # cv2.HoughCircles(image, method, dp, minDist[, circles[, param1[, param2[, minRadius[, maxRadius]]]]]) → circles
    # method – Detection method to use. Currently, the only implemented method is CV_HOUGH_GRADIENT
    # dp – Inverse ratio of the accumulator resolution to the image resolution. For example, if dp=1 ,
    #       the accumulator has the same resolution as the input image. If dp=2 , the accumulator has half as big width and height.
    # minDist – Minimum distance between the centers of the detected circles. If the parameter is too small, multiple neighbor circles
    #       may be falsely detected in addition to a true one. If it is too large, some circles may be missed
    # circles – Output vector of found circles. Each vector is encoded as a 3-element floating-point vector  (x, y, radius)
    # param1 – First method-specific parameter. In case of CV_HOUGH_GRADIENT ,
    #       it is the higher threshold of the two passed to the Canny() edge detector (the lower one is twice smaller)
    # param2 – Second method-specific parameter. In case of CV_HOUGH_GRADIENT , it is the accumulator threshold for the circle centers
    #       at the detection stage. The smaller it is, the more false circles may be detected. Circles, corresponding to the larger
    #       accumulator values, will be returned first
    # cv2中找不到cv2.HOUGH_GRADIENT，所以method参数用了cv.CV_HOUGH_GRADIENT
    circles = cv2.HoughCircles(img, cv.CV_HOUGH_GRADIENT, 1, 50, param1=50, param2=50, minRadius=0, maxRadius=0)

    circles = np.uint16(np.around(circles))  # around:Evenly round to the given number of decimals
    for i in circles[0, :]:
        # draw the outer circle
        cv2.circle(cimg, (i[0], i[1]), i[2], (0, 255, 0), 2)
        # draw the center of the circle
        cv2.circle(cimg, (i[0], i[1]), 2, (0, 0, 255), 3)

    cv2.imshow('detected circles', cimg)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

Hough_circle_transform()
