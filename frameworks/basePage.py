from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from config import settings
from frameworks.log import Logger
import time

# 创建一个日志实例
logger = Logger(logger="BasePage").getlog()


# 定义一个页面基类，所有页面郡继承该类
class BasePage:
    def __init__(self, driver):
        self.driver = driver

    # 打开url
    def open_url(self):
        self.driver.get(settings.URL)

    # 关闭浏览器
    def close_browser(self):
        self.driver.quit()

    # 刷新浏览器
    def flush_browser(self):
        self.driver.refresh()
        logger.info("Click refresh on current page.")

    # 后退
    def back_browser(self):
        self.driver.back()
        logger.info("Click back on current page.")

    # 前进
    def forward_browser(self):
        self.driver.forward()
        logger.info("Click forward on current page.")

    # 最大化窗口
    def max_window(self):
        self.driver.maximize_window()

    # 等待
    def wait(self, loc, seconds):
        try:
            wait_ = WebDriverWait(self.driver, seconds)
            wait_.until(lambda driver: driver.find_element(*loc))
            logger.info("wait for %d seconds." % seconds)
        except NameError as e:
            logger.error("Failed to load the element with %s" % e)

    # 找元素
    def find_element(self, loc):
        return self.driver.find_element(*loc)

    # 保存图片
    def save_screenshot(self):
        rq = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
        screen_name = settings.screen_path + '\\' + rq + '.png'
        try:
            self.driver.get_screenshot_as_file(screen_name)
            logger.info("Had take screenshot and save to folder : /screenshots")
        except NameError as e:
            logger.error("Failed to take screenshot! %s" % e)
            self.save_screenshot()

    # 输入事件
    def send_keys(self, selector, text):
        el = self.find_element(selector)
        el.clear()
        try:
            el.send_keys(text)
            logger.info("Had type \' %s \' in inputBox" % text)
        except NameError as e:
            logger.error("Failed to select in input box with %s" % e)
            self.save_screenshot()

    # 点击事件
    def click(self, selector):
        el = self.find_element(selector)
        try:
            el.click()
            logger.info("The element \'%s\' was clicked." % el)
        except NameError as e:
            logger.error("Failed to click the element with %s" % e)
            self.save_screenshot()

    # 鼠标事件点击
    def mouse_click(self, selector):
        el = self.find_element(selector)
        try:
            ActionChains(self.driver).click(el).release(el).perform()
            logger.info("The element \'%s\' was clicked." % el)
        except Exception as e:
            logger.error("Failed to click the element with %s" % e)
            self.save_screenshot()

    # 隐式等待
    def im_wait(self, sec):
        self.driver.implicitly_wait(sec)

    # 获取元素文本信息
    def get_text_info(self,loc):
        el = self.find_element(loc)
        try:
            text = el.text
            logger.info("Get text information:' %s ' successfully !!" % text)
        except NameError:
            logger.error("can't find such element：%s" % el)
            self.save_screenshot()
        else:
            return text

    # 全局等待
    @staticmethod
    def sleep(seconds):
        time.sleep(seconds)
        logger.info("Sleep for %d seconds" % seconds)
