import pytest

from pytest_bdd import scenarios, given, when, then, parsers
from libs.newtour.main_page import MainPage


# Scenarios

scenarios('../features/main_page.feature')


# Fixtures

@pytest.fixture
def main_page(firefox_driver):
    return MainPage(firefox_driver)


# Given Steps

@given(parsers.parse('page {webpage} is displayed'))
def go_to_webpage(firefox_driver, webpage):
    firefox_driver.get(webpage)


# When Steps

@when(parsers.parse('user insert login: "{login}" and password: "{password}"'))
def insert_login_credentials(main_page, login, password):
    main_page.insert_login_credentials(login, password)


@when('user clicks sign-in')
def log_in(main_page):
    main_page.log_in()


@when('user clicks "Register here" sign')
def move_to_registration_form(main_page):
    main_page.move_to_registration_form()


#Then Steps

@then(parsers.parse('user should be moved to another site with title name starts with: "{titlename}"'))
def verify_title(main_page, titlename):
    assert main_page.title_changed()
    assert titlename in main_page._title
