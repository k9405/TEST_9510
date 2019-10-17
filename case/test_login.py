import json
import unittest
import requests
from parameterized import parameterized

import app
from api.test_login_api import LoginApi


def my_json():
    list1 = []
    with open(app.DATE_Url + "/data/loing.json", "r", encoding="utf-8") as f:
        msg = json.load(f)
        for i in msg.values():
            list1.append((i.get("mobile"),
                          i.get("password"),
                          i.get("success"),
                          i.get("code"),
                          i.get("message")))
    return list1


class BGLogin(unittest.TestCase):
    def setUp(self):
        self.session = requests.Session()
        self.login_api = LoginApi()

    def tearDown(self):
        self.session.close()

    @parameterized.expand(my_json())
    def test_login_succeed(self, mobile, password, success, code, message):
        response = self.login_api.loginapi(self.session, mobile, password)
        reult = response.json()
        print("登录返回数据:", reult)
        s1 = reult.get("success")
        c1 = reult.get("code")
        m1 = reult.get("message")

        self.assertEqual(success, s1)
        self.assertEqual(code, c1)
        self.assertIn(message, m1)

    def test_login_handle(self):
        response = self.login_api.loginapi(self.session, "13800000002", "123456")

        result = response.json()
        print("第二次登录返回数据:", result)
        s2 = result.get("success")
        c2 = result.get("code")
        m2 = result.get("message")

        self.assertEqual(True,s2)
        self.assertEqual(10000,c2)
        self.assertIn("操作成功",m2)

        app.TOKEN = result.get("data")
