from conftest import driver
from metaclasses.meta_locator import MetaLocator
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data.links import Links

class BasePage(metaclass=MetaLocator):

    _DASHBOARD_MENU = "//a[contains(text(),'Dashboard')]"
    _DEALS_MENU = "//a[contains(text(),'Deals')]"
    _DEALS_URL = Links.DEALS_PAGE
    _DASHBOARD_URL = Links.DASHBOARD_PAGE

    def __init__(self, driver):
        self.driver :WebDriver= driver
        self._wait = WebDriverWait(self.driver, 10, 1)
        self._EC = EC

    def open(self):
        self.driver.get(self._PAGE_URL)
        assert self._wait.until(self._EC.url_to_be(self._PAGE_URL))

    def open_dashboard_from_menu(self):
        self._wait.until(self._EC.visibility_of_element_located(self._DASHBOARD_MENU), f"Элемент меню {self._DASHBOARD_MENU} недоступен").click()
        assert self._wait.until(self._EC.url_to_be(self._DASHBOARD_URL))

    def open_deals_from_menu(self):
        self._wait.until(self._EC.visibility_of_element_located(self._DEALS_MENU), f"Элемент меню {self._DEALS_MENU} недоступен").click()
        assert self._wait.until(self._EC.url_to_be(self._DEALS_URL))