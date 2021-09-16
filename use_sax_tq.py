#!/usr/bin/env python3
#-*- coding:utf-8 -*-

from urllib import request
import urllib
from xml.parsers.expat import ParserCreate


class DefaultSaxHandler(object):
    def __init__(self):
        self.name = ''
        self.data = {}

    def start_element(self, name, attrs):
        self.name = name
        print('sax:start_element: %s, attrs: %s' % (name, str(attrs)))
    
    def end_element(self, name):
        print('sax:end_element: %s' %name)

    def char_element(self, text):
        self.data[self.name] = text
        print('sax:char_data: %s' %text)


def parseXml(xml_str):
    print(xml_str)
    handler = DefaultSaxHandler()
    parser =ParserCreate()
    parser.StartElementHandler = handler.start_element
    parser.EndElementHandler = handler.end_element
    parser.CharacterDataHandler = handler.char_element
    parser.Parse(xml_str)
    data = handler.data
    return {
        'city' : data['city'],
        'live' : {
            'data': data['reporttime'],
            'weather': data['weather'],
            'temperature': data['temperature']
        }
    }


#测试
CITYCODE= '110000' # 北京市城市编码
KEY = '7a60924ba2ed0ab1f9a046ad9426304c' #web服务key
URL = 'https://restapi.amap.com/v3/weather/weatherInfo?city='+CITYCODE+'&key='+KEY+'&extensions=base&output=XML'

with request.urlopen(URL) as f:
    data = f.read()

result = parseXml(data.decode('UTF-8'))
print(result)
