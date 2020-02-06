#!/usr/bin/python
# coding:utf-8

"""实战：爬星座运势"""
from selenium.webdriver import ActionChains

__author__ = 'Liu Yangming'

from bs4 import BeautifulSoup
import urllib.request
from utils import re_util
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import datetime
import webbrowser

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Connection': 'keep-alive',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Upgrade-Insecure-Requests': '1'}
# base地址
base_url = "https://www.xzw.com"
# 首页地址
index_url = base_url + "/fortune/"
# 日期
now_date = datetime.datetime.now().strftime('%m-%d')
now_str = str.replace(str.replace(now_date, "-", "月") + "日", "0", "")
# 存储详情页面地址和星座信息
child_urls = {}


def get_menu():
    req = urllib.request.Request(index_url, headers=headers)
    resp = urllib.request.urlopen(req, timeout=20)
    content_str = resp.read()
    content_str = content_str.decode('utf-8')  # 解码
    soup_content = BeautifulSoup(content_str, 'html.parser')
    div = soup_content.find(name='div', attrs={'class': 'alb'})
    for child in div.children:
        key = base_url + child.dl.dt.a['href']
        value = child.dl.dd.strong.text + "（" + child.dl.dd.small.text + "）"
        child_urls[key] = value


# 通过网页代码获取星座名称
def get_name_xz(key):
    print("## " + child_urls[key])


# 获得内容简介
def get_simple_info(soup_content):
    single_star_width = 48 / 3
    zh_label = "综合运势："
    zh = soup_content.find(text=zh_label).parent
    span_zh = zh.next_sibling
    print(zh_label + "★" * int(re_util.get_first_number(str(span_zh)) / single_star_width))
    aq_label = "爱情运势："
    aq = soup_content.find(text=aq_label).parent
    span_aq = aq.next_sibling
    print(aq_label + "★" * int(re_util.get_first_number(str(span_aq)) / single_star_width))
    syxy_label = "事业学业："
    syxy = soup_content.find(text=syxy_label).parent
    span_syxy = syxy.next_sibling
    print(syxy_label + "★" * int(re_util.get_first_number(str(span_syxy)) / single_star_width))
    cf_label = "财富运势："
    cf = soup_content.find(text=cf_label).parent
    span_cf = cf.next_sibling
    print(cf_label + "★" * int(re_util.get_first_number(str(span_cf)) / single_star_width))
    jkzs_label = "健康指数："
    jkzs_value = soup_content.find(text=jkzs_label).parent.parent.text
    print(jkzs_value)
    stzs_label = "商谈指数："
    stzs_value = soup_content.find(text=stzs_label).parent.parent.text
    print(stzs_value)
    xyys_label = "幸运颜色："
    xyys_value = soup_content.find(text=xyys_label).parent.parent.text
    print(xyys_value)
    xysz_label = "幸运数字："
    xysz_value = soup_content.find(text=xysz_label).parent.parent.text
    print(xysz_value)
    spxz_label = "速配星座："
    spxz_value = soup_content.find(text=spxz_label).parent.parent.text
    print(spxz_value)
    dp_label = "短评："
    dp_value = soup_content.find(text=dp_label).parent.parent.text
    print(dp_value)


# 获得内容简介
def get_description(soup_content):
    prefix = "</br>**"
    suffix = "**</br>"
    div = soup_content.find(name='div', attrs={'class': 'c_cont'})
    zh_label = "综合运势"
    span = div.find(text=zh_label).parent.next_sibling
    child_list = []
    for child in span.children:
        child_list.append(child)
    zh_value = child_list[:1][0]
    print(prefix + zh_label + suffix)
    print(zh_value)
    aq_label = "爱情运势"
    aq_value = div.find(text=aq_label).parent.next_sibling.text
    print(prefix + aq_label + suffix)
    print(aq_value)
    syxy_label = "事业学业"
    syxy_value = div.find(text=syxy_label).parent.next_sibling.text
    print(prefix + syxy_label + suffix)
    print(syxy_value)
    cf_label = "财富运势"
    cf_value = div.find(text=cf_label).parent.next_sibling.text
    print(prefix + cf_label + suffix)
    print(cf_value)
    jk_label = "健康运势"
    jk_value = div.find(text=jk_label).parent.next_sibling.text
    print(prefix + jk_label + suffix)
    print(jk_value)


# 获取星座详情
def get_info(key):
    # 获取星座名和日期
    get_name_xz(key)
    req = urllib.request.Request(key, headers=headers)
    resp = urllib.request.urlopen(req, timeout=20)
    content_str = resp.read()
    content_str = content_str.decode('utf-8')  # 解码
    # 使用BeautifulSoup
    soup_content = BeautifulSoup(content_str, 'html.parser')
    # 获取运势级别、指数、颜色和速配星座（内容简介）
    get_simple_info(soup_content)
    # 获取其他描述
    get_description(soup_content)


# 打开浏览器
def open_chrome():
    chrome_path = r'C:\Users\Administrator\AppData\Local\Google\Chrome\Application\chrome.exe'
    webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
    # 这里的'chrome'可以用其它任意名字，如chrome111，这里将想打开的浏览器保存到'chrome'
    webbrowser.get('chrome').open("http://blog.didispace.com/tools/online-markdown/", new=0, autoraise=True)
    webbrowser.get('chrome').open("https://mp.weixin.qq.com/cgi-bin/filepage?type=2&begin=0&count=12&token=1475258708&lang=zh_CN", new=0, autoraise=True)


if __name__ == '__main__':
    open_chrome()
    print(now_str)
    print(
        "![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/DnuRxKrYr5dkYfXVJLUONibqyDCgtt7utepmHHqbebSOafgkrsHQKLt4e5zJDiatXUxagdmS49KbeNKWos8eKbwA/0?wx_fmt=jpeg)")
    get_menu()
    for child_url in child_urls:
        get_info(child_url)
        print("\n")
