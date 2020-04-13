import pytest

from pytest_bdd import scenarios, given, when, then, parsers
from libs.newtour.registration_page import RegistrationPage


example_user = {
    'firstName': 'Jan',
    'lastName': 'Kowalski',
    'phone': 'NotAPhoneNumber',
    'userName': 'example.jan.kowalski@email.email',
    'address1': 'Example street',
    'address2': 'Example number',
    'city': 'Middle of nowhere',
    'state': 'As above',
    'postalCode': 'proper',
    'country': '166',
    'email': 'example.jan.kowalski@email.email',
    'password': 'example_password',
    'confirmPassword': 'example_password'
}


# Scenarios

scenarios('../features/registration_page.feature')


# Fixtures

@pytest.fixture
def registration_page(firefox_driver):
    return RegistrationPage(firefox_driver)


# Given Steps

@given(parsers.parse('page {webpage} is displayed'))
def go_to_webpage(firefox_driver, webpage):
    firefox_driver.get(webpage)


# When Steps

@when('user insert register credentials')
def insert_register_credentials(registration_page):
    registration_page.insert_register_credentials(example_user)


@when('user clicks register')
def click_register(registration_page):
    registration_page.click_register()


# Then Steps

@then('user should be moved to another site')
def verify_title_and_url(registration_page):
    registration_page.wait_for_page_load_until_url_change()
    assert registration_page.is_url_changed()
    assert not registration_page.is_title_changed()


@then(parsers.parse('verify is message "{message}" exists on page'))
def verify_message(firefox_driver, message):
    assert firefox_driver.find_element_by_xpath(f"//*[contains(text(), '{message}')]")
