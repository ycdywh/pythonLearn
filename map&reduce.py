#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def normalize(name):
    L = len(name)
    if L == 0:
        return None
    elif L == 1:
        return name.upper()
    else:
        return name[0].upper() + name[1:].lower()
# 测试:
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)

#-------------------------------
from functools import reduce
def prod(L):
    m = reduce(lambda x,y: x*y, L)
    return m
#测试
print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')

#----------------------------------
DIGITS = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6}
def str2float(s):
    sList = s.split('.')
    start = sList[0]
    end = sList[1]
    index = len(end)
    all = start + end
    def char2num(x):
        return DIGITS.get(x)
    r = reduce(lambda x,y:x*10 + y,map(char2num,all))/10**index
    return r
print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')