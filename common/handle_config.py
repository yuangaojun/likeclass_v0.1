# -*- coding:utf-8 -*-
"""
==============================
Author:yuan
Time  :2021/4/20 15:00
file  :handle_config.py
===============================
"""
import os
from configparser import RawConfigParser
from common.handle_path import CONF_DIR


def get_configfile_dir():
    return os.path.join(CONF_DIR, 'likeClass.ini')


class HandleConfig(RawConfigParser):
    '''配置文件读取'''

    def __init__(self, filename):
        super().__init__()
        self.read(filename, encoding='utf-8')


conf = HandleConfig(get_configfile_dir())
