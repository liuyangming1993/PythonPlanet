#!/usr/bin/python
# coding:utf-8

"""使用itchat操作微信的demo"""
__author__ = 'Liu Yangming'

import itchat


def my_friends():
    itchat.auto_login()
    friends = itchat.get_friends(update=True)
    return friends


if __name__ == "__main__":
    friends = my_friends()
    for f in friends:
        print(str(f['NickName']))
