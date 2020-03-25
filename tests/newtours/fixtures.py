import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options


@pytest.fixture()
def firefox_driver():
    options = Options()
    options.headless = True
    firefox_driver = webdriver.Firefox(options=options)
    firefox_driver.get('http://newtours.demoaut.com/')
    yield firefox_driver
    firefox_driver.quit()
