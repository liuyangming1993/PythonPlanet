#!/usr/bin/python
# coding:utf-8

"""实战：爬小说"""

__author__ = 'Liu Yangming'

from bs4 import BeautifulSoup
import urllib.request
from urllib import error
import os

# 小说页面地址
novel_url = "http://www.biqukan.com/1_1496/"
# 根地址，用于拼接
base_url = "http://www.biqukan.com"
# 下载小说的存放路径
save_dir = "Novel/"


# 保存小说到本地
def save_chapter(txt, path):
    if os.path.isdir(save_dir):
        pass
    else:
        os.makedirs(save_dir)
    try:
        with open(path, "a+", encoding='utf-8') as f:
            # 删除字符前后的所有空格
            f.write(txt.get_text(strip=True))
    except (error.HTTPError, OSError) as reason:
        print(str(reason))
    else:
        print("下载完成：" + path)


# 获得所有章节的url
def get_chapter_url():
    chapter_req = urllib.request.Request(novel_url)
    chapter_resp = urllib.request.urlopen(chapter_req, timeout=20)
    chapter_content = chapter_resp.read()
    chapter_soup = BeautifulSoup(chapter_content, 'html.parser')
    # 取出章节部分
    list_main = chapter_soup.find_all(attrs={'class': 'listmain'})
    # 存放小说所有的a标签
    a_list = []
    # 过滤掉不是a标签的数据
    for i in list_main:
        if 'a' not in str(i):
            continue
        for d in i.findAll('a'):
            a_list.append(d)
    # 过滤掉前面"最新章节列表"部分
    result_list = a_list[12:14]
    return result_list


# 获取章节内容并下载
def get_chapter_content(c):
    # 获取url
    chapter_url = base_url + c.attrs.get('href')
    # 获取章节名称
    chapter_name = c.string
    chapter_req = urllib.request.Request(chapter_url)
    chapter_resp = urllib.request.urlopen(chapter_req, timeout=20)
    chapter_content = chapter_resp.read()
    chapter_soup = BeautifulSoup(chapter_content, 'html.parser')
    # 查找章节部分内容
    show_txt = chapter_soup.find_all(attrs={'class': 'showtxt'})
    for txt in show_txt:
        save_chapter(txt, save_dir + chapter_name + ".txt")


if __name__ == '__main__':
    novel_list = get_chapter_url()
    for chapter in novel_list:
        get_chapter_content(chapter)
