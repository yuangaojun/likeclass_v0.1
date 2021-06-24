"""
==============================
Author:yuan
Time  :2021/6/7 11:29
file  :test_product_put.py
===============================
"""
import unittest
import os
from common.handle_path import TESTDATA_DIR
from library.myddt import ddt, data
from common.handle_web_method import HandleWeb
from common.handle_replace_data import EnvData, replace_data
from jsonpath import jsonpath
from common.handle_config import conf
from common.handle_random_data import RandomData
from requests import request
from common.handler_excel import HandlerExcel
from common.handle_logging import log
from common.handle_sql import HandlerMysql


@ddt
class TestProductPut(unittest.TestCase):
    '''商品上架测试类'''
    web = HandleWeb()
    rand = RandomData()
    excel = HandlerExcel(os.path.join(TESTDATA_DIR, "case_data.xlsx"), "product_put")
    case_data = excel.read_excel_data()
    db = HandlerMysql()

    @classmethod
    def setUpClass(cls):
        '''上架商品前置-登录企业管理端'''
        login_response = cls.web.login("企业端")
        cls.access_token = jsonpath(login_response, "$..access_token")[0]
        setattr(EnvData, "access_token", cls.access_token)

    def setUp(self):
        '''商品上架前置-创建商品'''
        setattr(EnvData, "cnName", self.rand.random_product_cnname())
        setattr(EnvData, "fnName", self.rand.random_product_fnname())
        self.headers = {"Content-Type": "application/json", "Authorization": "Bearer " + self.access_token}
        url = conf.get("service", "domain") + "/business/api/products"
        method = "post"
        body_data = {
            "productAttribute": {
                "productAttributeClass": {
                    "isTeacher": False,
                    "isInterest": True,
                    "isStudentBook": True,
                    "isClasses": False,
                    "isLimitCancel": True,
                    "cancelNumber": 6
                },
                "productAttributePeriod": {
                    "isDelayPeriod": True,
                    "isFrozenPeriod": True,
                    "delayPeriodBefore": 1,
                    "delayPeriodAfter": 10,
                    "delayStageType": 1,
                    "frozenPeriod": 10,
                    "frozenCount": 3
                },
                "productAttributeSign": {
                    "isSignChange": True,
                    "signChangeDay": 11
                },
                "productAttributeGift": {
                    "isRegisterGift": True,
                    "isStaffGift": True,
                    "giftDay": 10,
                    "giftYear": 2
                },
                "productAttributeService": {
                    "isSa": True
                }
            },
            "coverFile": {
                "id": "1402162508120498178",
                "fileName": "likeclass/1381819360265039874/2021/06/%E5%9B%BE%E7%89%87-2.png",
                "size": 399445,
                "mimeType": "image/png",
                "fileUrl": "https://testoss.likeshuo.com/likeclass/1381819360265039874/2021/06/%25E5%259B%25BE%25E7%2589%2587-2.png",
                "expireTime": 3600,
                "acl": "public-read",
                "ext": ".png"
            },
            "productCancel": {},
            "productDelay": {},
            "productInfo": {
                "cover": "1402162508120498178",
                "labelIds": ["1384842551164223489"],
                "cnName": "#cnName#",
                "orgId": "1382572490914717698",
                "orgCnName": "成人英语",
                "productType": 1,
                "labels": [{
                    "labelId": "1384842551164223489",
                    "labelCnName": "奶茶"
                }],
                "reward": "100",
                "period": "60",
                "productPeriodTypeIds": ["1401812042138763265", "1392683802991345665", "1392683769227198466",
                                         "1392683729523916801"],
                "productPeriodType": 1,
                "contractTemplateId": "1400730492533981186",
                "price": "666",
                "description": "商品简介",
                "fnName": "#fnName#"
            },
            "productLesson": {
                "associatedType": 2,
                "productClassTypes": [{
                    "quantity": "3",
                    "classTypeId": "1382587378483011585",
                    "isLimit": True
                }],
                "productSubjectCatalog": {
                    "productSubjectCatalogDetails": [{
                        "subjectCatalogId": "1397080878956855298",
                        "subjectCatalogCnName": "第三级",
                        "subjectCatalogCnNames": ["佐佐木私教课程", "第一级", "第二级", "第三级"],
                        "quantity": "3"
                    }]
                }
            },
            "maxOrderClass": 1
        }
        body = eval(replace_data(str(body_data)))
        self.create_product_response = request(method=method, url=url, headers=self.headers, json=body).json()

    # @unittest.skip('跳过该方法')
    @data(*case_data)
    def test_product_put(self, case):
        '''上架商品'''
        request_headers = self.headers
        request_method = case["method"]
        request_url = conf.get("service", "domain") + case["url"]
        product_id_sql = "select id from lks_business.product where cn_name = '{}';".format(EnvData.cnName)
        product_id = self.db.find_one(product_id_sql)["id"]
        setattr(EnvData, "productId", str(product_id))
        setattr(EnvData, "productName", EnvData.cnName)
        datas = case["case_data"]
        if jsonpath(eval(datas), "$..salePlatformName") != False:
            sale_platform_name = jsonpath(eval(datas), "$..salePlatformName")[0]
            setattr(EnvData, "productNumber",
                    self.rand.random_sale_product_number(sale_platform_name))
            sale_platform_id_sql = "select id from lks_business.sale_platform where cn_name = '{}' order by create_time desc limit 1;".format(
                sale_platform_name)
        else:
            sale_platform_name = "天猫"
            sale_platform_id_sql = "select id from lks_business.sale_platform where cn_name = '{}' order by create_time desc limit 1;".format(
                sale_platform_name)
            setattr(EnvData, "productNumber",
                    self.rand.random_sale_product_number(sale_platform_name))
        sale_platform_id = self.db.find_one(sale_platform_id_sql)["id"]
        setattr(EnvData, "salePlatformId", str(sale_platform_id))
        test_data = replace_data(datas)
        self.request_data = eval(test_data)
        expected_result = eval(case["expected"])
        self.response = request(method=request_method, headers=request_headers, url=request_url,
                                json=self.request_data).json()
        try:
            self.assertEqual(self.response["code"], expected_result["code"])
            self.assertEqual(self.response["msg"], expected_result["msg"])
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
        '''商品上架后置处理-下架商品及删除商品'''
        try:
            if self.response["code"] == "000000" and self.response["msg"] == "成功":
                # 下架商品
                headers = self.headers
                putaway_id_sql = "select id from lks_business.product_putaway where cn_name = '{}'order by create_time desc limit 1;".format(
                    jsonpath(self.request_data, "$..cnName")[0])
                putaway_id = self.db.find_one(putaway_id_sql)["id"]
                url = conf.get("service", "domain") + "/business/api/product-put-away/{}/out-stock".format(putaway_id)
                body = {"promptly": True}
                request(headers=headers, method="PUT", url=url, json=body).json()
                # 删除上架商品
                delete_put_product_url = conf.get("service", "domain") + "/business/api/product-put-away/{}".format(
                    putaway_id)
                request(headers=headers, url=delete_put_product_url, method="DELETE", json=None).json()
        except:
            print("无需执行后置处理")
        finally:
            # 删除商品库新建的对应的商品
            if self.create_product_response["code"] == "000000":
                self.product_id = self.db.find_one(
                    "select id from lks_business.product where cn_name = '{}' order by create_time desc limit 1;".format(
                        EnvData.cnName))
                delete_product_url = conf.get("service", "domain") + "/business/api/products/{}/status".format(
                    self.product_id["id"])
                request(headers=self.headers, method="PUT", url=delete_product_url, json=None).json()


if __name__ == '__main__':
    unittest.main()
