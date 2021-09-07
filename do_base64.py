#!/usr/bin/env python3
#-*- coding:utf-8 -*-

import base64

s = base64.b64encode('在Python中使用BASE 64编码'.encode('utf-8'))
print(s)
d = base64.b64decode(s).decode('utf-8')
print(d)

s = base64.urlsafe_b64encode('在Python中使用BASE 64编码'.encode('utf-8'))
print(s)
d = base64.urlsafe_b64decode(s).decode('utf-8')
print(d)


def safe_base64_decode(s):
    while len(s) % 4 != 0:
        s = s + "="
    return base64.b64decode(s)


# 测试:
assert b'abcd' == safe_base64_decode('YWJjZA=='), safe_base64_decode(
    'YWJjZA==')
assert b'abcd' == safe_base64_decode('YWJjZA'), safe_base64_decode('YWJjZA')
print('ok')