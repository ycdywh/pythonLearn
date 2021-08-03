#!/usr/bin/env python3
#-*- condig:utf-8 -*-

'Stringio'

__author__ = 'HUA'

from io import StringIO

# write to StringIO
f = StringIO()
f.write('Hello')
f.write(' ')
f.write('world!')
print(f.getvalue())

#read from StringIO
f = StringIO('哈哈哈哈，\n 我是誰，\n 你是誰')
while True:
    s = f.readline()
    if s == '':
        break
    print(s.strip())
