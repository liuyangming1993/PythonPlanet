#!/usr/bin/python
# coding:utf-8

"""实战：爬图片地址"""

__author__ = 'Liu Yangming'

from bs4 import BeautifulSoup
import urllib.request
import gzip
import json

from webcrawler.application.beaty_checker.beauty_bean import Response, Content, Category
from webcrawler.application.beaty_checker.category_bean import CategoryBean

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    # 'Cookie': 'pjr5_2132_saltkey=Br1jq1jq; pjr5_2132_lastvisit=1583924239; pjr5_2132_sid=mgOEHO; pjr5_2132_sendmail=1; Hm_lvt_6a60b923391636750bd84d6047523609=1583927842; pjr5_2132_lastact=1583927920%09plugin.php%09; Hm_lpvt_6a60b923391636750bd84d6047523609=1583927922',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
}
index_url = "https://www.lesmao.co/"
base_url = "https://www.lesmao.co/"
json_file = "data.json"
# 存储分类页面地址和分类信息
category_list = []
beauty_list = []


# 根据url获取相应的soup_content
def get_soup_content(url):
    # 添加代理
    # proxy = {'http': '113.194.31.123:9999'}
    # handler = urllib.request.ProxyHandler(proxy)
    # opener = urllib.request.build_opener(handler)
    # urllib.request.install_opener(opener)
    # 添加代理end
    req = urllib.request.Request(url, headers=headers)
    resp = urllib.request.urlopen(req, timeout=100)
    # gzip解压缩
    content = gzip.decompress(resp.read())
    content_str = content.decode('utf-8')  # 解码
    soup_content = BeautifulSoup(content_str, 'html.parser')
    return soup_content


# 获取分类列表
def get_category_list():
    soup_content = get_soup_content(index_url)
    # 这里有两个分类被单独放在外面了，所以需要单独处理
    li39 = soup_content.find('li', {'id': 'mn_F39'})
    category_list.append(
        CategoryBean(li39.a.text, [CategoryBean(base_url + li39.a['href'], [])]))
    # li45 = soup_content.find('li', {'id': 'mn_F45'})
    # category_list.append(
    #     CategoryBean(li45.a.text, [CategoryBean(base_url + li45.a['href'], [])]))
    # ul_list = soup_content.findAll('ul', {'class': 'cl'})
    # for ul in ul_list:
    #     for li in ul.children:
    #         category_list.append(
    #             CategoryBean(li.a.text, [CategoryBean(base_url + li.a['href'], [])]))


# 获取该分类下的所有子页面地址
def get_category_list_child_pages():
    for category_bean in category_list:
        first_page = category_bean.c_child_list[0].c_name
        str_split = str.split(first_page, '-')
        # 获取页码之前的url，用于后面的拼装
        common_url = str.replace(first_page, str_split[-1], "")
        soup_content = get_soup_content(first_page)
        div_pg = soup_content.find('div', {'class': 'pg'})
        if div_pg is None:
            continue
        for child in div_pg.children:
            if 'class' in str(child):
                if 'last' in str(child):
                    # 可以根据页码获取所有地址，所以清除之前已经保存的地址
                    category_bean.c_child_list.clear()
                    # 获取页码数
                    page_count = int(str.replace(child.text, '...', ''))
                    for i in range(1, page_count + 1):
                        category_bean.c_child_list.append(CategoryBean(common_url + str(i) + '.html', []))
                    break
                continue
            category_bean.c_child_list.append(CategoryBean(base_url + child['href'], []))


# 获取专辑列表
def get_album_list():
    for category in category_list:
        for child_page in category.c_child_list:
            child_page_url = child_page.c_name
            soup_content = get_soup_content(child_page_url)
            div_group = soup_content.findAll('div', {'class': 'group'})
            for div in div_group:
                child_page.c_child_list.append(
                    CategoryBean({'album_name': div.a.img['alt'], 'thumbnail': div.a.img['src'],
                                  'first_page': str(base_url + div.a['href'])}, []))


# 获取专辑的所有子页面（包含首页）
def get_album_list_child_pages():
    for category in category_list:
        for child_page in category.c_child_list:
            for album_child_page in child_page.c_child_list:
                first_page = album_child_page.c_name['first_page']
                soup_content = get_soup_content(first_page)
                # 专辑首页放入到列表中
                album_child_page.c_child_list.append(CategoryBean(first_page, []))
                div_pg = soup_content.find('div', {'class': 'pg'})
                if div_pg is None:
                    continue
                for child in div_pg.children:
                    if 'class' in str(child):
                        continue
                    album_child_page.c_child_list.append(CategoryBean(base_url + child['href'], []))


def get_img_list():
    for category in category_list:
        for child_page in category.c_child_list:
            for album_child_page in child_page.c_child_list:
                for img in album_child_page.c_child_list:
                    soup_content = get_soup_content(img.c_name)
                    li_list = soup_content.findAll('li')
                    for li in li_list:
                        if 'img' in str(li):
                            img.c_child_list.append(li.img['src'])


def print_log():
    for category in category_list:
        # 分类
        print(category.c_name + "----------------------------------类别")
        for child_page in category.c_child_list:
            # 分类下的所有子页面
            print(child_page.c_name + "----------------------------------类别下的子页面")
            for album_child_page in child_page.c_child_list:
                print(album_child_page.c_name['album_name'] + album_child_page.c_name['thumbnail'])
                # 子页面中的专辑首页
                print(album_child_page.c_name['first_page'] + "----------------------------------子页面上的专辑首页")
                for img in album_child_page.c_child_list:
                    print(img.c_name + "----------------------------------专辑的子页面")
                    for img_src in img.c_child_list:
                        print(img_src + "----------------------------------专辑的子页面上的图片")


def output_file(s):
    with open(json_file, 'w') as f:
        # 清空文本内容
        f.truncate()
        f.write(s)


def build_response():
    response = {'code': 0, 'content': []}
    for category in category_list:
        # 分类
        category_bean = {}
        response['content'].append(category_bean)
        category_bean['name'] = category.c_name
        category_bean['albumList'] = []
        for child_page in category.c_child_list:
            # print(child_page.c_name + "----------------------------------类别下的子页面")
            for album_child_page in child_page.c_child_list:
                # 专辑
                album_bean = {}
                category_bean['albumList'].append(album_bean)
                album_bean['albumName'] = album_child_page.c_name['album_name']
                album_bean['thumbnail'] = album_child_page.c_name['thumbnail']
                album_bean['imgList'] = []
                # 子页面中的专辑首页
                # print(album_child_page.c_name + "----------------------------------子页面上的专辑首页")
                for img in album_child_page.c_child_list:
                    # print(img.c_name + "----------------------------------专辑的子页面")
                    for img_src in img.c_child_list:
                        album_bean['imgList'].append(img_src)
                        # print(img_src + "----------------------------------专辑的子页面上的图片")
    print(json.dumps(response))
    output_file(json.dumps(response))


if __name__ == "__main__":
    # get_category_list()
    # get_category_list_child_pages()
    # get_album_list()
    # get_album_list_child_pages()
    # get_img_list()
    # build_response()
    output_file("sssssss")
    # print_log()
