#!/usr/bin/env pythons
#-*- coding:utf-8 -*-

__author__ = 'HUA'


class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def get_grade(self):
        if self.score > 100 or self.score < 0:
            raise ValueError
        elif self.score >= 80:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'