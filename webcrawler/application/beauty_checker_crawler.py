#!/usr/bin/python
# coding:utf-8

"""实战：爬图片地址"""

__author__ = 'Liu Yangming'

from bs4 import BeautifulSoup
import urllib.request
import gzip

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Cookie': 'pjr5_2132_saltkey=Br1jq1jq; pjr5_2132_lastvisit=1583924239; pjr5_2132_sid=mgOEHO; pjr5_2132_sendmail=1; Hm_lvt_6a60b923391636750bd84d6047523609=1583927842; pjr5_2132_lastact=1583927920%09plugin.php%09; Hm_lpvt_6a60b923391636750bd84d6047523609=1583927922',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
}
index_url = "https://www.lesmao.co/"


def get_category_list():
    req = urllib.request.Request(index_url, headers=headers)
    resp = urllib.request.urlopen(req, timeout=20)
    # gzip解压缩
    content = gzip.decompress(resp.read())
    content_str = content.decode('utf-8')  # 解码
    soup_content = BeautifulSoup(content_str, 'html.parser')
    print(content_str)
    pass


if __name__ == "__main__":
    get_category_list()
    pass
