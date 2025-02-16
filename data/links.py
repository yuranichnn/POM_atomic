import os

class Links:
    HOST = f"https://{os.environ["LAYER"].lower()}-crm.qa-playground.com"
    DASHBOARD_PAGE = f"{HOST}/#/"
    CONTACT_PAGE = f"{HOST}/#/contacts"
    DEALS_PAGE = f"{HOST}/#/deals"