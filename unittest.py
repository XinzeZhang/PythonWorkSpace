# -*- coding: UTF-8 -*-
"""
this is a combile txts pY
"""
import os
import glob

'''
def combilefiles():
    """
    test combile 3 files
    """
    outfile = open('SVM\\Result_Collection\\_SRC_Result.txt', 'a')

    infile1 = open('SVM\\Result\\_src_sentiment.txt', 'r')
    infile2 = open('SVM\\Result\\_src_knowledge.txt', 'r')
    infile3 = open('SVM\\Result\\_src_society.txt', 'r')

    outfile.write('_src_sentiment:\n')
    print('_src_sentiment:\n')
    for line in infile1:
        outfile.write(line)
        print(line)

    outfile.write('\n')
    print('\n')

    outfile.write('_src_knowledge: \n')
    print('_src_knowledge: \n')
    for line in infile2:
        outfile.write(line)
        print(line)

    outfile.write('\n')
    print('\n')

    outfile.write('_src_society: \n')
    print('_src_society: \n')
    for line in infile3:
        outfile.write(line)
        print(line)

    infile1.close()
    infile2.close()
    infile3.close()
    outfile.close()

combilefiles()
'''

def combiledic():
    '''
    combile dictionary's txt to one file.txt
    '''
    outfile_name = 'SVM\\Result_Collection\\_Try9_Result.txt'
    outfile = open(outfile_name, 'a')

    dictionary = 'SVM\\Result\\'

    errorfiles = []

    if not os.path.isdir(dictionary):
        print('input dictionary is not a dir')
        return False


    for file in glob.glob(os.path.join(dictionary, '*.txt')):
        print(file, end='\n')
        try:
            infile = open(file, 'r')
            for line in infile:
                outfile.write(line)
            outfile.write('\n')
            infile.close()
        except IOError:
            print('error files', file)
            errorfiles.append(file)

    outfile.close()

    print('combiledic completed, %d file(s) missed.' % len(errorfiles))
    print('combiledic file.txt: ', outfile_name)

    if len(errorfiles) > 0:  # 判断
        print('missed files:')
        print('--------------------------------')
        for file in errorfiles:
            print(file)
        print('--------------------------------')

combiledic()
