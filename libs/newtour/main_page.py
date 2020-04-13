from typing import NoReturn

from libs.utils import AccessorBase


class MainPage(AccessorBase):

    def insert_login_credentials(self, username: str, password: str) -> NoReturn:
        self.driver.find_element_by_name('userName').send_keys(username)
        self.driver.find_element_by_name('password').send_keys(password)

    def log_in(self) -> NoReturn:
        self.driver.find_element_by_name("login").click()

    def move_to_registration_form(self) -> NoReturn:
        self.driver.find_element_by_partial_link_text("Register here").click()
