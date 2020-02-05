#!/usr/bin/python
# coding:utf-8

"""socket客户端的demo"""
__author__ = 'Liu Yangming'

import socket
import threading

charset = "utf-8"
is_open = True

# 创建socket，鞋也是IPv4，TCP协议
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 声明域名和端口
ip_port = ('127.0.0.1', 9999)
# 建立连接
s.connect(ip_port)


def recv_msg():
    while True:
        # 接收消息
        recv_msg = s.recv(1024)
        print(recv_msg.decode(charset))


# 启动一个线程来接收消息
t2 = threading.Thread(target=recv_msg)
t2.start()
while True:
    msg = input()
    # 发送消息
    s.send(msg.encode(charset))
    if msg == 'exit':
        s.close()
        break
print("断开连接")
