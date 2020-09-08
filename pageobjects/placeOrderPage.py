from selenium.webdriver.common.by import By
from pageobjects.goodsDetail import GoodsDetail
from frameworks.log import Logger

logger = Logger(logger='placeOrderPage').getlog()


class PlaceOrderPage(GoodsDetail):
    # 可操作元素
    place_order = (By.XPATH, '/html/body/div[3]/section[2]/form/label/span')

    # 元素方法：
    def click_place_order(self):
        self.wait(self.place_order, 5)
        self.click(self.place_order)
        logger.info('click place_order')
