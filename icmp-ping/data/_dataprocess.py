# coding:utf-8
import os
import codecs
import fileinput
infile = open('data\\school_name.txt', 'r', encoding='utf-8')
outfile = open('data\\temp.txt', 'w', encoding='utf-8')

count = 0
for line in infile.readlines():
    count += 1
    line = line.replace(" ", "\t")
    outfile.write(line)

infile.close()
outfile.close()
