#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：python-spider 
@File    ：toutiao_decode.py
@Author  ：wangxw
@Date    ：2023/7/19 11:53 
@Desc    ：头条js解密，涉及参数：as，cp，_signature
"""
import subprocess


def get_sign_key(url):
    """
    根据传入的url，生成签名串
    @param url: 传入的基础URL
    @return: 生成的签名串_signature
    """
    node_path = '/usr/local/bin/node'  # 替换为实际的 Node.js 可执行文件路径
    script_path = './touTiaoSign.js'  # 替换为实际的 JavaScript 文件路径
    command = [node_path, script_path, url]
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()
    sign_key = output.decode().strip()
    return sign_key


def get_as_cp():
    """
    使用js文件生成头条链接所需的as和cp参数值
    @return: 包含as和cp参数值的列表，第一位为as值，第二位为cp值
    """
    node_path = '/usr/local/bin/node'  # 替换为实际的 Node.js 可执行文件路径
    script_path = 'as_cp.js'  # 替换为实际的 JavaScript 文件路径
    command = [node_path, script_path]
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()
    result = output.decode('utf-8').strip()
    result = result.split('\n')
    return result
