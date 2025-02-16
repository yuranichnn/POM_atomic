import time

from base.base_test import BaseTest

class TestExample(BaseTest):


    def test_menu(self):
        self.dashboard_page.open()
        self.dashboard_page.open_deals_from_menu()
        self.dashboard_page.open_dashboard_from_menu()

    def test_example_1(self):
        self.dashboard_page.open()
        self.dashboard_page.hot_contact_click()
        self.contact_page.open_modal_new_contact()

    def test_example_2(self):
        self.contact_page.open()
        self.contact_page.open_modal_new_contact()
        self.contact_page.open_dashboard_from_menu()
