"""
==============================
Author:yuan
Time  :2021/4/19 15:02
file  :run.py
===============================
"""
from unittestreport import TestRunner
import unittest
import os
import time
from BeautifulReport import BeautifulReport
from common.handle_path import REPORT_DIR, TESTCASE_DIR
from common.handle_send_email import HandlerEmail


def get_now_time():
    now_time = time.strftime('%Y-%m-%d_%H%M%S', time.localtime(time.time()))
    return now_time


def run():
    suite = unittest.defaultTestLoader.discover(
        start_dir=TESTCASE_DIR,
        pattern='test_*.py',
        top_level_dir=None
    )
    report = BeautifulReport(suite)
    # report_file = os.path.join(get_now_time() + 'likeClass_report.html')
    report.report(description='likeClass接口自动化测试报告', report_dir=REPORT_DIR, filename="report.html")
    send_email = HandlerEmail()
    send_email.send_email()


def run_unittest_report():
    suite = unittest.defaultTestLoader.discover(
        start_dir=TESTCASE_DIR)
    # 创建测试运行程序
    runner = TestRunner(suite,
                        tester='测试人员—系统',
                        filename="report.html",
                        report_dir=REPORT_DIR,
                        title='接口测试报告',
                        desc='报告描述',
                        templates=1)
    # 运行用例，生成测试报告
    runner.run()
    # runner.send_email(
    #     host="smtp.exmail.qq.com",
    #     port=465,
    #     user="gaojun_ygj@meten.com",
    #     password="gDQYeMJyZRv5u8ix",
    #     to_addrs="betty_zxq@meten.com")

    # runner.run(count=3, interval=2)


if __name__ == '__main__':
    run_unittest_report()
    # run()
