#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   testcases_keyword.py
@Time    :   2020/12/15
@Author  :   yingjie
@Github :    https://github.com/WhiteMoonlights/API_Tester.git
@Contact :   ajie_jason@163.com
@Desc    :   定义以及获取测试用例字段所在列
"""

class TestcasesKeyword():
    CASE_ID = 0
    CASE_TITLE = 1
    IS_EXECUTE = 2
    INTERFACE_URL = 3
    API = 4
    PARAMS = 5
    HEADER = 6
    METHOD = 7
    EXPR = 8
    EXPECTED_RESULT = 9
    ACTUAL_RESULT = 10
    SET_VARIABLE_PATH = 11
    SET_VARIABLE_NAME = 12


    def get_case_id(self):
        return self.CASE_ID

    def get_case_title(self):
        return self.CASE_TITLE

    def get_is_execute(self):
        return self.IS_EXECUTE

    def get_interface_url(self):
        return self.INTERFACE_URL

    def get_method(self):
        return self.METHOD

    def get_header(self):
        return self.HEADER

    def get_api(self):
        return self.API

    def get_params(self):
        return self.PARAMS

    def get_expected_result(self):
        return self.EXPECTED_RESULT

    def get_actual_result(self):
        return self.ACTUAL_RESULT

    def get_expr(self):
        return self.EXPR

    def get_set_variable_path(self):
        return self.SET_VARIABLE_PATH

    def get_set_variable_name(self):
        return self.SET_VARIABLE_NAME

if __name__ == '__main__':
    print(TestcasesKeyword().get_case_id())