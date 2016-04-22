#__author__ = 'James'
#-*-coding:utf-8

import pickle
from numpy import array
from numpy import vstack

from matplotlib.pyplot import show

import imtools
import knntest
import os

print os.getcwd()

#用pickle载入二维数据点
# with open('points_normal.pkl', 'r') as f:
with open('/home/jamespei/workspace/machine_learning/kNN/points_ring.pkl', 'r') as f:
    class_1 = pickle.load(f)
    class_2 = pickle.load(f)
    labels = pickle.load(f)

#创建一个kNN分类器模型
model = knntest.KnnClassifier(labels, vstack((class_1, class_2)))

#用pickle模块载入测试数据
# with open('points_normal_test.pkl', 'r') as f:
with open('/home/jamespei/workspace/machine_learning/kNN/points_ring_test.pkl', 'r') as f:
    class_1 = pickle.load(f)
    class_2 = pickle.load(f)
    labels = pickle.load(f)

#在测试数据集的第一个数据点上进行测试
# print model.classify(class_1[0])

#定义绘图函数
def classify(x,y,model = model):
    return array([model.classify([xx,yy]) for (xx,yy) in zip(x,y)])

#绘制分类边界
imtools.plot_2D_boundary([-6, 6, -6, 6], [class_1, class_2], classify, [1, -1])
show()
