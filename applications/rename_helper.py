#!/usr/bin/python
# coding:utf-8

"""将Excel文件的扩展名统一修改为.xls"""
__author__ = 'Liu Yangming'

import os


def get_file_path_list(path):
    files = os.listdir(path)
    for fi in files:
        fi_d = os.path.join(path, fi)
        if os.path.isdir(fi_d):
            get_file_path_list(fi_d)
        else:
            file_name = os.path.splitext(fi)[0]  # 文件名
            file_type = os.path.splitext(fi)[1]  # 文件扩展名
            file_path = os.path.join(path, fi)  # 原来的文件路径
            file_list.append(file_path)


def copy_file(old_type, target_type):
    if os.path.exists(new_dir):
        pass
    else:
        os.makedirs(new_dir)
    for path in file_list:
        with open(path, 'rb') as origin_file:
            if path.endswith(target_type):
                new_path = path.replace(dir_path, new_dir)
            else:
                new_path = path.replace(old_type, target_type).replace(dir_path, new_dir)
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
    print("转换完成！")


# 原始的文件夹路径
dir_path = input("请输入文件夹路径：")
# 新的文件夹路径
new_dir = dir_path.replace(dir_path.split("\\")[-1], dir_path.split("\\")[-1] + "_new")
file_list = []
# 获取文件路径
get_file_path_list(dir_path)
# 复制文件
copy_file(".xlsx", ".xls")
input()
