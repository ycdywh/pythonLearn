#!/usr/bin/env python3
#-*-coding:utf-8 -*-

__author__ = 'HUA'


def foo(s):
    n = int(s)
    assert n != 0, 'n is zeso!'
    return 10 / n


def main():
    foo('1')


main()