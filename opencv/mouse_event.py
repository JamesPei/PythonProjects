#__author__ = 'James'
#-*-coding:utf-8-*-

import cv2
import numpy as np

# 所有被支持的鼠标事件
# events = [i for i in dir(cv2) if 'EVENT' in i]
# print events

# 下面的代码在鼠标双击时会绘制一个圆
# mouse callback function
def draw_circle(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img,(x,y),10,(255,0,0),-1)

# Create a black image, a window and bind the function to window
img = np.zeros((512,512,3), np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_circle)

while(1):
    cv2.imshow('image',img)
    if cv2.waitKey(20) & 0xFF == 27:    #Esc退出
        break
cv2.destroyAllWindows()
