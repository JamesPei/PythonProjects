#__author__ = 'James'
#-*-coding:utf-8

import numpy as np
# from detect_numbers import predict
import cv2

knn = cv2.ml.KNearest_create()    # 如果是opencv3则在此处不同

def predict_old(test):
    img = cv2.imread('digits.png')
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    # now we split the image to 5000 cells, each 20*20 size
    cells = [np.hsplit(row, 100) for row in np.vsplit(gray,50)]

    # Make it into a Numpy array. It size will be (50,100,20,20)
    x = np.array(cells)

    # now we prepare train_data and test_data
    train = x[:,:50].reshape(-1,400).astype(np.float32)     #Gives a new shape to an array without changing its data.
    if test==None: test = x[:, 50:100].reshape(-1,400).astype(np.float32)
    # create labels for train and test data
    k = np.arange(10)

    train_labels = np.repeat(k,250)[:, np.newaxis]  # Repeat elements of an array.
    test_labels = train_labels.copy()

    #cv2.KNearest.find_nearest(samples, k[, results[, neighborResponses[, dists]]]) → retval, results, neighborResponses, dists
    ret,result,neighbours,dist = knn.findNearest(test.reshape(-1,400).astype(np.float32),k=5)
    print '2-----:',result


    # Now we check the accuracy of classification
    # For that, compare the result with test_labels and check which are wrong
    matches = result==test_labels
    correct = np.count_nonzero(matches) # Counts the number of non-zero values in the array a.

    accuracy = correct*100.0/result.size
    print 'accuracy:',accuracy

    np.savez('knn_data.npz',train=train,train_labels=train_labels)

def train():
    img = cv2.imread('digits.png')
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    # now we split the image to 5000 cells, each 20*20 size
    cells = [np.hsplit(row, 100) for row in np.vsplit(gray,50)]

    # Make it into a Numpy array. It size will be (50,100,20,20)
    x = np.array(cells)

    # now we prepare train_data and test_data
    train = x[:,:].reshape(-1,400).astype(np.float32)     #Gives a new shape to an array without changing its data.
    k = np.arange(10)

    train_labels = np.repeat(k,500)[:, np.newaxis]  # Repeat elements of an array.

    #initiate kNN, train the data, then test it with test data for k=1
    knn.train(train, cv2.ml.ROW_SAMPLE, train_labels)

    np.savez('knn_data.npz',train=train,train_labels=train_labels)

def main_predict(test):
    #cv2.KNearest.find_nearest(samples, k[, results[, neighborResponses[, dists]]]) → retval, results, neighborResponses, dists
    train()
    ret,result,neighbours,dist = knn.findNearest(test.reshape(-1,400).astype(np.float32),k=5)
    print '2-----:',result

if __name__=='__main__':
    # img = cv2.imread('1_.jpg')
    # gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    # test = gray.reshape(-1,400).astype(np.float32)
    # main_predict(test)
    train()
