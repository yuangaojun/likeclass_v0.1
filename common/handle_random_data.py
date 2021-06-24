# -*- coding:utf-8 -*-
"""
==============================
Author:yuan
Time  :2021/4/21 22:57
file  :handle_random_data.py
===============================
"""
import datetime
import random
import time

from common.handle_config import conf
from common.handle_sql import HandlerMysql


class RandomData():
    db = HandlerMysql()

    def random_user(self):
        '''随机生成未注册的用户名'''
        while True:
            user = 'yuan'
            for i in range(8):
                r = random.randint(0, 9)
                user += str(r)
            sql = 'select * from test.auth_user where username = "{}";'.format(user)
            res = self.db.find_count(sql)
            if res == 0:
                return user

    def random_fith_user(self):
        '''随机生成未注册的用户名长度等于5'''
        while True:
            user = 'y'
            for i in range(4):
                r = random.randint(0, 9)
                user += str(r)
            sql = 'select * from test.auth_user where username = "{}";'.format(user)
            res = self.db.find_count(sql)
            if res == 0:
                return user

    def random_user_max_20(self):
        '''随机生成未注册的用户名长度大于20位'''
        while True:
            user = 'yuan'
            for i in range(18):
                r = random.randint(0, 9)
                user += str(r)
            sql = 'select * from test.auth_user where username = "{}";'.format(user)
            res = self.db.find_count(sql)
            if res == 0:
                return user

    def random_six_user(self):
        '''随机生成未注册的用户名六位'''
        while True:
            user = 'yu'
            for i in range(5):
                r = random.randint(0, 9)
                user += str(r)
            sql = 'select * from test.auth_user where username = "{}";'.format(user)
            res = self.db.find_count(sql)
            if res == 0:
                return user

    def random_number(self):
        '''随机生成未注册的用户名纯数字'''
        while True:
            user = ''
            for i in range(8):
                r = random.randint(1, 9)
                user += str(r)
            sql = 'select * from test.auth_user where username = "{}";'.format(user)
            res = self.db.find_count(sql)
            if res == 0:
                return user

    def random_eamil(self):
        '''随机生成未注册的用户名'''
        while True:
            email = 'yuan'
            for i in range(8):
                r = random.randint(0, 9)
                email = email + str(r)
            email += '@qq.com'
            sql = 'select * from test.auth_user where email = "{}";'.format(email)
            res = self.db.find_count(sql)
            if res == 0:
                return email

    def random_project(self):
        '''随机生成新建的项目名'''
        while True:
            project_name = '你在哪里'
            for i in range(8):
                r = random.randint(1, 9)
                project_name += str(r)
            sql = 'select * from test.tb_projects where name = "{}";'.format(project_name)
            res = self.db.find_count(sql)
            if res == 0:
                return project_name

    def random_project_200(self):
        '''随机生成新建的项目名长度等于200'''
        while True:
            project_name = '这是项目名称项目名称这是项目名称项目名称这是项目名称项目名称这是项目名称项目名称这是项目名称项目名称这是项目名称项目名称这是项目名称项目名称这是项目名称项目名称这是项目名称项目名称这是项目名称项目名称这是项目名称项目名称这是项目名称项目名称这是项目名称项目名称这是项目名称项目名称这是项目名称项目名称这是项目名称项目名称这是项目名称项目名称这是项目名称项目名称这是项目名称项目名称二百'
            for i in range(8):
                r = random.randint(1, 9)
                project_name += str(r)
            sql = 'select * from test.tb_projects where name = "{}";'.format(project_name)
            res = self.db.find_count(sql)
            if res == 0:
                return project_name

    def random_project_max_200(self):
        '''随机生成新建的项目名长度大于200'''
        while True:
            project_name = '这是项目名称项目名称这是项目名称项目名称这是项目名称项目名称这是项目名称项目名称这是项目名称项目名称这是项目名称项目名称这是项目名称项目名称这是项目名称项目名称这是项目名称项目名称这是项目名称项目名称这是项目名称项目名称这是项目名称项目名称这是项目名称项目名称这是项目名称项目名称这是项目名称项目名称这是项目名称项目名称这是项目名称项目名称这是项目名称项目名称这是项目名称项目大于二百的'
            for i in range(8):
                r = random.randint(1, 9)
                project_name += str(r)
            sql = 'select * from test.tb_projects where name = "{}";'.format(project_name)
            res = self.db.find_count(sql)
            if res == 0:
                return project_name

    def random_jiekou_name(self):
        '''随机生成新建的接口名'''
        while True:
            interfaces_name = '接口名称'
            for i in range(8):
                r = random.randint(1, 9)
                interfaces_name += str(r)
            sql = 'select * from test.tb_interfaces where name = "{}";'.format(interfaces_name)
            res = self.db.find_count(sql)
            if res == 0:
                return interfaces_name

    def random_testcase_name(self):
        '''随机生成新建的测试用例名'''
        while True:
            testcases_name = '用例名称'
            for i in range(8):
                r = random.randint(1, 9)
                testcases_name += str(r)
            sql = 'select * from test.tb_testcases where name = "{}";'.format(testcases_name)
            res = self.db.find_count(sql)
            if res == 0:
                return testcases_name

    def random_testcase_name_50(self):
        '''随机生成新建的测试用例名长度等于50'''
        while True:
            testcases_name = '用例名称长度等于50'
            for i in range(40):
                r = random.randint(1, 9)
                testcases_name += str(r)
            sql = 'select * from test.tb_testcases where name = "{}";'.format(testcases_name)
            res = self.db.find_count(sql)
            if res == 0:
                return testcases_name

    def random_testcase_name_max_50(self):
        '''随机生成新建的测试用例名长度大于50'''
        while True:
            testcases_name = '用例名称长度大于50'
            for i in range(41):
                r = random.randint(1, 9)
                testcases_name += str(r)
                # sql = 'select * from test.tb_testcases where name = "{}";'.format(testcases_name)
                # res = self.db.find_count(sql)
                # if res == 0:
                return testcases_name

    def random_product_cnname(self):
        '''随机生成商品中文名'''
        while True:
            cnname = "自动化-商品中文名称"
            for i in range(1, 9):
                r = random.randint(1, 9)
                cnname += str(r)
            sql = "select * from lks_business.product where cn_name = '{}';".format(cnname)
            res = self.db.find_count(sql)
            if res == 0:
                return cnname

    def random_product_fnname(self):
        '''随机生成商品外文名'''
        while True:
            fnname = "自动化-商品外文名称"
            for i in range(1, 9):
                r = random.randint(1, 9)
                fnname += str(r)
            sql = "select * from lks_business.product where fn_name = '{}';".format(fnname)
            res = self.db.find_count(sql)
            if res == 0:
                return fnname

    def random_sale_product_number(self, sale_plateform):
        '''随机生成销售平台商品编号'''
        while True:
            now_time = time.strftime('%Y%m%d', time.localtime(time.time()))
            if sale_plateform == "天猫":
                sale_product_number = "TM" + str(now_time)
                for i in range(6):
                    r = random.randint(0, 9)
                    sale_product_number += str(r)
                sql = "select * from lks_business.product_putaway where product_number = '{}';".format(
                    sale_product_number)
                res = self.db.find_count(sql)
                if res == 0:
                    return sale_product_number
            elif sale_plateform == "京东":
                sale_product_number = "JD" + str(now_time)
                for i in range(6):
                    r = random.randint(0, 9)
                    sale_product_number += str(r)
                sql = "select * from lks_business.product_putaway where product_number = '{}';".format(
                    sale_product_number)
                res = self.db.find_count(sql)
                if res == 0:
                    return sale_product_number
            elif sale_plateform == "淘宝":
                sale_product_number = "TB" + str(now_time)
                for i in range(6):
                    r = random.randint(0, 9)
                    sale_product_number += str(r)
                sql = "select * from lks_business.product_putaway where product_number = '{}';".format(
                    sale_product_number)
                res = self.db.find_count(sql)
                if res == 0:
                    return sale_product_number
            elif sale_plateform == "微盟":
                sale_product_number = "WM" + str(now_time)
                for i in range(6):
                    r = random.randint(0, 9)
                    sale_product_number += str(r)
                sql = "select * from lks_business.product_putaway where product_number = '{}';".format(
                    sale_product_number)
                res = self.db.find_count(sql)
                if res == 0:
                    return sale_product_number
            else:
                return "销售平台不存在，请检查！"

    def random_saleplatform_orderno(self, sale_plateform):
        '''随机生成售卖平台订单编号'''
        while True:
            now_time = time.strftime('%Y%m%d', time.localtime(time.time()))
            if sale_plateform == "天猫":
                sale_plateform_orderno = "TM" + str(now_time)
                for i in range(9):
                    r = random.randint(0, 9)
                    sale_plateform_orderno += str(r)
                sql = "select * from lks_business.order where sale_platform_order_number = '{}';".format(
                    sale_plateform_orderno)
                res = self.db.find_count(sql)
                if res == 0:
                    return sale_plateform_orderno
            elif sale_plateform == "京东":
                sale_plateform_orderno = "JD" + str(now_time)
                for i in range(6):
                    r = random.randint(0, 9)
                    sale_plateform_orderno += str(r)
                sql = "select * from lks_business.order where sale_platform_order_number = '{}';".format(
                    sale_plateform_orderno)
                res = self.db.find_count(sql)
                if res == 0:
                    return sale_plateform_orderno
            elif sale_plateform == "淘宝":
                sale_plateform_orderno = "TB" + str(now_time)
                for i in range(6):
                    r = random.randint(0, 9)
                    sale_plateform_orderno += str(r)
                sql = "select * from lks_business.order where sale_platform_order_number = '{}';".format(
                    sale_plateform_orderno)
                res = self.db.find_count(sql)
                if res == 0:
                    return sale_plateform_orderno
            elif sale_plateform == "微盟":
                sale_plateform_orderno = "WM" + str(now_time)
                for i in range(6):
                    r = random.randint(0, 9)
                    sale_plateform_orderno += str(r)
                sql = "select * from lks_business.order where sale_platform_order_number = '{}';".format(
                    sale_plateform_orderno)
                res = self.db.find_count(sql)
                if res == 0:
                    return sale_plateform_orderno
            else:
                return "销售平台不存在，请检查！"

    def later_now_time(self):
        '''返回未匹配成功的时间'''
        hours = 0
        while True:
            later_now_time = (datetime.datetime.now() + datetime.timedelta(hours=hours + 1)).strftime(
                "%Y-%m-%d %H:00:00")
            time1 = (datetime.datetime.now() + datetime.timedelta(hours=hours + 2)).strftime("%Y-%m-%d %H:00:00")
            teacher_requirement_status_sql = """select * from lks_teaching.teacher_requirement 
            where teacher_id = (select id from lks_teaching.teacher where mobile = (
            select mobile from lks_teaching.teacher where fn_name = '{}')) and requirement_status = 2 
            and time between '{}' and '{}' order by create_time desc;""".format(
                conf.get("case_data", "teacher_username"),
                later_now_time, time1)
            teacher_requirement_status = self.db.find_count(teacher_requirement_status_sql)
            if teacher_requirement_status <= 0:
                return later_now_time
            else:
                hours += 1

    def earlier_now_time(self):
        '''当前时间-1小时，早于当前时间'''
        earlier_now_time = (datetime.datetime.now() + datetime.timedelta(hours=-1)).strftime("%Y-%m-%d %H:00:00")
        return earlier_now_time

    def teacher_course_time(self):
        '''返回教师可预定课时间'''
        hours = 0
        while True:
            later_now_time = (datetime.datetime.now() + datetime.timedelta(hours=hours + 1)).strftime(
                "%Y-%m-%d %H:00:00")
            time1 = (datetime.datetime.now() + datetime.timedelta(days=hours + 2)).strftime("%Y-%m-%d %H:00:00")
            teacher_requirement_status_sql = """select * from lks_teaching.teacher_requirement 
            where teacher_id = (select id from lks_teaching.teacher where mobile = (
            select mobile from lks_teaching.teacher where fn_name = '{}')) and requirement_status = 1 
             and time between '{}' and '{}' order by create_time desc limit 1;""".format(
                conf.get("case_data", "teacher_username"), later_now_time, time1)
            student_course_time = self.db.find_one(teacher_requirement_status_sql)["time"]
            return student_course_time


if __name__ == '__main__':
    ran = RandomData()
    # print(ran.random_parodut_cnname())
    print(ran.later_now_time())
    print(ran.student_course_time())
