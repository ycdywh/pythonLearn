#!/usr/bin/env python3
#-*- coding:utf-8 -*-

'os'

__author__ = 'HUA'

from genericpath import isdir
import os

#操作系统类型
#如果是posix，说明系统是Linux、Unix或Mac OS X，如果是nt，就是Windows系统
#详细的系统信息os.uname() 不支持windows
f = os.name
print(f)

#获取环境变量
f = os.environ.get('PATH')
print(f)

#查看当前目录的绝对路径
f = os.path.abspath('.')
print(f)

#在某个目录下创建一个新目录，首先把新目录的完整路径表示出来:
f = os.path.join('E:\\pythonTest', 'testdir')
print(f)
#然后创建一个目录 os.mkdir('/Users/michael/testdir')
os.mkdir(f)
#删掉一个目录
os.rmdir(f)

#拆分路径
f = os.path.split('E:\\pythonTest\\test.txt')
print(f[0] + '-----' + f[1])
#获取拓展名
f = os.path.splitext('E:\\pythonTest\\test.txt')
print(f[0] + '-----' + f[1])

#对文件重命名
#os.rename('test.txt','test1.py')
#删掉文件
#os.remove('test1.py')

#列出当前目录下所有目录
f = [x for x in os.listdir('.') if os.path.isdir(x)]
print(f)

#列出所有py文件
f = [
    x for x in os.listdir('.')
    if os.path.isfile(x) and os.path.splitext(x)[1] == '.py'
]
print(f)