#!/usr/bin/python
# coding:utf-8

"""实战：爬代理列表"""

__author__ = 'Liu Yangming'

from bs4 import BeautifulSoup
import urllib.request
from urllib import error
import gzip

test_url = "https://www.baidu.com/"  # 测试ip是否可用
proxy_url_base = "https://www.kuaidaili.com/free/inha/"  # ip抓取源
ip_file = "availableIP.txt"
ip_list = []


# ip写入到文件中
def write_file(list):
    try:
        with open(ip_file, 'w') as f:
            for ip in list:
                f.write(ip + "\n")
    except OSError as e:
        print(str(e))


# 检测代理IP是否可以用，返回可用的代理IP列表
def test_ip(test_list):
    ip_list = []
    for ip in test_list:
        proxy = {'http': ip}
        try:
            handler = urllib.request.ProxyHandler(proxy)
            opener = urllib.request.build_opener(handler)
            urllib.request.install_opener(opener)
            test_resp = urllib.request.urlopen(test_url)
            if test_resp.getcode() == 200:
                ip_list.append(ip)
        except error.HTTPError as e:
            print(str(e))
    return ip_list


# 抓取快代理IP
def catch_ip(page):
    try:
        # 设置请求头，不然503
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Cookie': 'channelid=0; _ga=GA1.2.1978538623.1541388379; _gid=GA1.2.1552472901.1541388379; Hm_lvt_7ed65b1cc4b810e9fd37959c9bb51b31=1541388380; sid=1541386870009430; Hm_lpvt_7ed65b1cc4b810e9fd37959c9bb51b31=1541388516',
            'Host': 'www.kuaidaili.com',
            'Referer': 'https://www.kuaidaili.com/free/inha/2/',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
        }
        proxy_url = proxy_url_base + str(page) + "/"
        req = urllib.request.Request(proxy_url, headers=headers)
        resp = urllib.request.urlopen(req, timeout=20)
        content = gzip.decompress(resp.read()).decode("utf-8")
        soup = BeautifulSoup(content, 'html.parser')
        catch_list = soup.find_all('tbody')
        for i in catch_list:
            trs = i.find_all('tr')
            for tr in trs:
                td = tr.find_all('td')
                ip_list.append(td[0].get_text() + ":" + td[1].get_text())
    except error.URLError as e:
        print(str(e))


if __name__ == "__main__":
    for i in range(1, 2):
        catch_ip(i)
    available_ip_list = test_ip(ip_list)
    write_file(available_ip_list)
