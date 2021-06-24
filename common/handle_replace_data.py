# -*- coding:utf-8 -*-
"""
==============================
Author:yuan
Time  :2021/4/21 15:22
file  :handle_replace_data.py
===============================
"""

import re
from common.handle_config import conf


class EnvData():
    pass


def replace_data(data):
    '''替换数据'''
    while re.search('#(.*?)#', data):
        # 返回一个匹配对象
        res = re.search('#(.*?)#', data)
        # 返回一个匹配到的值，包含首位
        key = res.group()
        # 返回一个匹配到的括号里面的值
        item = res.group(1)
        try:
            value = conf.get('case_data', item)
        except:
            value = getattr(EnvData, item)
        data = data.replace(key, value)
    return data
