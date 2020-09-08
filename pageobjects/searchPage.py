from selenium.webdriver.common.by import By
from pageobjects.myAccountPage import MyAccountInfo
from frameworks.log import Logger

logger = Logger(logger='searchPage').getlog()


class SearchPage(MyAccountInfo):
    # 页面元素
    key_word = (By.XPATH, '/html/body/div[3]/div/section[1]')

    # 元素操作
    def get_key(self):
        self.wait(self.key_word, 5)
        text = self.get_text_info(self.key_word)
        logger.info('show text: %s' % text)
        return text
