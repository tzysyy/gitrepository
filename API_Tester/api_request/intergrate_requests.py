#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
@File    :   intergrate_requests.py
@Time    :   2020/12/15
@Author  :   yingjie
@Github :    https://github.com/WhiteMoonlights/API_Tester.git
@Contact :   ajie_jason@163.com
@Desc    :   请求方法集合
"""

import requests
import json

class IntergrateRequest():
    def get_req(self, url, data=None, headers=None):
        res = requests.get(url=url, data=data, headers=headers)
        return res

    def post_req(self, url, data=None, headers=None):
        res = requests.post(url=url, data=data, headers=headers)
        return res

    def delete_req(self, url, data=None, headers=None):
        res = requests.delete(url=url, data=data, headers=headers)
        return res

    def main_req(self, method, url, data=None, headers=None):
        if method == "get":
            res = self.get_req(url, data, headers)
        elif method == "post":
            res = self.post_req(url, data, headers)
        elif method == "delete":
            res = self.delete_req(url, data, headers)
        else:
            return "请求方式暂未开放，敬请期待"

        # return json.dumps(res.json(), indent=4, ensure_ascii=False, sort_keys=True)
        return res.json()



if __name__ == '__main__':
    url = "http://umsatest.niceloo.com/api/"
    params = {"apis" : '[{"cid":"","api":"sc/captcha/captcha","params":{"scene":"uc_login"}}]', "ctype" : "ADMIN.WEB"}
    ir = IntergrateRequest()
    res = ir.main_req(method="post", url=url, data=params)
    print(json.dumps(res, indent=4, ensure_ascii=False, sort_keys=True))






