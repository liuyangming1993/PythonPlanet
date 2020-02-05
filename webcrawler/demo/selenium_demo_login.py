#!/usr/bin/python
# coding:utf-8

"""使用selenium登录CSDN"""

__author__ = 'Liu Yangming'

import pickle

from selenium import webdriver

login_url = ""
csdn_url = ""


# 自动登录保存Cookie
def auto_login():
    browser = webdriver.Chrome()
    browser.delete_all_cookies()
    browser.get(login_url)
    browser.find_element_by_id("username").send_keys(u"lkasdjflajsdfl")
    browser.find_element_by_id("password").send_keys(u"lkasdjflajsdfl")
    login_btn = browser.find_element_by_class_name('logging').click()
    # 获得当前的url，可以利用这个和登录连接作对比，不同则说明登录成功
    print(browser.current_url)
    # 利用pickle序列化保存下来
    pickle.dump(browser.get_cookies(), open('cookies.pkl', 'wb'))
    browser.quit()


def cookie_browse():
    browser = webdriver.Chrome()
    browser.get(csdn_url)
    browser.delete_all_cookies()
    cookies = pickle.load(open("cookies.pkl", "rb"))
    for cookie in cookies:
        browser.add_cookie({
            "domain": ".csdn.net",
            'name': cookie.get('name'),
            'value': cookie.get('value'),
            'expiry': cookie.get('expiry'),
            'path': '/',
            'httpOnly': False,
            'hostOnly': False,
            'Secure': False
        })
    browser.get(csdn_url)
