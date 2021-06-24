# -*- coding:utf-8 -*-
"""
==============================
Author:yuan
Time  :2021/4/19 12:36
file  :handle_assert.py
===============================
"""


class AsserTion():
    '''自定义断言'''

    def custom_assert(self, expected, res):
        for key in expected:
            if key in res.keys() and expected[key] == res[key]:
                return True
            else:
                return False
