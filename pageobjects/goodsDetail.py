# 商品详情页
from selenium.webdriver.common.by import By
from pageobjects.loginPage import Login
from frameworks.log import Logger

logger = Logger(logger='goodsPage').getlog()


class GoodsDetail(Login):
    # 可操作元素
    buy_button = (By.XPATH, '//*[@id="buyNowButton"]/span')

    # 元素方法
    def click_buy_button(self):
        self.wait(self.buy_button, 5)
        self.click(self.buy_button)
        logger.info('click buy_button!')
