#!/usr/bin/python
# coding:utf-8

"""实战：爬星座运势"""

__author__ = 'Liu Yangming'

from bs4 import BeautifulSoup
import urllib.request
from utils import re_util
import datetime
import webbrowser
import ssl
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Connection': 'keep-alive',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Upgrade-Insecure-Requests': '1'}
# base地址
base_url = "https://www.xzw.com"
# 首页地址
index_url = base_url + "/fortune/"
# 存储详情页面地址和星座信息
child_urls = {}
# 今日、明日、本周、本月、今年、爱情
# end = ""
end = "/1.html"
# end = "/2.html"
# end = "/3.html"
# end = "/4.html"
# end = "/5.html"
# 多渠道
WECHAT = "wechat"
JIAN_SHU = "jian_shu"
TOU_TIAO = "tou_tiao"
channel = WECHAT


def get_menu():
    # ssl._create_default_https_context = ssl._create_unverified_context
    # 使用selenium爬取网页
    # chrome_options = Options()
    # chrome_options.add_argument('--headless')
    # chrome_options.add_argument('--disable-gpu')
    # browser = webdriver.Chrome(options=chrome_options)
    # browser.get(index_url)
    # content_str = browser.page_source
    req = urllib.request.Request(index_url, headers=headers)
    resp = urllib.request.urlopen(req, timeout=20)
    content_str = resp.read()
    content_str = content_str.decode('utf-8')  # 解码
    # print(content_str)
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
    star_num = int(re_util.get_first_number(str(span_zh)) / single_star_width)
    print(zh_label + "★" * star_num + "☆" * (5 - star_num))
    aq_label = "爱情运势："
    aq = soup_content.find(text=aq_label).parent
    span_aq = aq.next_sibling
    star_num = int(re_util.get_first_number(str(span_aq)) / single_star_width)
    print(aq_label + "★" * star_num + "☆" * (5 - star_num))
    syxy_label = "事业学业："
    syxy = soup_content.find(text=syxy_label).parent
    span_syxy = syxy.next_sibling
    star_num = int(re_util.get_first_number(str(span_syxy)) / single_star_width)
    print(syxy_label + "★" * star_num + "☆" * (5 - star_num))
    cf_label = "财富运势："
    cf = soup_content.find(text=cf_label).parent
    span_cf = cf.next_sibling
    star_num = int(re_util.get_first_number(str(span_cf)) / single_star_width)
    print(cf_label + "★" * star_num + "☆" * (5 - star_num))
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
    prefix = ""
    suffix = ""
    if JIAN_SHU == channel:
        prefix = "**"
        suffix = "**"
    elif WECHAT == channel:
        prefix = "</br>**"
        suffix = "**</br>"
    else:
        pass
    div = soup_content.find(name='div', attrs={'class': 'c_cont'})
    zh_label = "综合运势"
    if zh_label not in str(div):
        return
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
    # ssl._create_default_https_context = ssl._create_unverified_context
    req = urllib.request.Request(key + end, headers=headers)
    resp = urllib.request.urlopen(req, timeout=20)
    time.sleep(1)
    content_str = resp.read()
    content_str = content_str.decode('utf-8', "ignore")  # 解码
    # 使用BeautifulSoup
    soup_content = BeautifulSoup(content_str, 'html.parser')
    # 获取运势级别、指数、颜色和速配星座（内容简介）
    get_simple_info(soup_content)
    # 获取其他描述
    get_description(soup_content)


# 打开浏览器
def open_chrome():
    # chrome_path = r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
    chrome_path = r'C:\Users\Administrator\AppData\Local\Google\Chrome\Application\chrome.exe'
    webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
    # 这里的'chrome'可以用其它任意名字，如chrome111，这里将想打开的浏览器保存到'chrome'
    # 头条
    # webbrowser.get('chrome').open("https://mp.toutiao.com/profile_v3/index", new=0,
    #                               autoraise=True)
    if JIAN_SHU == channel:
        # 简书
        webbrowser.get('chrome').open("https://www.jianshu.com/writer#/notebooks/42686948/notes/60255342", new=0,
                                      autoraise=True)
    elif WECHAT == channel:
        # 公众号
        webbrowser.get('chrome').open("https://mp.weixin.qq.com/cgi-bin/home?t=home/index&token=1475258708&lang=zh_CN",
                                      new=0, autoraise=True)
        webbrowser.get('chrome').open("http://blog.didispace.com/tools/online-markdown/", new=0, autoraise=True)
    else:
        pass


def print_date():
    # 日期
    now_date = (datetime.datetime.now()+datetime.timedelta(days=+1)).strftime('%m-%d')
    now = str.split(now_date, "-")
    month = int(now[0])
    day = int(now[1])
    now_str = str(month) + "月" + str(day) + "日"
    print("星座运势（" + now_str + "）")
    print("您要的" + now_str + "的星座运势解读！请注意查收！")


if __name__ == '__main__':
    open_chrome()
    if JIAN_SHU == channel:
        print("###点击 [阅读原文](00) 并关注公众号，每晚8点准时获取星座运势哦~")
        print(
            "![](https://upload-images.jianshu.io/upload_images/21255456-c177b29de2637a7d?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)")
    else:
        print("###每晚8点，准时获取星座运势，一定要关注我哦~")
        print(
            "![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/DnuRxKrYr5dkYfXVJLUONibqyDCgtt7utepmHHqbebSOafgkrsHQKLt4e5zJDiatXUxagdmS49KbeNKWos8eKbwA/0?wx_fmt=jpeg)")
    get_menu()
    for child_url in child_urls:
        get_info(child_url)
        print("\n")
    print_date()
