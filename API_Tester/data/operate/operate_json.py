#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   operate_json.py
@Time    :   2020/12/15
@Author  :   yingjie
@Github :    https://github.com/WhiteMoonlights/API_Tester.git
@Contact :   ajie_jason@163.com
@Desc    :   提供Json文件的读取、追加写入操作方法
"""

import json
import os

class OperateJson():
    def __init__(self, filename = None):
        if filename:
            self.filename = filename
        else:
            dir_name = os.path.dirname(os.path.dirname(__file__)) + r"\cases_data\variable.json"
            self.filename = dir_name
        self.data = self.get_json()

    def get_json(self):
        with open(self.filename, encoding="utf-8") as fp:
            data = json.load(fp)
        return data

    def append_json(self, json_dict):
        copy_dict = self.get_json()
        copy_dict.update(json_dict)
        with open(self.filename, "w", encoding="utf-8") as fp:
            json.dump(copy_dict, fp, indent=4, ensure_ascii=False, sort_keys=True)



if __name__ == '__main__':
    oj = OperateJson()
    oj.append_json({"a":"5"})
    oj.get_json()
    print(oj.get_json())