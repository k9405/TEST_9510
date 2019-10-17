import unittest
import requests

import app
from api.test_handle_api import HandleEmp


class HandleBg(unittest.TestCase):
    def setUp(self):
        self.session = requests.Session()
        self.HEmp = HandleEmp()

    def tearDown(self):
        self.session.close()

    def test_1_add_emp(self):
        result2 = self.HEmp.add(self.session, "aote1266", "12221423666", "753126")

        print("添加员工数据:", result2.json())

        app.ID = result2.json().get("data").get("id")

    def test_2_get_emp(self):
        result3 = self.HEmp.get_emp(self.session)
        print("查看员工数据:", result3.json())

    def test_3_alter_emp(self):
        result4 = self.HEmp.alter_emp(self.session,"aoteman777","15990061234")
        print("修改员工数据: ", result4.json())

    def test_4_del_emp(self):
        result5 = self.HEmp.del_emp(self.session)
        print("删除员工数据:", result5.json())


