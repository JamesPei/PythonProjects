#__author__ = 'James'
#-*-coding:utf-8-*-

import cv2

def preprocessing(image_path):
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    ret, bin = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)

    resized = cv2.resize(bin, (100, 100))
    list=[]
    for i in range(0,360,5):
        dst = rotate(resized, i)
        list.append(dst.flatten())

    return list

def rotate(img, angle):
    rows, cols = img.shape
    M = cv2.getRotationMatrix2D((cols/2, rows/2), angle, 1)
    dst = cv2.warpAffine(img, M, (1*cols, 1*rows))

    return dst

if __name__=='__main__':
    preprocessing('benzene.jpg')


