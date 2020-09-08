from selenium import webdriver
from config import settings
from frameworks.basePage import logger


class OpenBrowser:
    base_path = settings.drivers_path + '\\'

    def __init__(self, browser_name):
        try:
            if browser_name == 'chrome':
                drivers_path = self.base_path + 'chromedriver.exe'
                self.driver = webdriver.Chrome(executable_path=drivers_path)
                logger.info("open Chrome")
            elif browser_name == 'firefox':
                drivers_path = self.base_path+ 'geckodriver.exe'
                self.driver = webdriver.Firefox(executable_path=drivers_path)
                logger.info("open firefox")
            elif browser_name == 'IE':
                drivers_path = self.base_path + 'IEDriverServer.exe'
                self.driver = webdriver.Ie(executable_path=drivers_path)
                logger.info("open ie")
            else:
                open_error = Exception("wrong name!")
                raise open_error
        except Exception as e:
            logger.error("can't load driver, because: %s" % e)
