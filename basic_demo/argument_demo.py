#!/usr/bin/python
# coding:utf-8

"""argv使用的demo"""
__author__ = 'Liu Yangming'

from sys import argv

script, your_name, your_age = argv

print(f"Your name is {your_name}")
print(f"Your age is {your_age}")
