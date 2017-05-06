# -*- coding: UTF-8 -*-
"""
this is a svm for sentiment
"""

import numpy as np
from sklearn import svm
from sklearn import metrics
# import scipy as sp
#from sklearn.svm import SVR
#from sklearn import cross_validation

#import datetime
#import time
#import pickle as pickle
"""
from sklearn.svm import LinearSVC
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import make_scorer
from sklearn.metrics import accuracy_score

from sklearn.cross_validation import train_test_split
"""
TRAIN_INPUT = np.loadtxt('SVM\\Inputs\\train.txt')
TRAIN_1 = TRAIN_INPUT[:, 5:6]
# TRAIN_2 = TRAIN_INPUT[:, 5:8]
# TRAIN_SETS = np.concatenate((TRAIN_1, TRAIN_2), axis=1)
TRAIN_SETS = TRAIN_1
TRAIN_LABLE = TRAIN_INPUT[:, 13]

TEST_INPUT = np.loadtxt('SVM\\Inputs\\test.txt')
TEST_1 = TEST_INPUT[:, 5:6]
# TEST_2 = TEST_INPUT[:, 5:8]
# TEST_SETS = np.concatenate((TEST_1, TEST_2), axis=1)
TEST_SETS = TEST_1
TEST_LABLE = TEST_INPUT[:, 13]

#clf_linear = svm.SVC(kernel='linear').fit(TRAIN_SETS, TRAIN_LABLE)
#clf_linear  = svm.LinearSVC().fit(x, y)
#clf_poly = svm.SVC(kernel='poly', degree=3).fit(TRAIN_SETS, TRAIN_LABLE)
#clf_sigmoid = svm.SVC(kernel='sigmoid').fit(TRAIN_SETS, TRAIN_LABLE)
CLF = svm.SVC(kernel='rbf').fit(TRAIN_SETS, TRAIN_LABLE)



def sentiment():
    '''
    write the result to the sentiment.txt
    只选择高斯核函数一种进行学习
    '''
# for i, clf in enumerate((clf_linear, clf_poly, clf_rbf, clf_sigmoid)):

    predict = CLF.predict(TEST_SETS)

    accuracy = metrics.accuracy_score(TEST_LABLE, predict)
    precision = metrics.precision_score(TEST_LABLE, predict)
    recall = metrics.recall_score(TEST_LABLE, predict)
    f_1 = metrics.f1_score(TEST_LABLE, predict)

    # print result
    print('Accuracy : %.2f%%' % (100 * accuracy))
    print('Precision : %.2f%%' % (100 * precision))
    print('Recall : %.2f%%' % (100 * recall))
    print('F_1 : %.2f%%' % (100 * f_1))

    output = open("SVM\\Result\\_src_sentiment.txt", "w")
    '''
    write the result to the sentiment.txt
    '''
    output.writelines('_src_sentiment:  ')
    output.writelines('F_1 : %.2f%% \n' % (100 * f_1))
    output.writelines('Accuracy : %.2f%% \n' % (100 * accuracy))
    output.writelines('Precision : %.2f%% \n' % (100 * precision))
    output.writelines('Recall : %.2f%% \n' % (100 * recall))
    output.writelines('F_1 : %.2f%% \n' % (100 * f_1))
    output.close()

sentiment()
