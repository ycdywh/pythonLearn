#!/usr/bin/env python3
#-*- coding:utf-8 -*-

'try except finally'

__author__ = 'HUA'

try:
    print('try...')
    r = 10/0
    print('result:',r)
except ZeroDivisionError as e:
    print('except:',e)
finally:
    print('finally...')
print('end')