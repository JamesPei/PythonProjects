#__author__ = 'James'
#-*-coding:utf-8

import cv2

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

image = thresholding_inv(gray)
# 轮廓检测
_im_, contours, heirs = cv2.findContours(image.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# cropped = gray[y:y+h, x:x+w]
# resized = cv2.resize(cropped, (20, 20))
# cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 3)
# pos_image = PosImage((x, y), resized)
# images.append(pos_image)

name = 'test'
cv2.namedWindow(name)
cv2.imshow(name, image)
cv2.waitKey(0)
cv2.destroyAllWindows()