#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   main_test.py
@Time    :   2020/12/15
@Author  :   yingjie
@Github :    https://github.com/WhiteMoonlights/API_Tester.git
@Contact :   ajie_jason@163.com
@Desc    :   测试执行
"""
from data.operate.assemble_case import AssembleCase
from data.operate.get_excel_testcases import GetExcelTestcases
from api_request.intergrate_requests import IntergrateRequest
from email_config.email_config import EmailConfig
from data.operate.operate_excel import OperateExcel
import jsonpath
from data.operate.produce_payload import ProducePayload
import pytest
import json

from variable_setting.variable_setting import VariableSetting


class TestExcelTestcases():

    gt = GetExcelTestcases()
    ir = IntergrateRequest()
    ec = EmailConfig()
    oe = OperateExcel()
    pp = ProducePayload()
    ac = AssembleCase()
    vs = VariableSetting()
    case_list = ac.assemble_case()
    pass_lists = []
    fail_lists = []

    @pytest.mark.parametrize("url, headers, method, expr, expected_res, set_variable_path, set_variable_name, row, rows", case_list)
    def test_runner(self, url, headers, method, expr, expected_res, set_variable_path, set_variable_name, row, rows):

        api = self.gt.get_api(row)
        params = self.gt.get_params(row)
        payload = self.pp.produce_payload(api, params)

        res = self.ir.main_req(method=method, url=url, data=payload, headers=headers)

        print("---------------------request----------------------------------")
        print(json.dumps(payload, indent=4, ensure_ascii=False, sort_keys=True))
        print("---------------------response---------------------------------")
        print(json.dumps(res, indent=4, ensure_ascii=False, sort_keys=True))

        actual_res = jsonpath.jsonpath(res, "$"+expr)[0]

        if actual_res == expected_res:
            self.gt.write_actual_result(row, "pass")
            self.pass_lists.append(row)
        else:
            self.gt.write_actual_result(row, "failed")
            self.fail_lists.append(row)
        if set_variable_path and set_variable_name:
            self.vs.set_variable(res, set_variable_path, set_variable_name)
            print(self.vs.oj.get_json())
        if row == self.case_list[-1][-2]:
            print("执行完毕")
            self.ec.send_mail(self.pass_lists, self.fail_lists)  #发邮件提醒


        assert actual_res == expected_res

if __name__ == '__main__':
    runner = TestExcelTestcases()
    runner.test_runner()
