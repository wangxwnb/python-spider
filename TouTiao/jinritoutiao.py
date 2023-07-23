#!/usr/bin/env python
# !/usr/local/bin/node
# -*- coding: UTF-8 -*-
"""
@Project ：python-spider
@File    ：jinritoutiao.py
@Author  ：wangxw
@Date    ：2023/7/14 14:18
@Desc    ：
"""
import csv
import requests
import toutiao_decode
from urllib.parse import urlencode, urljoin


def save_data(hot_list):
    """
    保存数据
    @param hot_list:热榜数据列表
    @return:
    """
    with open('TopHot.csv', 'w', newline='') as cf:
        writer = csv.writer(cf)
        for i in hot_list:
            rows = list(i.values())
            writer.writerow(rows)


def build_url(base_url, params):
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


class JinRiTouTiao(object):
    def __init__(self):
        # self.url = 'https://www.toutiao.com/api/pc/list/feed'
        self.hot_url = 'https://www.toutiao.com/hot-event/hot-board/?origin=toutiao_pc'
        self.params = {
            'channel_id': '3189398999',
            'min_behot_time': '0',
            'max_behot_time': '0',
            'offset': '0',
            'refresh_count': '1',
            'category': 'pc_profile_channel',
            'client_extra_params': '{"short_video_item":"filter"}',
            'aid': '24',
            'app_name': 'toutiao_web',
        }

        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_4; en-US; AppleWebKit/534.16 (KHTML, '
                          'like Gecko) Chrome/10.0.648.127 Safari/534.16',
            'Cache-Control': 'no-transform',
            'Referer': 'https://www.toutiao.com/',
            'Sec-Ch-Ua-Platform': '"macOS"',
            'Sec-Fetch-Site': 'none',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Dest': 'document',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Sec-Ch-Ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,'
                      '*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Sec-Ch-Ua-Mobile': '?0',
        }

    def get_json_date(self):
        # 生成签名串
        sign_key = toutiao_decode.get_sign_key(self.hot_url)  # url
        # 拼接成请求URL
        complete_url = self.hot_url + '&_signature=' + sign_key
        print(complete_url)
        res = requests.get(complete_url, headers=self.headers)
        res.encoding = res.apparent_encoding
        data_list = res.json()['data']  # 热榜数据
        # fixed_top_data = res.json()['fixed_top_data']  # 热榜置顶
        # dict = {
        #     'title': fixed_top_data[0]['Title'],
        #     'url': fixed_top_data[0]['Url']
        # }
        # hot_list = [dict]
        hot_list = []
        for i, data_dict in enumerate(data_list):
            hot_dict = {
                'number': i + 1,  # 排名
                'title': data_dict['Title'],
                'url': data_dict['Url']
            }

            hot_list.append(hot_dict)
        print(hot_list)
        print(len(hot_list))
        save_data(hot_list)


def main():
    toutiao = JinRiTouTiao()
    toutiao.get_json_date()


if __name__ == '__main__':
    main()
