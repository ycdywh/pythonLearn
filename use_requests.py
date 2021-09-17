#!/usr/bin/env python3
#-*- coding:utf-8 -*-

import requests

#GET访问界面
#需要传入HTTP Header时，我们传入一个dict作为headers参数：
headers = {
    'User-Agent':
    'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit'
}
r = requests.get('https://www.douban.com', headers=headers)
print(r.status_code)
print(r.text)
#自动检测编码
print(r.encoding)
#通过content获取bytes对象
print(r.content)
#可以直接获取json返回值
CITYCODE = '110000'  # 北京市城市编码
KEY = '7a60924ba2ed0ab1f9a046ad9426304c'  #web服务key
URL = 'https://restapi.amap.com/v3/weather/weatherInfo?city=' + CITYCODE + '&key=' + KEY + '&extensions=base&output=JSON'
r = requests.get(URL)
print(r.json())
"""
要发送POST请求，只需要把get()方法变成post()，然后传入data参数作为POST请求的数据：
>>> r = requests.post('https://accounts.douban.com/login', data={'form_email': 'abc@example.com', 'form_password': '123456'})


requests默认使用application/x-www-form-urlencoded对POST数据编码。如果要传递JSON数据，可以直接传入json参数：
params = {'key': 'value'}
r = requests.post(url, json=params) # 内部自动序列化为JSON


类似的，上传文件需要更复杂的编码格式，但是requests把它简化成files参数：
>>> upload_files = {'file': open('report.xls', 'rb')}
>>> r = requests.post(url, files=upload_files)
在读取文件时，注意务必使用'rb'即二进制模式读取，这样获取的bytes长度才是文件的长度。


除了能轻松获取响应内容外，requests对获取HTTP响应的其他信息也非常简单。例如，获取响应头：
>>> r.headers
{Content-Type': 'text/html; charset=utf-8', 'Transfer-Encoding': 'chunked', 'Content-Encoding': 'gzip', ...}
>>> r.headers['Content-Type']
'text/html; charset=utf-8'


requests对Cookie做了特殊处理，使得我们不必解析Cookie就可以轻松获取指定的Cookie：
>>> r.cookies['ts']
'example_cookie_12345'

要在请求中传入Cookie，只需准备一个dict传入cookies参数：
>>> cs = {'token': '12345', 'status': 'working'}
>>> r = requests.get(url, cookies=cs)


最后，要指定超时，传入以秒为单位的timeout参数：
>>> r = requests.get(url, timeout=2.5) # 2.5秒后超时
"""

