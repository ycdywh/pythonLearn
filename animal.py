#!/usr/bin/env python3
#-*- coding:utf-8 -*-

'继承、多态'

__author__ = 'HUA'


class Animal(object):
    def run(self):
        print('animal is running!')


class Dog(Animal):
    pass


class Cat(Animal):
    def run(self):
        print('cat is running!')


class Pig(object):
    def run(self):
        print('pig is running!')


class Stone(object):
    pass


def run_twice(Animal):
    Animal.run()
    Animal.run()


run_twice(Dog())
run_twice(Cat())
run_twice(Pig())
run_twice(Stone())
