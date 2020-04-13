from libs.newtour.registration_page import RegistrationPage
from libs.scenario import starting_scenario
from tests.fixtures import firefox_driver
from tests.newtours import test_main_page

from .test_main_page import example_user as user


example_user = {
    'firstName': 'Jan',
    'lastName': 'Kowalski',
    'phone': 'NotAPhoneNumber',
    'userName': user['username'],
    'address1': 'Example street',
    'address2': 'Example number',
    'city': 'Middle of nowhere',
    'state': 'As above',
    'postalCode': 'proper',
    'country': '166',
    'email': user['username'],
    'password': user['password'],
    'confirmPassword': user['password']
}


@starting_scenario(test_main_page.test_move_to_registration_form, firefox_driver = firefox_driver)
def test_user_wants_to_register(firefox_driver):
    registration_page = RegistrationPage(firefox_driver)
    registration_page.insert_register_credentials(example_user)
    registration_page.click_register()

    registration_page.wait_for_page_load_until_url_change()
    assert not registration_page.is_title_changed()
    assert registration_page.is_url_changed()
    
    assert firefox_driver.find_element_by_xpath(f"//*[contains(text(), 'Dear {example_user['firstName']} {example_user['lastName']}')]")
    assert firefox_driver.find_element_by_xpath("//*[contains(text(), 'Thank you for registering.')]")
