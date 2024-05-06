#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：python-spider 
@File    ：caigou.py
@Author  ：wangxw
@Date    ：2023/7/20 16:45 
@Desc    ：
"""
import base64
import csv
import time
import requests
import re
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from fontTools.ttLib import ttFont
from Tools.compute import compute
from aip import AipOcr
from lxml import etree
from secret import APP_ID, API_KEY, SECRET_KEY


class CaiGou(object):
    def __init__(self):
        self.url = 'https://www.china.cn/buy/purchase/'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_4; en-US; AppleWebKit/534.16 (KHTML, '
                          'like Gecko) Chrome/10.0.648.127 Safari/534.16',
        }
        self.list_data = []
        """ 你的 APPID AK SK """
        self.APP_ID = APP_ID
        self.API_KEY = API_KEY
        self.SECRET_KEY = SECRET_KEY

    def get_unicode_list(self, page=1):
        """
        获取字符集
        @return: 字符集列表，网页源码
        """
        url = self.url + str(page) + '.html'
        res = requests.get(url, headers=self.headers)
        res_html = res.text
        # 用正则表达式获取字符集的url
        pattern = re.compile("src:url\(\'(.*?)\'\)")
        font_base64 = pattern.search(res_html).group(1)
        # 截取base64数据
        data = font_base64.split(',')[1]
        # 转成二进制
        decoded_data = base64.b64decode(data)
        # 保存成字体集
        with open('font.ttf', 'wb') as file:
            file.write(decoded_data)
        # with open('font.ttf', 'wb') as file:
        #     file.write(decoded_data)

        ttf = ttFont.TTFont("font.ttf")
        ttf_t = ttf.getGlyphOrder()[1:]  # 获取字形顺序
        unicode_list = list(map(lambda x: "\\u" + x[3:], ttf_t))  # 字符集列表
        print(unicode_list)
        return unicode_list, res_html  # 由于每次请求时网页中的字体集和文本都会发生变化，所以每页只能请求一次，这里把请求后的网页返回

    def get_font_image(self, unicode_list):
        """
        利用字符集列表画图
        @param unicode_list: 字符集列表
        @return:
        """
        space_columns = 10  # 列间距
        line_length = 35  # 每行35个汉字
        margin = 20  # 初始边距
        result = compute('font.ttf', line_length, space_columns)  # 计算画布大小和字体大小

        canvas_width = result['canvas_width']
        canvas_height = result['canvas_height']
        max_char_width = result['max_char_width']
        max_char_height = result['max_char_height']

        img = Image.new("RGB", (canvas_width, canvas_height), color=(255, 255, 255))  # 创建图片
        # 准备画笔
        img_draw = ImageDraw.Draw(img)
        # 准备画图的字符
        img_font = ImageFont.truetype("font.ttf", max_char_width)
        # 写入图片
        new_line = []

        for i in range(len(unicode_list)):
            uni = chr(int(unicode_list[i][2:], 16))  # # 字体集是\u10071样式的，解码成汉字，然后转换成字符串

            if i % line_length == 0 and i != 0:
                new_line_s = "".join(new_line)
                # 定义第一行画的位置
                if i // line_length == 1:
                    img_draw.text((margin, margin), new_line_s, fill=1, font=img_font)
                else:  # 每够一行画一次
                    img_draw.text((margin, (i // line_length - 1) * (max_char_height + space_columns) + margin),
                                  new_line_s, fill=1, font=img_font)
                new_line = [uni]
            else:
                new_line.append(uni)
        # 画最后一行的汉字
        if new_line:
            new_line_s = "".join(new_line)
            img_draw.text((margin, (i // line_length) * (max_char_height + space_columns) + margin), new_line_s, fill=1,
                          font=img_font)

        img.save("tu.jpg")  # 保存图片

    def get_date(self):
        """
        将网页源码中字符编码替换为对应汉字，并通过xpath获取需要的内容进行存储
        @return:
        """
        for i in range(1, 11):
            unicode_list, res_html = self.get_unicode_list(i)  # 获取字体集
            self.get_font_image(unicode_list)  # 获取图片

            with open('tu.jpg', 'rb') as f:
                client = AipOcr(self.APP_ID, self.API_KEY, self.SECRET_KEY)
                res = client.basicGeneral(f.read())

            result_list = []
            for txt in res["words_result"]:
                result_list.extend(txt["words"])  # 将字符串换成list

            font_dic = dict(zip(unicode_list, result_list))  # zip将内容对应存储

            # 替换字符编码前缀
            for un in font_dic:
                uni = font_dic[un]
                funi = un.replace("\\u", "&#x") + ";"
                # print(funi, uni)  # 打印每个编码和字体对照关系
                res_html = res_html.replace(funi, uni)
            # print(res_html)

            tree = etree.HTML(res_html)
            li_list = tree.xpath('//ul[@class="industry_ul"]/li')
            for li in li_list:
                title = li.xpath('./div[2]/div/h3/a/text()')[0].strip()
                if len(li.xpath('./div[1]/p[2]')) > 0:
                    place = li.xpath('./div[1]/p[2]/text()')[0].strip().replace('\xa0', '')
                else:
                    place = '收货地：无'
                release_time = li.xpath('./div[2]/div/span/text()')[0].strip()
                purchase_url = li.xpath('./div[2]/div/h3/a/@href')[0].strip()
                dict_purchase = {
                    'title': title,  # 标题
                    'place': place,  # 收货地址
                    'release_time': release_time,  # 发布时间
                    'purchase_url': purchase_url,  # 收货地址
                }
                # print(dict_purchase)
                self.list_data.append(dict_purchase)
                time.sleep(2)
        self.wirte_data(self.list_data)

    def wirte_data(self, list_data=[]):
        """
        写入数据到文件中
        @param list_data: 数据列表，内部是字典格式
        @return:
        """
        with open('caigou.csv', 'a') as f:
            writer = csv.writer(f)
            for i, dict_data in enumerate(list_data):
                fields = list(dict_data.keys())
                rows = list(dict_data.values())
                if i == 0:
                    # 写入字段名
                    writer.writerow(fields)
                # 写入数据行
                writer.writerow(rows)


def main():
    caigou = CaiGou()
    caigou.get_date()


if __name__ == '__main__':
    main()
