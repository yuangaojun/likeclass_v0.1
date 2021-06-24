"""
==============================
Author:yuan
Time  :2021/6/16 19:07
file  :test_teacher_requirement.py
===============================
"""

import unittest
import os
from requests import request
from common.handle_logging import log
from common.handler_excel import HandlerExcel
from common.handle_path import TESTDATA_DIR
from common.handle_sql import HandlerMysql
from jsonpath import jsonpath
from common.handle_replace_data import EnvData, replace_data
from common.handle_web_method import HandleWeb
from common.handle_config import conf
from common.handle_random_data import RandomData
from library.myddt import ddt, data


@ddt
class TestTeacherRequirement(unittest.TestCase):
    '''导入订单'''

    excel = HandlerExcel(os.path.join(TESTDATA_DIR, "case_data.xlsx"), "teacher_requirement")
    case_data = excel.read_excel_data()
    db = HandlerMysql()
    web = HandleWeb()
    random_data = RandomData()

    @classmethod
    def setUpClass(cls):
        '''上架商品前置-登录企业管理端'''
        login_response = cls.web.login("企业端")
        cls.access_token = jsonpath(login_response, "$..access_token")[0]
        setattr(EnvData, "access_token", cls.access_token)

    @data(*case_data)
    def test_teacher_requirement(self, case):
        '''
        测试教师提交需求
        :param case:用例数据接收参数
        :return:
        '''
        teacher_requirement_header = {"Content-Type": "application/json",
                                      "Authorization": "Bearer " + self.access_token, "PlatformType": "2"}
        teacher_requirement_url = conf.get("service", "domain") + case["url"]
        teacher_requirement_method = case["method"]
        test_data = case["case_data"]
        teacher_id_sql = "select id from lks_teaching.teacher where fn_name = '{}';".format(
            conf.get("case_data", "teacher_username"))
        teacher_id = self.db.find_one(teacher_id_sql)["id"]
        setattr(EnvData, "teacherId", str(teacher_id))
        if "提交需求时间小于当前时间" not in case["title"]:
            setattr(EnvData, "time", self.random_data.later_now_time())
        else:
            setattr(EnvData, "time", self.random_data.earlier_now_time())
        teacher_requirement_request_data = eval(replace_data(test_data))
        teacher_requirement_response = request(headers=teacher_requirement_header, method=teacher_requirement_method,
                                               url=teacher_requirement_url,
                                               json=teacher_requirement_request_data).json()
        expected = eval(case["expected"])
        try:
            self.assertEqual(expected["code"], teacher_requirement_response["code"])
            self.assertEqual(expected["msg"], teacher_requirement_response["msg"])
            result = "Pass"
            log.info("{}--用例断言成功，测试通过".format(case["title"]))
        except AssertionError as e:
            result = "Fail"
            log.error("{}--用例断言失败，测试不通过".format(case["title"]))
            raise e
        finally:
            self.excel.back_write_excel(case["case_id"] + 1, 7, str(teacher_requirement_response))
            self.excel.back_write_excel(case["case_id"] + 1, 8, str(result))


if __name__ == '__main__':
    unittest.main()
