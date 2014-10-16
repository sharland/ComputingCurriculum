#! /usr/local/bin/python3

f = open('searchexample.txt','r')

for i, line in enumerate(fileHandle, 1):
    if 'hammer' in line:
        print (i), line

f.close()
