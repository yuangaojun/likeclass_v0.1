"""
==============================
Author:yuan
Time  :2021/5/11 10:25
file  :handle_web_method.py
===============================
"""

from requests import request
from common.handle_config import conf
from common.handle_replace_data import replace_data
from common.handle_replace_data import EnvData


class HandleWeb():
    def login(self, login_name):
        request_header = {"Content-Type": "application/x-www-form-urlencoded"}
        request_data = {
            "grant_type": "password",
            "username": "",
            "password": "",
            "scope": "all",
            "tenant": conf.get("case_data", "tenant"),
            "client_id": "likeclass-web",
            "device_type": "1"
        }
        url = conf.get("service", "domain") + "/auth/oauth/token"
        method = "post"
        if login_name == "学员端":
            request_data["username"] = conf.get("case_data", "student_username")
            request_data["password"] = conf.get("case_data", "student_password")
            response = request(headers=request_header, url=url, method=method, data=request_data).json()
            return response
        elif login_name == "教师端":
            request_data["username"] = conf.get("case_data", "teacher_username")
            request_data["password"] = conf.get("case_data", "teacher_password")
            print(request_data)
            response = request(headers=request_header, url=url, method=method, data=request_data).json()
            return response
        elif login_name == "企业端":
            request_data["username"] = conf.get("case_data", "qy_username")
            request_data["password"] = conf.get("case_data", "qy_password")
            response = request(headers=request_header, url=url, method=method, data=request_data).json()
            return response
        elif login_name == "平台管理端":
            request_data["username"] = conf.get("case_data", "pt_username")
            request_data["password"] = conf.get("case_data", "pt_password")
            response = request(headers=request_header, url=url, method=method, data=request_data).json()
            return response
        else:
            return "请检查登录系统的指定端名称是否正确，指定登录端名称：学员端，教师端，企业端，平台管理端！"

    def add_product(self, cnName, fnName):
        """创建商品"""
        products_url = conf.get("service", "domain") + "/business/api/products"
        products_method = "post"
        products_header = {"Content-Type": "application/json", "Authorization": "Bearer " + str(EnvData.access_token)}
        products_info = {
            "productAttribute": {
                "productAttributeClass": {
                    "isTeacher": False,
                    "isInterest": False,
                    "isStudentBook": True,
                    "isClasses": True,
                    "isLimitCancel": False
                },
                "productAttributePeriod": {
                    "isDelayPeriod": True,
                    "isFrozenPeriod": True,
                    "frozenCount": 2,
                    "delayPeriodBefore": 10,
                    "delayPeriodAfter": 20,
                    "delayStageType": 1,
                    "frozenPeriod": 3
                },
                "productAttributeSign": {
                    "isSignChange": True,
                    "signChangeDay": 10
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
            "coverFile": {},
            "productCancel": {},
            "productDelay": {},
            "productInfo": {
                "cnName": cnName,
                "cover": "1392028479466577921",
                "labelIds": [],
                "orgId": "1382572490914717698",
                "productType": 1,
                "period": "90",
                "productPeriodTypeIds": ["1387691661010006017", "1386229388521369601", "1384434377562828801",
                                         "1384406975113637889", "1384402317632647170", "1383022423526531074"],
                "productPeriodType": 1,
                "contractTemplateId": "1390924870624317441",
                "price": "299",
                "fnName": fnName
            },
            "productLesson": {
                "associatedType": 2,
                "productClassTypes": [{
                    "quantity": "",
                    "classTypeId": "1382587481826467841",
                    "isLimit": False
                }],
                "productSubjectCatalog": {
                    "productSubjectCatalogDetails": [{
                        "subjectCatalogId": "1382604729718874114",
                        "subjectCatalogCnName": "托业公开课（第一期）",
                        "quantity": ""
                    }, {
                        "subjectCatalogId": "1382933648615059457",
                        "subjectCatalogCnName": "第一单元",
                        "quantity": ""
                    }]
                }
            },
            "maxOrderClass": 4
        }

        products_response = request(method=products_method, url=products_url, headers=products_header,
                                    json=products_info).json()
        return products_response

    def put_product(self):
        """上架商品"""
        put_product_url = conf.get("service", "domain") + "/business/api/product-put-away"
        put_product_method = "post"
        put_product_header = {"Content-Type": "application/json",
                              "Authorization": "Bearer " + str(EnvData.access_token)}
        put_product_info = {
            "putAwayDetails": [{
                "productId": "1392046142846377985",
                "price": "299",
                "productPrice": 299,
                "quantity": 1,
                "productName": "接口新增商品"
            }],
            "putAwayInfoList": [{
                "isSend": 0,
                "promptly": True,
                "cnName": "接口上架商品01",
                "salePlatformId": "1382627501953564674",
                "productNumber": "TM202105120002",
                "salePlatformName": "天猫"
            }]
        }
        put_product_response = request(method=put_product_method, url=put_product_url, headers=put_product_header,
                                       json=put_product_info).json()
        return put_product_response


if __name__ == '__main__':
    web = HandleWeb()
    print(web.put_product())
