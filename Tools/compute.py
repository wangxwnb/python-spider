#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：python-spider 
@File    ：compute.py
@Author  ：wangxw
@Date    ：2023/7/20 11:25 
@Desc    ：
"""
from PIL import ImageFont
from fontTools.ttLib import ttFont


def compute(fontPath, num_line=10, space_columns=10):
    """
    计算适宜画布大小及字体大小，以便可以正确显示图形表现
    @param fontPath: 字体集路径
    @param num_line: 每行最大字数
    @param space_columns: 列间距高度
    @return:
    """

    # 字体大小
    font_size = 40
    # 加载字体文件并创建字体对象
    font = ImageFont.truetype(fontPath, font_size)

    # 初始化画布的大小
    canvas_width = 0
    canvas_height = 0

    # 初始化最大字体宽度和总字体高度
    max_char_width = 0
    max_char_height = 0
    total_char_width = 0
    total_char_height = 0

    # 默认边距和字体行间距
    margin = 20
    spacing = 10

    ttf = ttFont.TTFont(fontPath)
    ttf_t = ttf.getGlyphOrder()[2:]
    uni_text = list(map(lambda x: "\\u" + x[3:], ttf_t))
    for i in range(len(uni_text)):
        char = chr(int(uni_text[i][2:], 16))  # # 字体集是\u10071样式的，解码成汉字，然后转换成字符串
        # 获取字符的宽度和高度
        bbox = font.getbbox(char)

        # 计算字符的宽度和高度
        char_width = bbox[2] - bbox[0]
        char_height = bbox[3] - bbox[1]
        # char_width, char_height = font.getsize(char)
        # 更新最大字体宽度和总字体高度
        max_char_width = max(max_char_width, char_width)
        max_char_height = max(max_char_height, char_height)
        total_char_width += char_width
        total_char_height += char_height

    # 计算画布的大小
    # num_columns = num_line  # 每行的字符数量
    num_rows = (len(uni_text) + num_line - 1) // num_line  # 需要的行数
    # 适宜宽度为每行的字符数量*最大字体宽度+字体行间距+前后边距
    canvas_width = num_line * max_char_width + margin * 2
    # 适宜高度为行数*字体最大高度+总列间距 + 上线边距
    canvas_height = num_rows * max_char_height + (num_rows - 1) * space_columns + margin * 2

    result = {
        'canvas_width': canvas_width,  # 建议画布宽度
        'canvas_height': canvas_height,  # 建议画布高度
        'total_char_width': total_char_width,  # 总字体宽度
        'total_char_height': total_char_height,  # 总字体高度
        'max_char_width': max_char_width,  # 单个字体最大宽度
        'max_char_height': max_char_height  # 单个字体最大高度
    }
    print(result)
    return result


def test():
    compute('font.ttf', 35)


if __name__ == '__main__':
    test()
