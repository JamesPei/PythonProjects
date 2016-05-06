#__author__ = 'James'
#-*-coding:utf-8-*-

import cv2
import numpy as np

font = cv2.FONT_HERSHEY_SIMPLEX

#霍夫直线变换
def Hough_line_transform():
    img = cv2.imread('benzene4.jpg')
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    #cv2.Canny(image, threshold1, threshold2[, edges[, apertureSize[, L2gradient]]]) → edges
    # edges = cv2.Canny(gray,50,150,apertureSize = 3)
    ret, edges = cv2.threshold(gray, 55, 255, cv2.THRESH_BINARY_INV)

    #cv2.HoughLines(image, rho, theta, threshold[, lines[, srn[, stn]]]) → lines
    #rho – Distance resolution of the accumulator in pixels.
    #theta – Angle resolution of the accumulator in radians
    #Accumulator threshold parameter. Only those lines are returned that get enough votes (>threshold)
    lines = cv2.HoughLines(edges,1,np.pi/180,30)
    print len(lines)
    find_benzene(lines)
    for i in range(len(lines)):
        for rho,theta in lines[i]:
            a = np.cos(theta)
            b = np.sin(theta)
            x0 = a*rho
            y0 = b*rho
            x1 = int(x0 + 1000*(-b))
            y1 = int(y0 + 1000*(a))
            x2 = int(x0 - 1000*(-b))
            y2 = int(y0 - 1000*(a))

            cv2.line(img,(x1,y1),(x2,y2),(0,0,255),1)

    return img

#概率性霍夫变换 is an optimization of Hough Transform we saw.
# It doesn’t take all the points into consideration, instead
# take only a random subset of points and that is sufficient for line detection
def probabilistic_hough_transform(path, min_LineLength, max_LineGap):
    img = cv2.imread(path)
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    # edges = cv2.Canny(gray,50,150,apertureSize = 3)
    ret, bin = cv2.threshold(gray, 55, 255, cv2.THRESH_BINARY_INV)
    minLineLength = min_LineLength     #Minimum length of line. Line segments shorter than this are rejected
    maxLineGap = max_LineGap     #Maximum allowed gap between line segments to treat them as single line

    lines = cv2.HoughLinesP(bin,1,np.pi/180,min_LineLength,minLineLength,maxLineGap)
    # print len(lines)
    find_benzene(lines)
    for i in range(len(lines)):
        for x1,y1,x2,y2 in lines[i]:
            # print (x1,y1),(x2,y2)
            cv2.line(img,(x1,y1),(x2,y2),(0,0,255),1)
            # cv2.putText(img, str((x1,y1)), (x1,y1), font, 0.3, (255,0,0),1)
            # cv2.putText(img, str((x2,y2)), (x2,y2), font, 0.3, (255,0,0),1)
            cv2.putText(img, str((min_LineLength,max_LineGap, len(lines))), (10,10), font, 0.3, (255,0,0),1)
    return img

def find_benzene(lines):
    list=[]
    for i in range(len(lines)):
        for x1,y1,x2,y2 in lines[i]:
            x1=float(x1)
            y1=float(y1)
            x2=float(x2)
            y2=float(y2)
            if (x2-x1)!=0: slope=(y2-y1)/(x2-x1)
            else: slope='inf'
            list.append((slope,(x1,y1),(x2,y2)))
    print len(list)
    print list
    for item in list:
        slope = item[0]     #斜率
        spoint = item[1]    #起点坐标
        epoint = item[2]    #终点坐标
        x1 = spoint[0]
        y1 = spoint[1]
        x2 = epoint[0]
        y2 = epoint[1]
        for item2 in list:
            if item==item2: continue
            slope2 = item2[0]
            spoint2 = item2[1]
            epoint2 = item2[2]
            x21 = spoint2[0]
            y21 = spoint2[1]
            x22 = epoint2[0]
            y22 = epoint2[1]
            if slope=='inf' and slope==slope2:  #若垂直于x轴
                if x21==x1 and y21!=y1:         #若不是同一条线
                    list.remove(item)
                    list.remove(item2)
                    list.append((slope,(x1,y1 if y1<y21 else y21),(x2, y22 if y22>y2 else y2)))     #合并
                if x1!=x21 and abs(x1-x21)<=4:
                    list.remove(item2)
            elif slope!='inf' and slope2!='inf' and abs(slope-slope2)<0.05:
                check_slope = (y21-y2)/(x21-x2)
                if abs(check_slope)<=0.01:
                    list.remove(item)
                    list.remove(item2)
                    list.append((slope,(min(x1,x2,x21,x22),min(y1,y2,y21,y22)),(max(x1,x2,x21,x22),max(y1,y2,y21,y22))))
    print len(list)
    print list

if __name__=='__main__':
    # img = Hough_line_transform()
    img = probabilistic_hough_transform('benzene01.jpg', 40, 8)
    # cv2.imshow('image',img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()