from libs.newtour.registration_page import RegistrationPage

from .test_main_page import example_user as user
from .test_main_page import test_move_to_registration_form


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

def test_user_wants_to_register(newtours_on_firefox):
    test_move_to_registration_form(newtours_on_firefox)
    registration_page = RegistrationPage(newtours_on_firefox)
    registration_page.insert_register_credentials(example_user)
    registration_page.click_register()
    assert not registration_page.title_changed()
    assert newtours_on_firefox.find_element_by_xpath(f"//*[contains(text(), 'Dear {example_user['firstName']} {example_user['lastName']}')]")
    assert newtours_on_firefox.find_element_by_xpath("//*[contains(text(), 'Thank you for registering.')]")
