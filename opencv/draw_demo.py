#__author__ = 'James'
#-*-coding:utf-8-*-

import numpy
import cv2

# Create a black image
img = numpy.zeros((512,512,3), numpy.uint8)

# Draw a diagonal blue line whith thickness of 5px
cv2.line(img, (0,0), (511, 511), (255,0,0), 5)

#画矩形,参数２,3 分别表示矩形左上定点和右下顶点
cv2.rectangle(img, (384,0), (510,128), (0,255,0), 3)

#画圆,指定圆心坐标及半径大小
cv2.circle(img, (447,63), 63, (0,0,255), -1)    #-1表示填充

#画椭圆,参数２：中心点坐标,参数３：长轴和短轴的长度,参数４:椭圆沿逆时针方向旋转的角度,参数5,6:椭圆弧沿顺时针方向起始的角度和结束角度，若是０或３６０则代表整个椭圆
cv2.ellipse(img, (256,256), (100,50), 0, 0, 90, (255,0,255), -1)

#画多边形：需要指定每个顶点的坐标.用这些点的坐标构建一个大小等于行数X1X2的数组，行数就是点的数目.这个数组的数据类型必须是int32
pts = numpy.array([[10,5],[20,30],[70,20],[50,10]], numpy.int32)
pts = pts.reshape((-1,1,2))  #这里的reshape的第一个参数是-1,表明这一维的长度是根据后面的维度计算出来的
img = cv2.polylines(img,[pts],True,(0,255,255))

#在图片上添加文字
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'opencv', (10,500), font, 4, (255,255,255),2)

name = 'test'
cv2.namedWindow(name)
cv2.imshow(name, img)
cv2.waitKey(0)
cv2.destroyAllWindows()
