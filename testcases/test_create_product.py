"""
==============================
Author:yuan
Time  :2021/5/8 16:05
file  :test_create_product.py
===============================
"""
import unittest
import os
import time
from library.myddt import ddt, data
from requests import request
from jsonpath import jsonpath
from common.handle_replace_data import EnvData, replace_data
from common.handle_config import conf
from common.handler_excel import HandlerExcel
from common.handle_path import TESTDATA_DIR
from common.handle_web_method import HandleWeb
from common.handle_random_data import RandomData
from common.handle_sql import HandlerMysql
from common.handle_logging import log


@ddt
class TestCreateProduct(unittest.TestCase):
    '''
    创建商测试类
    '''
    excel = HandlerExcel(os.path.join(TESTDATA_DIR, "case_data.xlsx"), "create_product")
    case_data = excel.read_excel_data()
    web = HandleWeb()
    random_data = RandomData()
    db = HandlerMysql()

    @classmethod
    def setUpClass(cls):
        '''添加商品前置-登录企业端'''
        # 登录企业端并获取token
        login_response = cls.web.login("企业端")
        cls.access_token = jsonpath(login_response, "$..access_token")[0]
        setattr(EnvData, "access_token", cls.access_token)

    def setUp(self):
        setattr(EnvData, "cnName", self.random_data.random_product_cnname())
        setattr(EnvData, "fnName", self.random_data.random_product_fnname())

    # @unittest.skip("跳过创建商品接口测试用例")
    @data(*case_data)
    def test_create_product(self, case):
        '''
        创建商品
        :param case:用例数据接收参数
        :return:
        '''
        request_headers = {"Content-Type": "application/json", "Authorization": "Bearer " + self.access_token}
        request_url = conf.get("service", "domain") + case["url"]
        request_method = case["method"]
        test_data = replace_data(case["case_data"])
        request_data = eval(test_data)
        self.response = request(method=request_method, headers=request_headers, url=request_url,
                                json=request_data).json()
        expected_results = eval(case["expected"])
        try:
            self.assertEqual(expected_results["code"], self.response["code"])
            self.assertEqual(expected_results["msg"], self.response["msg"])
            result = "Pass"
            log.info("{}--用例断言成功，测试通过".format(case["title"]))
        except AssertionError as e:
            result = "Fail"
            log.error("{}--用例断言失败，测试不通过\n{}".format(case["title"], e))
            raise e
        finally:
            self.excel.back_write_excel(case["case_id"] + 1, 7, str(self.response))
            self.excel.back_write_excel(case["case_id"] + 1, 8, str(result))

    def tearDown(self):
        # ES在写入的同时修改数据造成写入不成功
        # time.sleep(0.3)
        '''后置处理-添加完商品后删除该商品'''
        if self.response["code"] == "000000" and self.response["msg"] == "成功":
            self.product_id = self.db.find_one(
                "select id from lks_business.product where cn_name = '{}';".format(EnvData.cnName))
            url = conf.get("service", "domain") + "/business/api/products/{}/status".format(self.product_id["id"])
            headers = {"Content-Type": "application/json", "Authorization": "Bearer " + self.access_token}
            request(headers=headers, method="PUT", url=url, json=None).json()
        else:
            pass


if __name__ == '__main__':
    unittest.main()
