#!/usr/bin/env python3
#-*- coding:utf-8 -*-

'use_slots'

__author__ = 'HUA'


class Student(object):
    __slots__ = ('name', 'age')  # 用tuple定义允许绑定的属性名称


class GraduateStudent(Student):
    pass


s = Student()  #创建实例
s.name = 'AA'
s.age = 20
# ERROR: AttributeError: 'Student' object has no attribute 'score'
try:
    s.score = 99
except AttributeError as e:
    print('AttributeError:', e)

g = GraduateStudent()
g.score = 99
print('g.score = ', g.score)