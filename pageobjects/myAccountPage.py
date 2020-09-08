from selenium.webdriver.common.by import By
from pageobjects.loginPage import Login
from frameworks.log import Logger

logger = Logger(logger='myAccountPage').getlog()


class MyAccountInfo(Login):
    # 元素信息
    user_info = (By.XPATH, '/html/body/header/div[1]/div/div[2]/div[1]/a')

    def get_user_text(self):
        self.wait(self.user_info, 5)
        text = self.get_text_info(self.user_info)
        logger.info('show text: %s' % text)
        return text
