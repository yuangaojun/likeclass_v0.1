"""
==============================
Author:yuan
Time  :2021/6/15 17:48
file  :test_active_contract.py
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
class TestImportOrder(unittest.TestCase):
    '''导入订单'''

    excel = HandlerExcel(os.path.join(TESTDATA_DIR, "case_data.xlsx"), "active_contract")
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

    def setUp(self):
        '''导入商品订单前置-创建商品，上架商品'''
        # 商品上架前置-创建商品
        setattr(EnvData, "cnName", self.random_data.random_product_cnname())
        setattr(EnvData, "fnName", self.random_data.random_product_fnname())
        self.headers = {"Content-Type": "application/json", "Authorization": "Bearer " + self.access_token}
        url = conf.get("service", "domain") + "/business/api/products"
        method = "post"
        create_product_body_data = {
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
        body = eval(replace_data(str(create_product_body_data)))
        self.create_product_response = request(method=method, url=url, headers=self.headers, json=body).json()
        # 导入订单前置-商品上架
        put_away_product_data = {
            "putAwayDetails": [{
                "productId": "#productId#",
                "price": "#price#",
                "productPrice": "#productPrice#",
                "quantity": 1,
                "productName": "#productName#"
            }],
            "putAwayInfoList": [{
                "isSend": 1,
                "promptly": True,
                "cnName": "#cnName#",
                "salePlatformId": "#salePlatformId#",
                "productNumber": "#productNumber#",
                "undercarriageTime": "2029-06-30 00:00:00",
                "remark": "备注说明",
                "salePlatformName": "天猫"
            }]
        }
        product_info_sql = "select id,price from lks_business.product where cn_name = '{}';".format(EnvData.cnName)
        product_id = self.db.find_one(product_info_sql)["id"]
        price = self.db.find_one(product_info_sql)["price"]
        self.sale_platform_name = jsonpath(put_away_product_data, "$..salePlatformName")[0]
        sale_platform_id_sql = "select id from lks_business.sale_platform where cn_name = '{}' order by create_time desc limit 1;".format(
            self.sale_platform_name)
        product_number = self.random_data.random_sale_product_number(
            self.sale_platform_name)
        sale_platform_id = self.db.find_one(sale_platform_id_sql)["id"]
        setattr(EnvData, "productId", str(product_id))
        setattr(EnvData, "price", str(price))
        setattr(EnvData, "productPrice", str(price))
        setattr(EnvData, "productName", EnvData.cnName)
        setattr(EnvData, "productNumber", product_number)
        setattr(EnvData, "salePlatformId", str(sale_platform_id))
        put_away_product_request_data = eval(replace_data(str(put_away_product_data)))
        put_away_product_url = conf.get("service", "domain") + "/business/api/product-put-away"
        self.put_away_product_response = request(method="post", url=put_away_product_url, headers=self.headers,
                                                 json=put_away_product_request_data).json()
        # 导入订单
        import_order_header = self.headers
        import_order_url = conf.get("service", "domain") + "/business/api/orders/import"
        method = "post"
        datas = {
            "orders": [{
                "prefix": "86",
                "mobile": "#mobile#",
                "salePlatformOrderNumber": "#salePlatformOrderNumber#",
                "products": [{
                    "quantity": 2,
                    "productNumber": "#productNumber#"
                }],
                "paymentType": 1,
                "total": "#total#",
                "paymenteds": "#paymenteds#",
                "discount": None,
                "denomination": None,
                "integral": None,
                "privilege": None,
                "poundage": None
            }]
        }
        setattr(EnvData, "mobile", conf.get("case_data", "student_username"))
        sale_platform_order_number = self.random_data.random_saleplatform_orderno(self.sale_platform_name)
        setattr(EnvData, "salePlatformOrderNumber", sale_platform_order_number)
        setattr(EnvData, "productNumber", EnvData.productNumber)
        sql = "select price from lks_business.product where cn_name = '{}';".format(EnvData.cnName)
        price = self.db.find_one(sql)["price"]
        quantity = jsonpath(datas, "$..quantity")[0]
        if quantity != None and type(quantity) == int:
            total = str(quantity * price)
            setattr(EnvData, "total", total)
            setattr(EnvData, "paymenteds", total)
        test_data = eval(replace_data(str(datas)))
        self.import_order_response = request(method=method, url=import_order_url, headers=import_order_header,
                                             json=test_data).json()

    @data(*case_data)
    def test_active_contract(self, case):
        '''激活协议测试'''
        active_contract_header = self.headers
        active_contract_method = case["method"]
        if "合同协议已激活再次进行激活" not in case["title"]:
            contract_id_sql = "select id from lks_business.student_contract where order_id =\n" \
                              "(select id from lks_business.order where sale_platform_order_number = '{}'); ".format(
                EnvData.salePlatformOrderNumber)
        else:
            contract_id_sql = "select id from lks_business.student_contract where contract_status_type = '3' order by create_time desc limit 1; "
        contract_id = self.db.find_one(contract_id_sql)["id"]
        active_contract_url = conf.get("service", "domain") + case["url"].format(contract_id)
        active_contract_datas = case["case_data"]
        active_contract_test_data = eval(active_contract_datas)
        expected = eval(case["expected"])
        active_contract_response = request(headers=active_contract_header, url=active_contract_url,
                                           method=active_contract_method, json=active_contract_test_data).json()
        try:
            self.assertEqual(expected["code"], active_contract_response["code"])
            self.assertEqual(expected["msg"], active_contract_response["msg"])
            result = "Pass"
            log.info("{}--用例断言成功，测试通过".format(case["title"]))
        except AssertionError as e:
            result = "Fail"
            log.error("{}--用例断言失败，测试不通过".format(case["title"]))
            raise e
        finally:
            self.excel.back_write_excel(case["case_id"] + 1, 7, str(active_contract_response))
            self.excel.back_write_excel(case["case_id"] + 1, 8, str(result))

    def tearDown(self):
        try:
            if self.put_away_product_response["code"] == "000000" and self.put_away_product_response[
                "msg"] == "成功":
                # 下架商品
                headers = self.headers
                putaway_id_sql = "select id from lks_business.product_putaway where cn_name = '{}'order by create_time desc limit 1;".format(
                    EnvData.cnName)
                putaway_id = self.db.find_one(putaway_id_sql)["id"]
                url = conf.get("service", "domain") + "/business/api/product-put-away/{}/out-stock".format(putaway_id)
                body = {"promptly": True}
                request(headers=headers, method="PUT", url=url, json=body).json()
                # 删除上架商品
                delete_put_product_url = conf.get("service", "domain") + "/business/api/product-put-away/{}".format(
                    putaway_id)
                request(headers=headers, url=delete_put_product_url, method="DELETE", json=None).json()
        except Exception as e:
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
