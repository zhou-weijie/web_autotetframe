import unittest
from HTMLTestRunner import HTMLTestRunner
import time
import os
from config import settings
# 定义输出的文件位置和名字
# DIR = os.path.dirname(os.path.abspath(__file__))
now = time.strftime("%Y%m%d%H%M", time.localtime(time.time()))
report_path = settings.report_path + '\\'
filename = now + "report.html"
# discover方法执行测试套件
testsuite = unittest.defaultTestLoader.discover(
    settings.case_path,
    pattern='test_*',
    top_level_dir=None
)

with open(report_path + filename, 'w+', encoding='utf-8') as f:
    runner = HTMLTestRunner(
        stream=f,
        verbosity=2,
        title='开源商城系统测试报告',
        description='执行情况'
    )
    runner.run(testsuite)