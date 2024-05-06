#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：python-spider 
@File    ：gov-jzsc.py
@Author  ：wangxw
@Date    ：2024/4/16 19:25 
@Desc    ：
"""
import requests
import execjs
from fake_useragent import UserAgent

ua = UserAgent()


def get_aes(msg):
    """调用js文件中的函数，实现AES加密"""
    with open('jzsc.js', 'r', encoding='utf-8') as f:
        js_code = f.read()
    aes = execjs.compile(js_code)
    return aes.call('get_decode', msg)


if __name__ == '__main__':
    url = 'https://jzsc.mohurd.gov.cn/APi/webApi/dataservice/query/comp/list?pg=1&pgsz=15&total=450'
    headers = {
        'user-agent': ua.random,
        'v': '231012'
    }
    resp = requests.get(
        url,
        headers=headers
    )
    print(resp.text)
    t = resp.text.strip()
    decode_data = get_aes(t)
    print(decode_data.get('data').get('list'))
