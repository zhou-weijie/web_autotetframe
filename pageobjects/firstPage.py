from selenium.webdriver.common.by import By
from frameworks.basePage import BasePage
from frameworks.log import Logger

logger = Logger(logger="firstPage").getlog()


class FirstPage(BasePage):
    # 定位器
    log_button = (By.XPATH, '/html/body/header/div[1]/div/div[2]/div/a[1]')
    reg_button = (By.XPATH, '/html/body/header/div[1]/div/div[2]/div/a[2]')
    search_input = (By.XPATH, '/html/body/header/div[1]/div/div[4]/form/div/input')
    search_button = (By.XPATH, '/html/body/header/div[1]/div/div[4]/form/div/button')
    goods = (By.XPATH, '/html/body/div[3]/section[3]/div/div[2]/a[1]')

    # 元素操作
    def click_log_button(self):
        self.wait(self.log_button, 5)
        self.click(self.log_button)
        logger.info('click login_button')

    def click_reg_button(self):
        self.wait(self.reg_button, 5)
        self.click(self.reg_button)
        logger.info('click reg_button!')

    def search_goods(self, goods_name):
        self.wait(self.search_input, 5)
        self.send_keys(self.search_input, goods_name)

    def click_search_button(self):
        self.wait(self.search_button, 5)
        self.click(self.search_button)
        logger.info('click search_button!')

    def click_goods(self):
        self.wait(self.goods, 5)
        self.click(self.goods)
        logger.info('click goods!')
