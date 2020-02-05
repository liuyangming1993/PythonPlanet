#!/usr/bin/python
# coding:utf-8

"""实战：爬小说"""

__author__ = 'Liu Yangming'

from bs4 import BeautifulSoup
import urllib.request
import os
from os.path import exists
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# 小说页面地址
novel_url = "https://www.biqukan.com/3_3037/"
# 根地址，用于拼接
base_url = "http://www.biqukan.com"
# 下载小说的存放路径
save_dir = "Novel/"
# 文件地址
file_path = save_dir + "sectionCache.txt"
# 想看的章节
section_num = 17
# 每行的字数
line_char_size = 40 * 2
# 显示章节数量
sections = 3
# 过滤掉的章节，因为有一些无用章节，并非正文，需要过滤，所以我们在阅读过程中，需要手动更改开始章节
filterSection = 12 + 28

# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
#     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
#     'Connection': 'keep-alive',
#     'Accept-Language': 'zh-CN,zh;q=0.9',
#     'Cache-Control': 'max-age=0',
#     'If-Modified-Since': 'Thu, 20 Dec 2018 21:13:59 GMT',
#     'If-None-Match': '1545340439',
#     'Referer': 'https://www.biqukan.com/3_3012/',
#     'Upgrade-Insecure-Requests': '1'}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Connection': 'keep-alive',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Upgrade-Insecure-Requests': '1'}


# 展示小说
def print_chapter(txt):
    novel_content = txt.get_text(strip=True)
    line_num = int(len(novel_content) / line_char_size) + 1
    for i in range(line_num):
        if i == 0:
            print(novel_content[0:line_char_size])
        else:
            print(novel_content[i * line_char_size:(i + 1) * line_char_size])


# 获得所有章节的url
def get_chapter_url():
    chapter_req = urllib.request.Request(novel_url, headers=headers)
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
    result_list = a_list[filterSection + section_num + 1:filterSection + section_num + 6]
    return result_list


# 获取章节内容并下载
def get_chapter_content(c):
    # 获取url
    chapter_url = base_url + c.attrs.get('href')
    # 获取章节名称
    chapter_name = c.string
    print(chapter_name)
    # 使用selenium爬取网页
    # chrome_options = Options()
    # chrome_options.add_argument('--headless')
    # chrome_options.add_argument('--disable-gpu')
    # browser = webdriver.Chrome(options=chrome_options)
    # browser.get(chapter_url)
    # chapter_content = browser.page_source
    # 使用urllib爬取网页
    chapter_req = urllib.request.Request(chapter_url)
    chapter_resp = urllib.request.urlopen(chapter_req, timeout=20)
    chapter_content = chapter_resp.read()
    chapter_soup = BeautifulSoup(chapter_content, 'html.parser')
    # 查找章节部分内容
    show_txt = chapter_soup.find_all(attrs={'class': 'showtxt'})
    for txt in show_txt:
        print_chapter(txt)


def change_section_num():
    if os.path.isdir(save_dir):
        pass
    else:
        os.makedirs(save_dir)
    with open(file_path, "w", encoding='utf-8') as f:
        f.truncate()
        f.write(str(section_num + sections))


def get_section_num():
    if exists(file_path):
        with open(file_path, "r", encoding='utf-8') as f:
            return int(f.read())


if __name__ == '__main__':
    section_num = get_section_num()
    novel_list = get_chapter_url()
    for chapter in novel_list:
        print(chapter)
    read_list = novel_list[0:sections]
    for chapter in read_list:
        get_chapter_content(chapter)
    change_section_num()
