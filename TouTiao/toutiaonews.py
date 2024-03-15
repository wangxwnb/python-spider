#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：python-spider 
@File    ：toutiaonews.py
@Author  ：wangxw
@Date    ：2023/7/18 18:31 
@Desc    ：
"""

from urllib.parse import urlencode, urljoin
import requests
import time
import toutiao_decode


class TouTiao(object):
    def __init__(self):
        self.hot_url = 'https://m.toutiao.com/list/'
        self.url = 'https://www.toutiao.com/api/pc/feed/?category=news_game&utm_source=toutiao&widen=1&max_behot_time=0&max_behot_time_tmp=0&tadrequire=true'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_4; en-US; AppleWebKit/534.16 (KHTML, '
                          'like Gecko) Chrome/10.0.648.127 Safari/534.16',
            'Referer': 'https://m.toutiao.com/?source=m_redirect&channel=tech',
            'Host': 'm.toutiao.com'
        }
        self.params = {
            'tag': 'news_hot',
            'max_time': '0',
            'min_behot_time': '0',
            'ac': 'wap',
            'count': '20',
            'format': 'json_raw',
            'i': '',
            'aid': '1698'
        }

    def get_as_cp(self):
        result = toutiao_decode.get_as_cp()
        current_timestamp = time.time()
        five_hours_ago_timestamp = current_timestamp - 10 * 60 * 60
        self.params['max_time'] = self.params['i'] = str(round(time.time()))
        self.params['min_behot_time'] = str(round(five_hours_ago_timestamp))
        # url = self.build_url(self.hot_url,self.params) +'&as=' + result[0] + '&cp=' + result[1]
        url = self.url + '&as=' + result[0] + '&cp=' + result[1]
        # url = 'https://m.toutiao.com/list/?tag=__all__&max_time=0&min_behot_time=0&ac=wap&count=20&format=json_raw&i=&aid=1698&'
        # com_url = url + 'as=' + result[0] + '&cp=' + result[1]
        print(url)
        return url

    def build_url(self, base_url, params):
        """
        构建需要生成签名串的URL
        @param base_url: 基础url
        @param params: 参数列表
        @return: 拼接参数后的url
        """
        # 将参数编码为 URL 查询字符串,':'不转义
        query_string = urlencode(params, safe=':')
        # 将查询字符串拼接到基础 URL 中
        complete_url = urljoin(base_url, '?' + query_string)

        return complete_url

    def get_json(self):
        news_url = self.get_as_cp()
        res = requests.get(url=news_url, headers=self.headers)
        res.encoding = 'gbk'
        print(res.json())
        news_data = res.json()['data']
        news_list = []
        for data in news_data:
            news_dict = {
                'title': data.get('title'),
                # 'url': data.get('url')
                'url': 'https://www.toutiao.com' + data.get('source_url')
            }
            news_list.append(news_dict)
            print(news_dict)


def main():
    toutiao_news = TouTiao()
    toutiao_news.get_json()


if __name__ == '__main__':
    main()
