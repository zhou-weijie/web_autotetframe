from selenium.webdriver.common.by import By
from pageobjects.placeOrderPage import PlaceOrderPage
from frameworks.log import Logger

logger = Logger(logger='successPlaceOrderPage').getlog()


class SuccessPlaceOrderPage(PlaceOrderPage):
    # 页面元素
    form_title = (By.XPATH, '/html/body/div[3]/section[2]/header')

    # 元素操作
    def get_info(self):
        self.wait(self.form_title, 5)
        text = self.get_text_info(self.form_title)
        logger.info('show text: %s' % text)
        return text
