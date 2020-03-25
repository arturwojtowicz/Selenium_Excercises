import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options


@pytest.fixture
def firefox_driver():
    options = Options()
    options.headless = True
    return webdriver.Firefox(options=options)


@pytest.fixture
def newtours_on_firefox(firefox_driver):
    firefox_driver.get('http://newtours.demoaut.com/')
    return firefox_driver


@pytest.fixture(autouse=True)
def run_around_tests(newtours_on_firefox):
    yield
    newtours_on_firefox.quit()
