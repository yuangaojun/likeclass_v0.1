# -*- coding:utf-8 -*-
"""
==============================
Author:yuan
Time  :2021/4/22 15:30
file  :handle_send_email.py
===============================
"""
import smtplib
import os
from common.handle_path import REPORT_DIR
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication


class HandlerEmail():

    def send_email(self):
        '''发送邮件'''
        # 连接邮箱服务器
        smtp = smtplib.SMTP_SSL(host='smtp.exmail.qq.com', port='465')
        # 登录邮箱
        smtp.login(user='gaojun_ygj@meten.com', password='gDQYeMJyZRv5u8ix')
        # 创建一封多组件的邮件
        msg = MIMEMultipart()
        msg['Subject'] = 'likeclass接口测试报告'
        msg['To'] = 'betty_zxq@meten.com'
        msg['From'] = 'gaojun_ygj@meten.com'
        text = MIMEText('附件为测试报告', _charset='utf-8')
        msg.attach(text)

        # 添加测试报告为邮件附件
        with open(os.path.join(REPORT_DIR, 'report.html'), 'rb') as f:
            content = f.read()
        report = MIMEApplication(content)
        report.add_header('content-disposition', 'attachment', filename='report.html')
        msg.attach(report)

        # 发送邮件
        # smtp.send_message(msg, to_addrs='771305126@qq.com', from_addr='musen_nmb@qq.com') betty_zxq@meten.com
        smtp.send_message(msg, from_addr='gaojun_ygj@meten.com',to_addrs=['gaojun_ygj@meten.com'])


if __name__ == '__main__':
    aa = HandlerEmail()
    aa.send_email()
