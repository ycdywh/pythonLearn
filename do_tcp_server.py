#!/usr/bin/env python3
#-*- coding:utf-8 -*-

import socket, threading, time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#监听端口
s.bind(('127.0.0.1', 9999))
#调用listen()方法开始监听端口，传入的参数指定等待的最大链接数
s.listen(5)
print('Waiting for connection ...')


def tcplink(sock, addr):
    print('Accept new connection from %s:%s...' % addr)
    sock.send(b'Welcome!')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        sock.send(('Hello, %s!' % data.decode('utf-8')).encode('utf-8'))
    sock.close()
    print('Connection from %s:%s closed.' % addr)


#服务器程序通过一个永久循环来接受来自客户端的连接，accept()会等待并返回一个客户端的连接:
while True:
    #接受一个新链接
    sock, addr = s.accept()
    #创建新线程来处理TCP链接
    t = threading.Thread(target=tcplink, args=(sock, addr))
    t.start()
