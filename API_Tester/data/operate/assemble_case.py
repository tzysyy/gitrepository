#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   assemble_case.py
@Time    :   2020/12/15
@Author  :   yingjie
@Github :    https://github.com/WhiteMoonlights/API_Tester.git
@Contact :   ajie_jason@163.com
@Desc    :   将单条测试用例数据拼装成元组，再组成列表，供 pytest 框架读取
"""

from data.operate.get_excel_testcases import GetExcelTestcases
from data.operate.operate_excel import OperateExcel
from data.operate.produce_payload import ProducePayload


class AssembleCase():
    oe = OperateExcel()
    gt = GetExcelTestcases()
    pp = ProducePayload()
    case_list = []
    case_tuple = ()

    def assemble_case(self):
        rows = self.oe.get_sheet_nrows()
        for row in range(1, rows):
            is_run = self.gt.get_is_run(row)
            if is_run:
                url = self.gt.get_url(row)

                headers = self.gt.get_headers(row)
                method = self.gt.get_method(row)
                expr = self.gt.get_expr(row)
                expected_res = self.gt.get_expected(row)
                set_variable_path = self.gt.get_set_variable_path(row)
                set_variable_name = self.gt.get_set_variable_name(row)
                if set_variable_path:
                    set_variable_path = set_variable_path.split("&")
                if set_variable_name:
                    set_variable_name = set_variable_name.split("&")
                self.case_tuple = (url, headers, method, expr, expected_res, set_variable_path, set_variable_name, row, rows)
                self.case_list.append(self.case_tuple)
        return self.case_list

if __name__ == '__main__':
    ac = AssembleCase()
    print(ac.assemble_case())

