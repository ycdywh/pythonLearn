#!/usr/bin/env python3
# -*- coding:utf-8 -*-

__author__ = 'HUA'

from datetime import datetime

with open(r'c:\Users\weihua\Desktop\2.txt',
          'r',
          encoding='utf-8',
          errors='ignore') as f:
    #s = f.read()
    #print(s)
    for line in f.readlines():
        print(line.strip())  # 把末尾的'\n'删掉

with open('test.txt', 'w', encoding='utf-8') as f:
    f.write('今天是')
    f.write(datetime.now().strftime('%Y-%m-%d'))

with open('test.txt', 'r', encoding='utf-8') as f:
    s = f.read()
    print('open for read...')
    print(s)

with open('test.txt', 'rb') as f:
    s = f.read()
    print('open as binary for read...')
    print(s)
