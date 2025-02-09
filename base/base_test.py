from pages.dashboard_page import DashboardPage
from pages.contact_page import ContactPage


class BaseTest:

    def setup_method(self):
        self.dashboard_page = DashboardPage(self.driver)
        self.contact_page = ContactPage(self.driver)

