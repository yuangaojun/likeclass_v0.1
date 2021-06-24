"""
==============================
Author:yuan
Time  :2021/4/30 11:13
file  :test_login.py
===============================
"""
import unittest
import os
from requests import request
from library.myddt import ddt, data
from common.handler_excel import HandlerExcel
from common.handle_path import TESTDATA_DIR
from common.handle_replace_data import replace_data
from common.handle_config import conf


@ddt
class TestLogin(unittest.TestCase):
    datas_file = os.path.join(TESTDATA_DIR, 'case_data.xlsx')
    excel = HandlerExcel(datas_file, 'login')
    case_data = excel.read_excel_data()

    @unittest.skip("登录方法不执行")
    @data(*case_data)
    def test_login(self, case):
        """
        测试登录接口
        :param case:用例数据接收参数
        :return:
        """
        header = {'Content-Type': 'application/x-www-form-urlencoded'}
        url = case['url']
        method = case['method']
        data = eval(replace_data(case['case_data']))
        response = request(headers=header, url=url, data=data, method=method)
        self.excel.back_write_excel(case['case_id'] + 1, 6, str(response.json()))


if __name__ == '__main__':
    unittest.main()
