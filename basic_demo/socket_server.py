#!/usr/bin/python
# coding:utf-8

"""socket服务端的demo"""
__author__ = 'Liu Yangming'

import socket
import threading

charset = 'utf-8'
# 创建socket，鞋也是IPv4，TCP协议
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 声明域名和端口
ip_port = ('127.0.0.1', 9999)
# 监听端口
s.bind(ip_port)
# 开始监听端口，指定等待连接的最大数量
s.listen(5)
print('Waiting for connection...')


def get_byte(s):
    print(f'接收到的信息：{s}')
    return str.encode(charset)


def tcp_link(sock, addr):
    print('Accept new connection from %s:%s...' % addr)
    sock.send('已成功连接至服务端'.encode(charset))
    while True:
        data = sock.recv(1024)
        print(data.decode(charset))
        # 服务器发送给客户端
        new_msg = input()
        sock.send(new_msg.encode(charset))
        if not data or data.decode(charset) == 'exit':
            break
    sock.close()
    print('Connection from %s:%s closed.' % addr)


while True:
    # 接受一个新的连接
    sock, addr = s.accept()
    # 创建新线程来处理TCP连接
    t = threading.Thread(target=tcp_link, args=(sock, addr))
    t.start()
