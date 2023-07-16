#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：python-spider 
@File    ：jinritoutiao.py
@Author  ：wangxw
@Date    ：2023/7/14 14:18 
@Desc    ：
'''

import requests
from lxml import etree

class JinRiTouTiao(object):
    def __init__(self):
        self.url = 'https://www.toutiao.com/'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_4; en-US; AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.127 Safari/534.16'
        }

    def get_html(self):
        res = requests.get(self.url, headers=self.headers)
        res.encoding = res.apparent_encoding
        print(res.text)
        return res.text



def main():
    jrtt = JinRiTouTiao()
    jrtt.get_html()


if __name__ == '__main__':
    main()




