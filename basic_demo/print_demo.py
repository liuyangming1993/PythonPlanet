#!/usr/bin/python
# coding:utf-8

"""输出和输入的demo"""
__author__ = 'Liu Yangming'

print("Hello world")
my_age = 18
print(f"I'm {my_age} years old.")
my_name = "Will"
print("My name is {}.".format(my_name))
formatter = "{} {} {} {}"
print(formatter.format("1", "2", "3", "4"))
# 为了结尾不换行
print("How are you?", end=' ')
your_answer = input()
