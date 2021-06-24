# -*- coding:utf-8 -*-
"""
==============================
Author:yuan
Time  :2021/4/19 10:07
file  :handle_path.py
===============================
"""
import os

# 项目路径
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# 配置文件路径
CONF_DIR = os.path.join(BASE_DIR, 'conf')

# 测试报搞路径
REPORT_DIR = os.path.join(BASE_DIR,'reports')

# 日志文件路径
LOG_DIR = os.path.join(BASE_DIR,'logs')

# 测试用例文件路径
TESTCASE_DIR = os.path.join(BASE_DIR,'testcases')

# 测试用例数据文件路径
TESTDATA_DIR = os.path.join(BASE_DIR,'testdatas')
