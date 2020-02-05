#!/usr/bin/python
# coding:utf-8

"""模仿post请求"""

__author__ = 'Liu Yangming'

import urllib.request
from datetime import datetime
import json

# 通用header
header = {
    "Content-Type": "application/json"
}
# 服务地址
base_url = ""


# 请求网络并打印数据
def request_net(url, values):
    data = json.dumps(values, sort_keys=True, indent=2, ensure_ascii=False)
    print("请求参数：")
    print(data)
    data = bytes(data, 'utf-8')
    req = urllib.request.Request(url, data, headers=header)
    resp = urllib.request.urlopen(req)
    # Byte结果转Json
    result_json = json.loads(resp.read())
    # 输出格式化后的json
    print("返回参数：")
    print(json.dumps(result_json, sort_keys=True, indent=2, ensure_ascii=False))
    return result_json


# 登陆url
url_login = base_url + "/login"
values = {
    "timestamp": datetime.now().timestamp(),
    "request": {
        "username": "admin",
        "password": "1",
        "clientKey": "asdf"
    }
}
result = request_net(url_login, values)

# 请求的url
url_getList = base_url + "/getList"
token = result['response']['content']['token']
values = {
    "timestamp": datetime.now().timestamp(),
    "service": "",
    "token": token,
    "request": {
        "search": None
    }
}
request_net(url_getList, values)
