#!/usr/bin/env python3
#-*- coding:utf-8 -*-

from urllib import request
import json

def fetch_data(url):
    with request.urlopen(url) as f:
        a = f.read()
        b = a.decode('utf-8')
    return json.loads(b)

URL = "http://www.httpbin.org/get"
data = fetch_data(URL)
print(data)
assert data['query']['results']['channel']['location']['city'] == 'Beijing'
print('ok')
    