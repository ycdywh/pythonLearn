#!/usr/bin/env python3
#-*- coding:utf-8 -*-

'search'

__author__ = 'HUA'

import os


# 查找指定目录下文件名包含指定字符文件的绝对路径
def checktarget(pathurl, target):
    list = [x for x in os.listdir(pathurl)]
    for filename in list:
        fileurl = os.path.join(pathurl, filename)
        if (os.path.isdir(fileurl)):  # 是目录类型
            checktarget(fileurl, target)
        else:  #是文件类型
            filelist = os.path.split(fileurl)
            if (filelist[1].find(target) >= 0):
                print(os.path.abspath(fileurl))


if __name__ == '__main__':
    pathurl = input("请输入目标路径")
    target = input("请输入目标内容")
    checktarget(pathurl, target)
