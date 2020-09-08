from pageobjects.myAccountPage import MyAccountInfo
from testsuites.testBase import TestBase
from pageobjects.loginPage import Login


class LoginTest(TestBase):
    def test_right_login(self):
        login = MyAccountInfo(self.driver)
        login.open_url()
        login.click_log_button()
        login.account_input('x8494149x')
        login.pass_input('qweASD*963.')
        login.submit_btn()
        user_text = login.get_user_text()
        self.assertEqual(user_text, 'x8494149x', 'fail')

    def test_wrong_login_01(self):
        login = Login(self.driver)
        login.open_url()
        login.click_log_button()
        login.account_input('x8494149')
        login.pass_input('qweASD*963.')
        login.submit_btn()
        text = login.get_text()
        self.assertEqual(text, '账号或密码错误', 'fail')

    def test_wrong_login_02(self):
        login = Login(self.driver)
        login.open_url()
        login.click_log_button()
        login.account_input('x8494149x')
        login.pass_input('qweASD')
        login.submit_btn()
        text = login.get_text()
        self.assertEqual(text, '账号或密码错误', 'fail')
