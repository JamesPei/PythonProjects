#__author__ = 'James'
#-*-coding:utf-8

import cv2
import numpy as np

img = cv2.imread('tj.jpg', cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(img,127,255,0)
image, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

cnt = contours[2]
M = cv2.moments(cnt)        #图像矩
print M
cx = int(M['m10']/M['m00'])     #x轴对象重心
cy = int(M['m01']/M['m00'])     #y轴对象重心
print 'x:',cx
print 'y:',cy
area = cv2.contourArea(cnt)     #轮廓面积
print 'area:',area
perimeter = cv2.arcLength(cnt, True)    #轮廓周长,第二个参数用来指定对象的形状是闭合的还是打开的
print 'perimeter:',perimeter

#直边界矩形：一个直矩形，不会考虑边界的旋转，因此边界矩形的面积不是最小的
x, y, w, h = cv2.boundingRect(cnt)
# img = cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 2)

#旋转边界矩形
rect = cv2.minAreaRect(cnt) #Finds a rotated rectangle of the minimum area enclosing the input 2D point set.
box = cv2.boxPoints(rect)   #Finds the four vertices of a rotated rect. Useful to draw the rotated rectangle.
box = np.int0(box)
# img = cv2.drawContours(img,[box],0,(0,0,255),2)

#最小外接圆
(x,y),radius = cv2.minEnclosingCircle(cnt)
center = (int(x),int(y))
radius = int(radius)
# img = cv2.circle(img,center,radius,(0,255,0),2)

#椭圆拟合
ellipse = cv2.fitEllipse(cnt)
# img = cv2.ellipse(img, ellipse, (0,255,0), 2)

#直线拟合
rows,cols = img.shape[:2]
#cv2.fitLine(points, distType, param, reps, aeps[, line]) → line
#(vx, vy) is a normalized vector collinear to the line and (x0, y0) is a point on the line
[vx,vy,x,y] = cv2.fitLine(cnt, cv2.DIST_L2,0,0.01,0.01)
lefty = int((-x*vy/vx) + y)
righty = int(((cols-x)*vy/vx)+y)
print (cols-1,righty),(0,lefty)
# img = cv2.line(img,(cols-1,righty),(0,lefty),(0,255,0),2)

#Extreme Points
leftmost = tuple(cnt[cnt[:,:,0].argmin()][0])
rightmost = tuple(cnt[cnt[:,:,0].argmax()][0])
topmost = tuple(cnt[cnt[:,:,1].argmin()][0])
bottommost = tuple(cnt[cnt[:,:,1].argmax()][0])
print leftmost,rightmost,topmost,bottommost

cv2.imshow('1', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
