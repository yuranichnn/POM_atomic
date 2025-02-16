from base.base_page import BasePage
from data.links import Links


class DashboardPage(BasePage):
    _PAGE_URL = Links.DASHBOARD_PAGE
    _HOT_CONTACT_BUTTON = "//a[contains(text(),'Hot contacts')]"
    _HOT_CONTACT_URL = Links.CONTACT_PAGE

    def hot_contact_click(self):
        self._wait.until(self._EC.visibility_of_element_located(self._HOT_CONTACT_BUTTON),
                         f"Элемент страницы {self._HOT_CONTACT_BUTTON} недоступен").click()

        assert self._wait.until(self._EC.url_to_be(self._HOT_CONTACT_URL))
