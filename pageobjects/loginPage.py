from pageobjects.firstPage import FirstPage
from selenium.webdriver.common.by import By
from frameworks.log import Logger

logger = Logger(logger="loginPage").getlog()


class Login(FirstPage):
    # 定位器
    user_account = (By.XPATH, '/html/body/div[3]/section/section/form/dl[1]/dd/input')
    user_pass = (By.XPATH, '/html/body/div[3]/section/section/form/dl[2]/dd/input')
    login_button = (By.XPATH, '/html/body/div[3]/section/section/form/dl[5]/dd/input')
    login_info = (By.XPATH, '/html/body/div[3]/section/section/form/div')

    def account_input(self, account):
        self.wait(self.user_account, 5)
        self.send_keys(self.user_account, account)

    def pass_input(self, password):
        self.wait(self.user_pass, 5)
        self.send_keys(self.user_pass, password)

    def submit_btn(self):
        self.click(self.login_button)
        logger.info("show results!")
        self.sleep(2)

    def get_text(self):
        self.wait(self.login_info, 5)
        text = self.get_text_info(self.login_info)
        logger.info('show text: %s' % text)
        return text
