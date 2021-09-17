#!/usr/bin/env python3
#-*- coding:utf-8 -*-

import chardet

data = '离离原上草，一岁一枯荣'.encode('GBK')
print(chardet.detect(data))

data = '真実はいつもひとつ'.encode('euc-jp')
print(chardet.detect(data))