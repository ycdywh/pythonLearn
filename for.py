#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections.abc import Iterable
def findMinAndMax(s):
    if isinstance(s,Iterable):
        min = None
        max = None
        for i,x in enumerate(s):
            if(i==0):
                min = x
                max = x
            else:
                if x<min :
                    min = x
                if x>max:
                    max = x
        print((min,max))
        return (min,max)
    else:
        print("不能进行迭代")
            
# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')