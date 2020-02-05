#!/usr/bin/python
# coding:utf-8

"""文件demo"""
__author__ = 'Liu Yangming'

from sys import argv
from os.path import exists

script, file_path = argv
with open(file_path, 'w') as f:
    # 清空文本内容
    f.truncate()
    f.write("文本新内容")
# 如果文件存在
if exists(file_path):
    print(open(file_path).read())
