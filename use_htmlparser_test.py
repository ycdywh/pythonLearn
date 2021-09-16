#!/usr/bin/env python3
#-*-coding:utf-8 -*-

from html.parser import HTMLParser
from urllib import request


class MyHTMLParser(HTMLParser):
    #初始化
    def __init__(self):
        super().__init__()
        self.__attr = ''

    #获取网页起始位置，并判断需要的内容
    def handle_starttag(self, tag, attrs):
        if ('class', 'event-title') in attrs:
            self.__attr = 'Title'
        if tag == 'time':
            self.__attr = 'Date'
        if ('class', 'say-no-more') in attrs:
            self.__attr = 'Year'
        if ('class', 'event-location') in attrs:
            self.__attr = 'Location'

    def handle_endtag(self, tag):
        self.__attr = ''

    def handle_data(self, data):
        if self.__attr == 'Title':
            print('%s : %s' % (self.__attr, data))
        if self.__attr == 'Date':
            print('%s : %s' % (self.__attr, data.strip()),
                  end='')  # Year 也属于 Date, 没必要换行
        if self.__attr == 'Year':
            data = data.strip()
            if data.isdecimal():  # Year 应当为数字，排除最后两个数据
                print(' %s' % data)
        if self.__attr == 'Location':
            print('%s: %s' % (self.__attr, data))
            print()


parser = MyHTMLParser()
URL = 'https://www.python.org/events/python-events'
with request.urlopen(URL) as f:
    data = f.read()
parser.feed(data.decode('UTF-8'))