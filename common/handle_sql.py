# -*- coding:utf-8 -*-
"""
==============================
Author:yuan
Time  :2021/4/22 13:42
file  :handle_sql.py
===============================
"""
import pymysql
from common.handle_config import conf


class HandlerMysql():
    '''数据库操作封装'''

    def __init__(self):
        '''初始化连接数据库'''
        self.mysql = pymysql.connect(host=conf.get('database', 'host'),
                                     port=eval(conf.get('database', 'port')),
                                     user=conf.get('database', 'user'),
                                     password=conf.get('database', 'password'),
                                     charset='utf8',
                                     cursorclass=pymysql.cursors.DictCursor
                                     )
        self.cur = self.mysql.cursor()

    def find_one(self, sql):
        '''
        查询数据库并返回一条数据
        :param sql:需要执行的算sql语句
        :return:查询语句的一条信息
        '''
        self.mysql.ping(reconnect=True)
        self.mysql.commit()
        self.cur.execute(sql)
        return self.cur.fetchone()

    def find_all(self, sql):
        '''
        查询数据库返回所有的数据
        :param sql: 需要执行的查询sql语句
        :return: sql查询出来的所有信息
        '''
        self.mysql.ping(reconnect=True)
        self.mysql.commit()
        self.cur.execute(sql)
        return self.cur.fetchall()

    def find_count(self, sql):
        '''查询语句的查询条数'''
        self.mysql.ping(reconnect=True)
        self.mysql.commit()
        res = self.cur.execute(sql)
        return res

    def update(self, sql):
        '''
        更新数据库
        :param sql:需要更新数据库表信息的语句
        :return:
        '''
        self.mysql.ping(reconnect=True)
        self.mysql.commit()
        self.cur.execute(sql)
        return self.mysql.commit()

    def close(self):
        '''断开连接'''
        self.cur.close()
        self.mysql.close()


if __name__ == '__main__':
    mysql = HandlerMysql()
    print(mysql.find_one('select * from lks_business.product where cn_name = "测试0.1";'))
