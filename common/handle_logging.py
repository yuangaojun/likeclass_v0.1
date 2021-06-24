# -*- coding:utf-8 -*-
"""
==============================
Author:yuan
Time  :2021/4/21 9:55
file  :handle_logging.py
===============================
"""
import logging
import os
from common.handle_path import LOG_DIR
from logging.handlers import TimedRotatingFileHandler
from common.handle_config import conf

class HandlerLogging():
    '''创建日志'''

    def create_log(self):
        '''创建日志'''

        # 创建日志对象
        log = logging.getLogger('yuan')
        # 设置日志收集等级
        log.setLevel(conf.get('env','log_level'))
        # 日志保存路径
        log_dir = os.path.join(LOG_DIR,conf.get('env','log_filename'))
        # 创建日志收集器输出渠道
        fh_log = TimedRotatingFileHandler(filename=log_dir,when='M',interval=60,
                                          backupCount=7,encoding='utf-8')
        # 设置日志输出等级
        fh_log.setLevel(conf.get('env','sh_level'))
        log.addHandler(fh_log)

        # 设置日志输出格式
        formats = '%(asctime)s - [%(filename)s-->line:%(lineno)d] - %(levelname)s: %(message)s'
        format = logging.Formatter(formats)
        fh_log.setFormatter(format)

        return log

log = HandlerLogging().create_log()
