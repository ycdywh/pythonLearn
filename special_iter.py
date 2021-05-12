#!/usr/bin/env python3
#-*- coding:utf-8 -*-

'__iter__'

__author__ = 'HUA'

class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1 #初始化两个计数器
    def __iter__(self):
        return self #返回迭代对象
    def __next__(self):
        self.a , self.b = self.b , self.a + self.b #计算下一个值
        if self.a > 100000:
            raise StopIteration #跳出循环
        return self.a

for n in Fib():
    print(n)