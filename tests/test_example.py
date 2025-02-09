import time

from base.base_test import BaseTest

class TestExample(BaseTest):


    def test_example(self):
        self.dashboard_page.open()
        self.dashboard_page.hot_contact_click()
        self.contact_page.open_modal_new_contact()
