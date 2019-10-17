import unittest

import time

import app
from Tools.HTMLTestRunner import HTMLTestRunner

from case.test_handle import HandleBg
from case.test_login import BGLogin

suite = unittest.TestSuite()

suite.addTest(BGLogin("test_login_handle"))
suite.addTest(HandleBg("test_1_add_emp"))
suite.addTest(HandleBg("test_2_get_emp"))
suite.addTest(HandleBg("test_3_alter_emp"))
suite.addTest(HandleBg("test_4_del_emp"))

file = "./report/report1996"
with open(file + ".html","wb") as f:

    runner = HTMLTestRunner(f, title="我的报告", description="chrome")

    runner.run(suite)
