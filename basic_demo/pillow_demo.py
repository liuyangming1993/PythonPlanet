#!/usr/bin/python
# coding:utf-8

"""使用Pillow缩放图片的demo"""
__author__ = 'Liu Yangming'

from PIL import Image
from PIL import ImageFile

ImageFile.LOAD_TRUNCATED_IMAGES = True

pic_path = input("输入图片路径：")
# 打开一个jpg图像文件，注意是当前路径:
im = Image.open(pic_path)
# 获得图像尺寸:
w, h = im.size
print('Original image size: %sx%s' % (w, h))
# 缩放到25%:
im.thumbnail((w // 4, h // 4))
print('Resize image to: %sx%s' % (w // 2, h // 2))
# 把缩放后的图像用jpeg格式保存:
im.save('D:\AndroidStudioWorkspace\BlogPic\screen.png', 'png')
