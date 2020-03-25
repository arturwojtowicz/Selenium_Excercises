from libs.driver_utils import SelectByValue, SendKeys

from .main_page import MainPage


class RegistrationPage(MainPage):
    registration_layout = {
        'firstName': SendKeys('firstName'),
        'lastName': SendKeys('lastName'),
        'phone': SendKeys('phone'),
        'userName': SendKeys('userName'),
        'address1': SendKeys('address1'),
        'address2': SendKeys('address2'),
        'city': SendKeys('city'),
        'state': SendKeys('state'),
        'postalCode': SendKeys('postalCode'),
        'country': SelectByValue('country'),
        'email': SendKeys('email'),
        'password': SendKeys('password'),
        'confirmPassword': SendKeys('confirmPassword'),
    }

    def insert_register_credentials(self, user: dict):
        for key, value in user.items():
            self.registration_layout[key](self.driver, value)

    def click_register(self):
        self.driver.find_element_by_name("register").click()
