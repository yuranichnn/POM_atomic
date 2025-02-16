from base.base_page import BasePage
from data.links import Links


class ContactPage(BasePage):

    _PAGE_URL = Links.CONTACT_PAGE

    _NEW_CONTACT_BUTTON = "//a[@aria-label='New Contact']"
    _NEW_CONTACT_URL = f"{_PAGE_URL}/create"
    _NEW_CONTACT_FORM = "//form"

    def open_modal_new_contact(self):
        self._wait.until(self._EC.visibility_of_element_located(self._NEW_CONTACT_BUTTON)).click()
        assert (self._wait.until(self._EC.url_to_be(self._NEW_CONTACT_URL)) and
                self._wait.until(self._EC.visibility_of_element_located(self._NEW_CONTACT_FORM)))




