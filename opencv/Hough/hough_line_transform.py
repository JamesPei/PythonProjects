#__author__ = 'James'
#-*-coding:utf-8-*-

import cv2
import numpy as np

#霍夫直线变换
def Hough_line_transform():
    img = cv2.imread('sd.jpg')
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    #cv2.Canny(image, threshold1, threshold2[, edges[, apertureSize[, L2gradient]]]) → edges
    edges = cv2.Canny(gray,50,150,apertureSize = 3)

    #cv2.HoughLines(image, rho, theta, threshold[, lines[, srn[, stn]]]) → lines
    #rho – Distance resolution of the accumulator in pixels.
    #theta – Angle resolution of the accumulator in radians
    #Accumulator threshold parameter. Only those lines are returned that get enough votes (>threshold)
    lines = cv2.HoughLines(edges,1,np.pi/180,150)
    for rho,theta in lines[0]:
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a*rho
        y0 = b*rho
        x1 = int(x0 + 1000*(-b))
        y1 = int(y0 + 1000*(a))
        x2 = int(x0 - 1000*(-b))
        y2 = int(y0 - 1000*(a))

        cv2.line(img,(x1,y1),(x2,y2),(0,0,255),2)

    return img

#概率性霍夫变换 is an optimization of Hough Transform we saw.
# It doesn’t take all the points into consideration, instead
# take only a random subset of points and that is sufficient for line detection
def probabilistic_hough_transform():
    img = cv2.imread('sd.jpg')
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray,50,150,apertureSize = 3)
    minLineLength = 50     #Minimum length of line. Line segments shorter than this are rejected
    maxLineGap = 10     #Maximum allowed gap between line segments to treat them as single line

    lines = cv2.HoughLinesP(edges,1,np.pi/180,50,minLineLength,maxLineGap)
    for x1,y1,x2,y2 in lines[0]:
        cv2.line(img,(x1,y1),(x2,y2),(0,255,0),2)
    cv2.imwrite('houghlines5.jpg',img)

# img = Hough_line_transform()
# cv2.imwrite('houghlines_test.jpg',img)
probabilistic_hough_transform()