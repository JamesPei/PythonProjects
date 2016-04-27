#__author__ = 'James'
#-*-coding:utf-8

import cv2
import numpy as np

font = cv2.FONT_HERSHEY_SIMPLEX

def detect_numbers(original_image=None):
    if not original_image:img = cv2.imread('2.jpg')
    else: img = cv2.imread(original_image)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    image = thresholding_inv(gray)
    resizeds = detect_contours(img, image, 0.2) #img:原图, image:阈值处理后的图, 0.2：缩放比例

    cv2.imshow('result', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# 二值图转换并做中值模糊
def thresholding_inv(gray):
    #由于轮廓检测算法需要从黑色的背景中搜索白色的轮廓，所有此处的 threshold 最后一项参数为 cv.CV_THRESH_BINARY_INV ，即反转黑白色。
    ret, bin = cv2.threshold(gray, 55, 255, cv2.THRESH_BINARY_INV)

    # 自适应阈值
    # bin = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 3, 2)
    # bin = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 3, 2)

    bin = cv2.medianBlur(bin, 3)

    return bin

#图像识别
def predict(letter):
    trainingData = np.load('knn_data.npz')
    train = trainingData['train']
    trainLabels = trainingData['train_labels']

    knn = cv2.KNearest()
    knn.train(train, trainLabels)

    letter = np.float32(letter)

    ret, result, neighbors, dist = knn.find_nearest(letter, k=5)
    print '预测结果:',result
    return result

# 轮廓检测
def detect_contours(img, image, scale):
    contours, heirs = cv2.findContours(image.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # cv2.drawContours(img, contours, 2, (0,255,0), 1)

    resizeds = []
    for cnt in contours:
        x,y,w,h = cv2.boundingRect(cnt)     #元素左下角坐标（x,y）以及宽(w)高(h)
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0), 1)     #在原图上给元素画矩形框

        kernel=np.ones((3,3),np.uint8)
        image = cv2.dilate(image,kernel,iterations=1)   #膨胀

        #resize图片
        if y-h*scale>0 and x-w*scale>0:
            cropped = image[y-h*scale:y+h*(1+scale), x-w*scale:x+w*(1+scale)]
        elif y-h*scale>0:
            cropped = image[y-h*scale:y+h*(1+scale), 0:x+w*(1+scale)]
        elif x-w*scale>0:
            cropped = image[0:y+h*(1+scale), x-w*scale:x+w*(1+scale)]
        else:
            cropped = image[0:y+h*(1+scale), 0:x+w*(1+scale)]
        resized = cv2.resize(cropped, (20, 20))
        letter = resized.reshape(-1,400).astype(np.float32)

        #识别图像
        pred = predict(letter)
        cv2.putText(img, str(int(pred[0][0])), (x,y), font, 0.5, (255,0,0),2)

        resizeds.append(resized)

    return resizeds

if __name__=='__main__':
    for i in range(10):
        img_path = str(i)+'.jpg'
        detect_numbers(img_path)