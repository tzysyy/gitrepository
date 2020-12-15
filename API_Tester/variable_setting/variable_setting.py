#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   variable_setting.py
@Time    :   2020/12/15
@Author  :   yingjie
@Github :    https://github.com/WhiteMoonlights/API_Tester.git
@Contact :   ajie_jason@163.com
@Desc    :   设置以及读取变量
"""

from data.operate.operate_json import OperateJson
import time
import jsonpath


class VariableSetting():
    oj = OperateJson()
    def set_variable(self, res, path_list, name_list):
        for i in range(len(path_list)):
            value = jsonpath.jsonpath(res, "$" + path_list[i])[0]
            name = name_list[i]
            data = {name:value}
            self.oj.append_json(data)

    def get_variable(self, key):
        value = self.oj.get_json()[key]
        return value



if __name__ == '__main__':
    vs = VariableSetting()
    vs.set_variable("token", "123456789")
    # time.sleep(2)
    print(vs.oj.get_json())
    print(vs.get_variable("token"))
