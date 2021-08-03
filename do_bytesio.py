#!/usr/bin/env python3
# -*- coding:utf-8 -*-

'bytesio'

__author__ = 'HUA'

from io import BytesIO

# write to BytesIO
f = BytesIO()
f.write(b'hello')
f.write(b' ')
f.write(b'world!')
print(f.getvalue())

#read from BytesIO
data = '哈哈哈哈哈'.encode('utf-8')
f = BytesIO(data)
print(f.read())

#write执行后，光标会到末尾，因此执行read()为空，需要用seek移动光标位置
f = BytesIO(b'hello ')
f.write(b'world ')
f.write(b'haha')
print(f.read())
f.seek(0)
print(f.read())