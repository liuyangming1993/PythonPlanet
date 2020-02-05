#!/usr/bin/python
# coding:utf-8

"""实战：爬星座运势"""

__author__ = 'Liu Yangming'

from bs4 import BeautifulSoup
import urllib.request
import re

# 首页地址
parent_url = "https://m.xzw.com/fortune/"
# 子页面地址
child_url = "https://m.xzw.com/fortune/leo"
# 正则表达式
re_chinese = r'[\u4e00-\u9fa5]+'
re_num = r'[1-9]+\.?[0-9]*'


def remove_unused_char(s):
    result = str.replace(s, "[", "")
    result = str.replace(result, ",", "")
    result = str.replace(result, "]", "")
    result = str.replace(result, "'", "")
    return result


def get_menu():
    req = urllib.request.Request(parent_url)
    resp = urllib.request.urlopen(req, timeout=20)
    content_str = resp.read()
    content_str = content_str.decode('utf-8')  # 解码
    print(content_str)


# 获得所有章节的url
def get_info(url):
    req = urllib.request.Request(url)
    resp = urllib.request.urlopen(req, timeout=20)
    content_str = resp.read()
    content_str = content_str.decode('utf-8')  # 解码
    # 使用BeautifulSoup
    soup_content = BeautifulSoup(content_str, 'html.parser')
    # 截取出相应的有用内容
    # 获取星座名
    name_xz = soup_content.find(attrs={'class': 'astro'})
    name_xz = str(name_xz.find_all(["em"])[0])
    name_xz = str.replace(name_xz, "<em>", "")
    name_xz = str.replace(name_xz, "</em>", "")
    name_xz = str.replace(name_xz, "<i>", "")
    name_xz = str.replace(name_xz, "</i>", "")
    print(name_xz)
    # 获取运势级别、指数、颜色和速配星座
    span = soup_content.find_all('span', attrs={"class": ["layer"]})
    for info in span:
        info_str = str(info)
        title = str(re.findall(re_chinese, info_str))
        title = remove_unused_char(title)
        if info_str.find("em") >= 0:
            level = int(float(re.findall(re_num, info_str)[1]) * 2)
            print(f"{title}：{level}星")
        else:
            if title.find("健康指数") >= 0:
                num = int(float(re.findall(re_num, info_str)[0]))
                print(f"{title}：{num}%")
            if title.find("商谈指数") >= 0:
                num = int(float(re.findall(re_num, info_str)[0]))
                print(f"{title}：{num}%")
            if title.find("幸运颜色") >= 0:
                color = str.replace(title, "幸运颜色", "")
                color = remove_unused_char(color)
                print(f"幸运颜色：{color}")

    # 拿到具体的文字描述
    content = soup_content.find(attrs={'class': 'cont'})
    # 存放小标题和内容
    for child in content.children:
        print(child.string)


if __name__ == '__main__':
    get_menu()
    # get_info(child_url)
