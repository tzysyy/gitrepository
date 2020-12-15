#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   get_excel_testcases.py
@Time    :   2020/12/15
@Author  :   yingjie
@Github :    https://github.com/WhiteMoonlights/API_Tester.git
@Contact :   ajie_jason@163.com
@Desc    :   根据测试用例的行数，读取测试用例某字段对应的值
"""

from data.operate.operate_excel import OperateExcel
from data.operate import testcases_keyword
from data.operate.testcases_keyword import TestcasesKeyword


class GetExcelTestcases():
    def __init__(self):
        self.oe = OperateExcel()
        self.tk = TestcasesKeyword()
    def get_is_run(self, row):
        col = self.tk.get_is_execute()
        is_run = self.oe.get_sheet_cell(row, col)
        if is_run:
            flag = True
        else:
            flag = False
        return flag
    def get_url(self, row):
        col = self.tk.get_interface_url()
        url = self.oe.get_sheet_cell(row, col)
        return url

    def get_api(self, row):
        col = self.tk.get_api()
        api = self.oe.get_sheet_cell(row, col)
        return api

    def get_params(self, row):
        col = self.tk.get_params()
        params = self.oe.get_sheet_cell(row, col)
        # params = ast.literal_eval(params)
        return params

    def get_headers(self, row):
        col = self.tk.get_header()
        headers = self.oe.get_sheet_cell(row, col)
        return headers

    def get_method(self, row):
        col = self.tk.get_method()
        method = self.oe.get_sheet_cell(row, col)
        return method

    def get_id(self, row):
        col = self.tk.get_case_id()
        case_id = self.oe.get_sheet_cell(row, col)
        return case_id

    def get_expected(self, row):
        col = self.tk.get_expected_result()
        expected = self.oe.get_sheet_cell(row, col)
        return expected

    def get_expr(self, row):
        col = self.tk.get_expr()
        expr = self.oe.get_sheet_cell(row, col)
        return expr

    def write_actual_result(self, row, values):
        col = self.tk.get_actual_result()
        self.oe.write_to_excel(row, col, values)

    def get_set_variable_path(self, row):
        col = self.tk.get_set_variable_path()
        path = self.oe.get_sheet_cell(row, col)
        return path

    def get_set_variable_name(self, row):
        col = self.tk.get_set_variable_name()
        name = self.oe.get_sheet_cell(row, col)
        return name



if __name__ == '__main__':
    gt = GetExcelTestcases()
    print(gt.get_params(1))
    print(type(gt.get_params(1)))
