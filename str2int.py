#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from functools import reduce

DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

def str2int(s):
    def f(x,y):
        return x*10+y
    def m(x):
        return DIGITS.get(x)
    return reduce(f,map(m,s))

print(str2int('1337777'))  