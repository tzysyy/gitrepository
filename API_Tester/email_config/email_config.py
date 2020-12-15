#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   email_config.py
@Time    :   2020/12/15
@Author  :   yingjie
@Github :    https://github.com/WhiteMoonlights/API_Tester.git
@Contact :   ajie_jason@163.com
@Desc    :   发送邮件配置
"""

import smtplib
from email.mime.text import MIMEText

class EmailConfig(object):

    global send_user
    global mail_host
    global password

    send_user = '1185726255@qq.com'
    mail_host = 'smtp.qq.com'
    password = 'xryvsplhqaxqhaaf'

    def send_config(self, user_lists, subject, content):
        user = "海阔天空" + "<" + send_user + ">"
        message = MIMEText(content, _subtype="plain", _charset="utf-8")
        message["Subject"] = subject
        message["From"] = send_user
        message["To"] = ";".join(user_lists)

        server = smtplib.SMTP()
        server.connect(mail_host)
        server.login(send_user, password)
        server.sendmail(user, user_lists, message.as_string())
        server.close()

    def send_mail(self, pass_cases, fail_cases):
        pass_count = int(len(pass_cases))
        fail_count = int(len(fail_cases))
        # execute_count = pass_count + fail_count
        # not_execute_count = int(len(not_execute_cases))
        total_count = pass_count + fail_count
        pass_ratio = f"{pass_count / total_count * 100}%"

        user_lists = ["tzy_fly@163.com"]
        subject = "自动化测试完成提醒"
        content = f"测试完成，本次测试共执行{total_count}条用例，通过{pass_count}条，失败{fail_count}条，通过率为{pass_ratio}"
        self.send_config(user_lists, subject, content)

if __name__ == "__main__":
    ec = EmailConfig()
    ec.send_mail([1, 3, 5, 7, 9, 10, 11, 12, 13, 14, 15], [2, 4, 6])