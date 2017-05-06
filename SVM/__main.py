# -*- coding: UTF-8 -*-

'''
this is a svm for sentiment\knownledge\society
'''

from _1knowledge  import knowledge
from _1sentiment  import sentiment
from _1society    import society
from _2stm_kld    import stm_kld
from _2stm_sct    import stm_sct
from _2kld_sct    import kld_sct
from _3target     import target

"""
from sklearn.svm import LinearSVC
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import make_scorer
from sklearn.metrics import accuracy_score

from sklearn.cross_validation import train_test_split
"""


def main():
    '''
    train and test 7 combination
    '''
    target()
    print('target success... \n')
    sentiment()
    print('sentiment success... \n')
    knowledge()
    print('knowledge success... \n')
    society()
    print('society success... \n')
    stm_kld()
    print('stm_kld success... \n')
    stm_sct()
    print('stm_sct success... \n')
    kld_sct()
    print('kld_sct success... \n')

main()
