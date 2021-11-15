#!usr/bin/env python3
#-*- coding:utf-8 -*-

__author__ = 'HUA'

from turtle import *

#设置笔刷宽度
forward(4)

#前进
forward(200)
#右转90度
right(90)

#笔刷颜色
pencolor('red')
forward(100)
right(90)

pencolor('blue')
forward(200)
right(90)

pencolor('green')
forward(100)
right(90)

#调用done()使得窗口等待被关闭，否则将立刻关闭窗口
done()