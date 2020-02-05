#!/usr/bin/python
# coding:utf-8

"""批量缩放图片"""
__author__ = 'Liu Yangming'

import utils.file_util
from PIL import Image
from PIL import ImageFile

ImageFile.LOAD_TRUNCATED_IMAGES = True

# 缩放比例
scaling_ratio = float(input("请输入缩放系数（例如缩小为原图的四分之一，则输入0.4）："))
# 原始的文件夹路径
dir_path = input("请输入文件或文件夹路径：")
if utils.file_util.is_dir(dir_path):  # 如果是文件夹
    # 新的文件夹路径
    new_dir = dir_path.replace(dir_path.split("\\")[-1], dir_path.split("\\")[-1] + "_new")
    # 获取文件列表
    utils.file_util.get_file_list(dir_path)
    # 将文件复制到新的文件夹
    utils.file_util.copy_file_dir(dir_path, new_dir)

    # 清空文件工具模块的文件列表
    utils.file_util.file_list.clear()
    # 获取新的文件列表
    utils.file_util.get_file_list(new_dir)
    # 循环打开所有文件
    for file_bean in utils.file_util.file_list:
        im = Image.open(file_bean.path)
        # 获得图像尺寸:
        w, h = im.size
        # 缩放:
        im.thumbnail((w // (scaling_ratio * 10), h // (scaling_ratio * 10)))
        # 把缩放后的图像用原格式保存:
        # im.save(file_bean.path, file_bean.file_type.replace(".", ""))
        im.save(file_bean.path, "JPEG")
else:  # 如果是个文件
    # 打开一个图像文件
    im = Image.open(dir_path)
    # 获得图像尺寸:
    w, h = im.size
    # 缩放:
    im.thumbnail((w // (scaling_ratio * 10), h // (scaling_ratio * 10)))
    # 把缩放后的图像用原格式保存:
    file_type = dir_path.split(".")[-1]
    file_path = dir_path.replace(dir_path.split("\\")[-1], "")
    new_file_name = dir_path.split("\\")[-1].replace("." + file_type, "") + "_new." + file_type
    print(file_type, new_file_name)
    print(file_path)
    im.save(file_path + new_file_name, file_type)
print("缩放完成！")
