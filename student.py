#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'a student class'

__author__ = 'HUA'


class Student(object):
    def __init__(self, name, score, gender):
        self.name = name
        self.score = score
        self.__gender = gender

    def set_gender(self, gender):
        if gender in ('male','female'):
            self.__gender = gender
        else:
            raise ValueError('the value is error')

    def get_gender(self):
        return self.__gender

    def print_score(self):
        print('%s : %s' % (self.name, self.score))

    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'


lisa = Student('Lisa', 99, 'male')
bart = Student('Bart', 59, 'female')
print(lisa.name, lisa.get_grade() , lisa.get_gender())
print(bart.name, bart.get_grade())

lisa.age = 8
print(lisa.name, lisa.age)

lisa.set_gender('female')
print(lisa.name, lisa.get_grade() , lisa.get_gender())
