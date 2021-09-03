#!/usr/bin/env python3
#-*- coding:utf-8 -*-

import re


#请尝试写一个验证Email地址的正则表达式。版本一应该可以验证出类似的Email：
def is_valid_email(addr):
    m = re.match(r'^([0-9a-zA-Z][0-9a-zA-Z.]+)@([0-9a-zA-Z.]+)$', addr)
    if m:
        return True
    else:
        print("failed! ", addr)


# 测试:
assert is_valid_email('someone@gmail.com')
assert is_valid_email('bill.gates@microsoft.com')
assert not is_valid_email('bob#example.com')
assert not is_valid_email('mr-bob@example.com')
print('ok')


#版本二可以提取出带名字的Email地址
def name_of_email(addr):
    m = re.match(r'^<([\w\s]+)>([\w\s.]+)@([0-9a-zA-Z.]+)$', addr)
    m2 = re.match(r'^([\w.]+)@([0-9a-zA-Z.]+)$', addr)
    if m:
        print(m.groups())
        return m.group(1)
    elif m2:
        print(m2.groups())
        return m2.group(1)
    else:
        return None


# 测试:
assert name_of_email('<Tom Paris> tom@voyager.org') == 'Tom Paris'
assert name_of_email('tom@voyager.org') == 'tom'
print('ok')
