#!/usr/bin/python
# coding:utf-8

"""正则表达式的工具类"""

__author__ = 'Liu Yangming'

import re

# 正则表达式
re_chinese = r'[\u4e00-\u9fa5]+'
re_num = r'[1-9]+\.?[0-9]*'


# 获取s中的数字集合
def get_numbers(s):
    numbers = re.findall(re_num, s)
    return numbers


# 获取s中的第一个数字
def get_first_number(s):
    first_number = float(get_numbers(s)[0])
    return first_number
