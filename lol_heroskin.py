#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：python-spider 
@File    ：lol_heroskin.py
@Author  ：wangxw
@Date    ：2023/7/13 22:04 
@Desc    ：
'''
import time
from concurrent.futures import ThreadPoolExecutor
import requests
import os

class LolHeroskin(object):
    '''
    爬取lol所有英雄皮肤
    '''
    def __init__(self):
        self.url = 'https://game.gtimg.cn/images/lol/act/img/js/heroList/hero_list.js?ts=2815671'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/56.0.2924.87 UBrowser/6.2.0.1067.8 Safari/537.36',
        }
        self.hero_url = []

    def get_hero_url(self):
        res = requests.get(self.url,headers = self.headers)
        hero_list = res.json()['hero']
        for hero in hero_list:
            hero_dict={
                'heroname': hero['name'] + '-' + hero['title'],
                'heroId': hero['heroId'],
                'heroUrl': 'https://game.gtimg.cn/images/lol/act/img/js/hero/{}.js?ts=2815675'.format(hero['heroId'])
            }
            self.hero_url.append(hero_dict)
        # print(self.hero_url)

    def get_hero_pic(self):
        # 获取所有英雄详情的url
        self.get_hero_url()
        # 获取所有英雄皮肤信息的列表
        skin_list = []
        for hero in self.hero_url:
            res = requests.get(hero['heroUrl'],headers = self.headers)
            skin_list.append(res.json()['skins'])
        # 数据清洗，去掉炫彩皮肤的信息
        skin_list_real = [] # 最终下载url和name
        for list in skin_list:
            list_real = []
            for i,dict in enumerate(list):
                if dict['chromas'] == '0':
                    list_real.append({'name':dict['name'],'mainImg':dict['mainImg'],'heroName':dict['heroName']+'-'+dict['heroTitle']})
            skin_list_real.append(list_real)

        # print(skin_list_real)
        # 包含最终皮肤下载url的列表,常规版
        # for list_skin in skin_list_real:
        #     for dict_skin in list_skin:
        #         self.download_pic(dict_skin,dict_skin['heroName'])

        # 多线程版
        with ThreadPoolExecutor(max_workers=8) as executor:
            for list_skin in skin_list_real:
                for dict_skin in list_skin:
                    executor.submit(self.download_pic,dict_skin, dict_skin['heroName'])
        print('下载完成!')

    def download_pic(self,pic_url,dir_name):
        '''

        Args:
            pic_url:
            dir_name:

        Returns:

        '''
        file_path = "./"+dir_name
        if not os.path.exists(file_path):  # 判断文件夹是否存在
            os.makedirs(file_path)  # 创建文件夹
        pic_name = file_path + '/' + pic_url['name'].replace('/','') + '.jpg' # K/DA类型的皮肤名称渠道'/'
        if os.path.exists(pic_name):
            print('{}已经存在'.format(pic_name))
            return pic_name
        else:
            print('{}不存在，正在下载'.format(pic_name))
            pic = requests.get(pic_url['mainImg'],headers = self.headers).content
            with open(pic_name,'wb') as f:
                f.write(pic)
            time.sleep(3)
def main():
    lol_skin = LolHeroskin()
    lol_skin.get_hero_pic()

if __name__ == '__main__':
    main()