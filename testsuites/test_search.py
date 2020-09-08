from pageobjects.searchPage import SearchPage
from testsuites.testBase import TestBase


class SearchTest(TestBase):
    def test_search_1(self):
        search = SearchPage(self.driver)
        search.open_url()
        search.click_log_button()
        search.account_input('x8494149x')
        search.pass_input('qweASD*963.')
        search.submit_btn()
        search.search_goods('苹果')
        search.click_search_button()
        text = search.get_key()
        self.assertIn('苹果', text, 'fail')

    def test_search_2(self):
        search1 = SearchPage(self.driver)
        search1.open_url()
        search1.click_log_button()
        search1.account_input('x8494149x')
        search1.pass_input('qweASD*963.')
        search1.submit_btn()
        search1.search_goods('梨子')
        search1.click_search_button()
        text = search1.get_key()
        self.assertIn('梨子', text, 'fail')

    def test_search_3(self):
        search2 = SearchPage(self.driver)
        search2.open_url()
        search2.click_log_button()
        search2.account_input('x8494149x')
        search2.pass_input('qweASD*963.')
        search2.submit_btn()
        search2.search_goods('小米')
        search2.click_search_button()
        text = search2.get_key()
        self.assertIn('小米', text, 'fail')
