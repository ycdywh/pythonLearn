#!/usr/bin/env python3
#-*- coding:utf-8 -*-

__author__ = 'HUA'

from multiprocessing import Process
import os


# 子进程要执行的代码
def run_proc(name):
    print('Parent process %s.' % os.getpid())


if __name__ == '__main__':
    print('Parent process %s.' % os.getpid())
    p = Process(target=run_proc, args=('test', ))
    print('Child process will start.')
    p.start()
    p.join()
    print('Child process end.')