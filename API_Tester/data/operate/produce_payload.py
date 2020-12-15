#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   produce_payload.py
@Time    :   2020/12/15
@Author  :   yingjie
@Github :    https://github.com/WhiteMoonlights/API_Tester.git
@Contact :   ajie_jason@163.com
@Desc    :   将从Excel读取到的API，PARAMS信息拼装为完整的请求参数信息
"""

import ast
from variable_setting.variable_setting import VariableSetting
import re


class ProducePayload():
    vs = VariableSetting()
    def produce_payload(self, api, params):
        matchobj = re.findall('\\$\\{\\w*\\}', params)
        if matchobj:
            for i in matchobj:
                key = re.findall("\\w+", i)
                value = self.vs.get_variable(key[0])
                params = re.sub('\\$\\{'+key[0]+'\\}', value, params)
                print(params)

        token = self.vs.get_variable("token")
        payload = f"""{{"apis" : '[{{"cid":"","api":"{api}","params":{params}}}]', "ctype" : "ADMIN.WEB", "TOKEN":"{token}"}}"""
        payload_json = ast.literal_eval(payload)
        return payload_json


if __name__ == '__main__':
    pp = ProducePayload()
    a = pp.produce_payload("sc/captcha/captcha","""{'userLoginname': 'YL029866', 'userLoginpwd': 'abc@123456','userMobile': '', 'userEmail': '', 'verify': '', 'captcha': {'captchaToken': '${captchaToken}', 'captchaValue': '${captchaValue}'}}""")
    print(a)