#!/usr/bin/env python3
#-*- coding:utf-8 -*-

__author__ = 'HUA'


import pickle

d = dict(name='Bob' , age = 20, score = 88)
data = pickle.dumps(d)
print(data)
with open('dump.txt', 'wb') as f :
    f.write(data)

with open('dump.txt', 'rb') as f :
    print(pickle.load(f))


reborn = pickle.loads(data)
print(reborn)