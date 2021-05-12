#!/usr/bin/env python3
#-*- coding:utf-8 -*-

'多重继承C3算法'

__author__ = 'HUA'

class A(object):
    def foo(self):
        print('A foo')
    def bar(self):
        print('A bar')

class B(object):
    def foo(self):
        print('B foo')
    def bar(self):
        print('B bar')

class C1(A,B):
    pass

class C2MixIn(A,B):
    def bar(self):
        print('C2 bar')

class D(C1,C2MixIn):
    pass

if __name__ == '__main__':
    print(D.__mro__)
    d=D()
    d.foo()
    d.bar()