#!/usr/bin/python
# coding:utf-8

"""使用selenium"""

__author__ = 'Liu Yangming'

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# 可以使用Options设置是否显示地打开浏览器
# chrome_options = Options()
# chrome_options.add_argument('--headless')
# chrome_options.add_argument('--disable-gpu')
# browser = webdriver.Chrome(options=chrome_options)
# 基本代码
browser = webdriver.Chrome()  # 调用本地的Chrome浏览器
browser.get('http://www.baidu.com')  # 请求页面，会打开一个浏览器窗口
html_text = browser.page_source  # 获得页面代码
browser.quit()  # 关闭浏览器
print(html_text)
