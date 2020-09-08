from testsuites.testBase import TestBase
from pageobjects.successPlaceOrderPage import SuccessPlaceOrderPage


class TestPlaceOrder(TestBase):
    def test_palceorder(self):
        order = SuccessPlaceOrderPage(self.driver)
        order.open_url()
        order.click_log_button()
        order.account_input('x8494149x')
        order.pass_input('qweASD*963.')
        order.submit_btn()
        order.click_goods()
        order.click_buy_button()
        order.click_place_order()
        order.save_screenshot()
        text = order.get_info()
        self.assertEqual(text, '成功提交订单', 'fail')
