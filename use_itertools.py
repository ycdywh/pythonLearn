#!/usr/bin/env python3
#-*- coding:utf-8 -*-

import itertools

#“无限”迭代器
natuals = itertools.count(1)
for n in natuals:
    print(n)
    if n >= 100:
        break

ns = itertools.takewhile(lambda x: x <= 10, natuals)
list(ns)

cs = itertools.cycle('ABC')
t = 10
for c in cs:
    print(c)
    t = t - 1
    if t == 0:
        break

#chain()可以把一组迭代对象串联起来，形成一个更大的迭代器：
for c in itertools.chain('ABC', 'XYZ'):
    print(c)

#groupby()把迭代器中相邻的重复元素挑出来放在一起：
for key, group in itertools.groupby('AAABBBCcAaa', lambda x: x.upper()):
    print(key, list(group))
