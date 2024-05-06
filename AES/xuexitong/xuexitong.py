#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：python-spider 
@File    ：xuexitong.py
@Author  ：wangxw
@Date    ：2024/4/16 17:09 
@Desc    ： 模拟登录学习通  https://passport2.chaoxing.com/fanyalogin
"""

import requests
import execjs
from fake_useragent import UserAgent

USERNAME = "15327108514"
PASSWORD = "1qaz2wsx"
ua = UserAgent()


def get_aes(msg):
    """调用js文件中的函数，实现AES加密"""
    with open('xuexitong.js', 'r',encoding='utf-8') as f:
        js_code = f.read()

    aes = execjs.compile(js_code)
    return aes.call('encryptByAES', msg)


if __name__ == '__main__':
    url = 'https://passport2.chaoxing.com/fanyalogin'
    headers = {
        'user-agent': ua.random,
    }
    data = {
        'fid': '-1',
        'uname': get_aes(USERNAME),
        'password': get_aes(PASSWORD),
        'refer': 'http%3A%2F%2Fi.mooc.chaoxing.com',
        't': 'true',
        'forbidotherlogin': '0',
        'validate': '',
        'doubleFactorLogin': '0',
        'independentId': '0',
        'independentNameId': '0',
    }
    resp = requests.post(
        url,
        data=data,
        headers=headers
    )

    print(resp.json())
    set_cookie = resp.headers.get('set-cookie')     # 模拟登录获取cookie
    session = requests.Session()
    session.headers.update({'Cookie': set_cookie})  # 设置cookie
    res = session.get('https://i.mooc.chaoxing.com/space/index?t=1713263877416')
    print(res.text)
