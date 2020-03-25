import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from libs.newtour.main_page import MainPage


@pytest.fixture()
def firefox_driver():
    options = Options()
    options.headless = True
    firefox_driver = webdriver.Firefox(options=options)
    yield firefox_driver
    firefox_driver.quit()