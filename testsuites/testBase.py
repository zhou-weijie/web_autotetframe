import unittest
from selenium import webdriver
from frameworks.openBrowser import OpenBrowser
from config import settings


class TestBase(unittest.TestCase):
    def setUp(self):
        # self.driver = OpenBrowser(settings.browser_name)  # 驱动浏览器
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
