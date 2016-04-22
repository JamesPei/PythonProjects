#__author__ = 'James'
#-*-coding:utf-8

import cv2
import numpy as np
from kNN import main_predict

class PosImage(object):
    def __init__(self, pos, image):
        self.pos = pos
        self.image = image

    def get_position(self):
        return self.pos

    def get_image(self):
        return self.image

img = cv2.imread('number.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 二值图转换并做中值模糊
def thresholding_inv(gray):
    #由于轮廓检测算法需要从黑色的背景中搜索白色的轮廓，所有此处的 threshold 最后一项参数为 cv.CV_THRESH_BINARY_INV ，即反转黑白色。
    ret, bin = cv2.threshold(gray, 55, 255, cv2.THRESH_BINARY_INV)

    # 自适应阈值
    # bin = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 3, 2)
    # bin = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 3, 2)

    bin = cv2.medianBlur(bin, 3)

    return bin

def rearrange(images):
    return sorted(images, cmp=lambda x, y:cmp(x.get_position()[0], y.get_position()[0]))

def predict(letter):
    trainingData = np.load('knn_data.npz')
    train = trainingData['train']
    trainLabels = trainingData['train_labels']

    knn = cv2.KNearest()
    knn.train(train, trainLabels)

    letter = np.float32(letter)

    ret, result, neighbors, dist = knn.find_nearest(letter, k=5)
    return result


image = thresholding_inv(gray)

# 轮廓检测
contours, heirs = cv2.findContours(image.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
# cv2.drawContours(img, contours, 2, (0,255,0), 1)
cnt = contours[0]
cnt1 = contours[1]
cnt2 = contours[2]

x,y,w,h = cv2.boundingRect(cnt)
cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0), 1)
x1,y1,w1,h1 = cv2.boundingRect(cnt1)
cv2.rectangle(img,(x1,y1),(x1+w1,y1+h1),(0,255,0), 1)
x2,y2,w2,h2 = cv2.boundingRect(cnt2)
cv2.rectangle(img,(x2,y2),(x2+w2,y2+h2),(0,255,0), 1)

cropped = image[y:y+h, x:x+w]
resized = cv2.resize(cropped, (20, 20))
letter = resized.reshape(-1,400).astype(np.float32)
pred = predict(letter)
# main_predict(letter)

cropped1 = image[y1:y1+h1, x1:x1+w1]
resized1 = cv2.resize(cropped1, (20, 20))
letter1 = resized1.reshape(-1,400).astype(np.float32)
pred1 = predict(letter1)

cropped2 = image[y2:y2+h2, x2:x2+w2]
resized2 = cv2.resize(cropped2, (20, 20))
letter2 = resized2.reshape(-1,400).astype(np.float32)
pred2 = predict(letter2)

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, str(pred[0][0]), (x,y), font, 0.5, (0,0,255),1)
cv2.putText(img, str(pred1[0][0]), (x1,y1), font, 0.5, (0,0,255),1)
cv2.putText(img, str(pred2[0][0]), (x2,y2), font, 0.5, (0,0,255),1)

cv2.imshow('ori', img)
cv2.waitKey(0)
cv2.destroyAllWindows()