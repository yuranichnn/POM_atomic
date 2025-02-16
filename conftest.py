import os

import pytest
from selenium import webdriver

@pytest.fixture(autouse=True)
def driver(request):
    if os.environ["BROWSER"].lower() == "chrome":
        driver = webdriver.Chrome()
        request.cls.driver = driver
        yield
        driver.quit()
    elif os.environ["BROWSER"].lower() == "firefox":
        driver = webdriver.Firefox()
        request.cls.driver = driver
        yield
        driver.quit()