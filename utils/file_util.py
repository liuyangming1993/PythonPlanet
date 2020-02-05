#!/usr/bin/python
# coding:utf-8

"""文件操作的工具类"""

__author__ = 'Liu Yangming'

import os


# 文件的bean
class FileBean(object):
    def __init__(self, path, name, file_type):
        self.path = path
        self.name = name
        self.file_type = file_type


file_list = []


# 是否为文件夹
def is_dir(path):
    return os.path.isdir(path)


# 获取传入路径中的所有文件列表
def get_file_list(dir_path):
    files = os.listdir(dir_path)
    for file in files:
        path = os.path.join(dir_path, file)
        # 如果是文件夹，则进行递归操作
        if os.path.isdir(path):
            get_file_list(path)
        else:
            file_name = os.path.splitext(path)[0]  # 文件名
            file_type = os.path.splitext(path)[1]  # 文件扩展名
            file_path = os.path.join(path, path)  # 原来的文件路径
            file_list.append(FileBean(file_path, file_name, file_type))


# 将文件（或文件夹）复制到新的路径
def copy_file_dir(old_dir_path, new_dir_path):
    if os.path.exists(new_dir_path):
        pass
    else:
        os.makedirs(new_dir_path)
    for bean in file_list:
        with open(bean.path, 'rb') as origin_file:
            new_path = bean.path.replace(old_dir_path, new_dir_path)
            file_name = new_path.split("\\")[-1]
            file_dir = new_path[0:len(new_path) - len(file_name)]
            if os.path.exists(file_dir):
                pass
            else:
                os.makedirs(file_dir)
            with open(new_path, 'wb') as new_file:
                # 清空文件内容
                new_file.truncate()
                new_file.write(origin_file.read())
