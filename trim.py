#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def trimA(s):
    x = True 
    while(x):
        if s[0:1] != ' ' and s[-2:-1] != ' ':
            x = False
        if s[0:1] == ' ':
            s = s[1:]
        if s[-2:-1] == ' ':
            s = s[:-2]
    return s

def trim(s):
    if s[0:1] != ' ' and s[-2:-1] != ' ':
        return s
    if s[0:1] == ' ':
        s = s[1:]
    if s[-2:-1] == ' ':
        s = s[:-2]
    return trim(s)


# 测试:
if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')