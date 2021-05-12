#!/usr/bin/env python3
#-*- coding:utf-8 -*-

'a test model'

__author__ = 'Hua'

import sys

def test():
    args = sys.argv
    if len(args) == 1:
        print('Hello World!')
    elif len(args) == 2:
        print('Hello,%s'%args[1])
    else:
        print('Too many arguments!')

if __name__ == '__main__':
    test()

import numpy as np
a = np.arange(8)
print ('原始数组：')
print (a)
print ('\n')
 
b = a.reshape(4,2)
print ('修改后的数组：')
print (b)