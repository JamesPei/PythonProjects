#__author__ = 'James'
#-*-coding:utf-8-*-

import cv2
import numpy as np
import matplotlib as plt

def detect_alphabets():

    # Load the data, converters convert the letter to a number
    # numpy.loadtxt(fname, dtype=<type 'float'>, comments='#', delimiter=None, converters=None, skiprows=0, usecols=None, unpack=False, ndmin=0)[source]
    data = np.loadtxt('letter-recognition.data', dtype= 'float32', delimiter = ',', converters= {0: lambda ch: ord(ch)-ord('A')})

    # split the data to two, 10000 each for train and test
    train, test = np.vsplit(data,2)

    # split trainData and testData to features and responses
    responses, trainData = np.hsplit(train,[1])
    labels, testData = np.hsplit(test,[1])

    # Initiate the kNN, classify, measure accuracy.
    knn = cv2.ml.KNearest_create()
    knn.train(trainData, cv2.ml.ROW_SAMPLE, responses)
    ret, result, neighbors, dist = knn.findNearest(testData, k=5)

    correct = np.count_nonzero(result == labels)
    accuracy = correct*100.0/10000
    print accuracy

detect_alphabets()