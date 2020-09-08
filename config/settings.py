import os

# 获取当前项目的根目类
# os.path.abspath(__file__)是获取当前文件的绝对路径，摆正斜杠
# os.path.dirname()是获取所在文件夹的路径
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 定义访问的url
URL = 'http://shop.aircheng.com/site/index'

# 拼接出driver所在的文件夹路径
drivers_path = os.path.join(BASE_DIR, 'drivers')

# 拼接出日志所在的文件夹路径
log_path = os.path.join(BASE_DIR, 'logs')

# 拼接出截图所在的路径
screen_path = os.path.join(BASE_DIR, 'screenshots')

# 拼接出测试报告所在的路径
report_path = os.path.join(BASE_DIR, 'test_report')

# 拼接出测试数据所在的的路径
data_path = os.path.join(BASE_DIR, 'data')

# 设置打开的浏览器名称
browser_name = 'chrome'

# 用例所在目录
case_path = os.path.join(BASE_DIR, 'testsuites')
