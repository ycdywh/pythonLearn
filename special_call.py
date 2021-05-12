#!/usr/bin/env python3
#-*- coding:utf-8 -*-

'__call__'

__author__ = 'HUA'

class Student(object):
    def __init__(self, name):
        self.name = name 
    def __call__(self):
        print('My name is %s.' % self.name)

s = Student('AAA')
s()