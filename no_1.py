import unittest
from selenium import webdriver
from selenium.webdriver.support.select import Select


class SelectByValue:
    def __init__(self, key):
        self._key = key
    
    def __call__(self, driver, value):
        Select(driver.find_element_by_name(self._key)).select_by_value(value)


class SendKeys:
    def __init__(self, key):
        self._key = key

    def __call__(self, driver, value):
        driver.find_element_by_name(self._key).send_keys(value)


user = {
    SendKeys('firstName'): 'Jan',
    SendKeys('lastName'): 'Kowalski',
    SendKeys('phone'): 'NotAPhoneNumber',
    SendKeys('userName'): 'example.jan.kowalski@email.email',
    SendKeys('address1'): 'Example street',
    SendKeys('address2'): 'Example number',
    SendKeys('city'): 'Middle of nowhere',
    SendKeys('state'): 'As above',
    SendKeys('postalCode'): 'proper',
    SelectByValue('country'): '166',
    SendKeys('email'): 'example.jan.kowalski@email.email',
    SendKeys('password'): 'example_password',
    SendKeys('confirmPassword'): 'example_password'
}


class LogInAndRegister(unittest.TestCase):
 
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.get('http://newtours.demoaut.com/')

    def test_user_wants_to_register(self):
        driver = self.driver
        driver.find_element_by_partial_link_text("Register here").click()
        for key, value in user.items():
            key(driver, value)
        driver.find_element_by_name("register").click()
 
    def test_user_wants_to_log_in(self):
        driver = self.driver
        driver.find_element_by_name('userName').send_keys('example.jan.kowalski@email.email')
        driver.find_element_by_name('password').send_keys("example_password")
        driver.find_element_by_name("login").click()

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
