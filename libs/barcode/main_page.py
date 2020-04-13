from typing import NoReturn

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

from libs.utils import AccessorBase


class MainPage(AccessorBase):

    def is_user_on_upload_page(self) -> bool:
        try:
            return all([
                self.driver.find_element_by_xpath("//label[@for='fileupfield']")
                    .text == 'Upload a file:',
                self.driver.find_element_by_xpath("//label[@for='fileupfield-url']")
                    .text == 'Or enter a URL:',
                self.driver.find_element_by_xpath("//div[@class='fieldhint']")
                    .text == 'Max. file size for upload is 10 MB.'
                                '\nMax. height or width for image is 5000 pixel.'
                                '\nSupported file types: png, jpg, jpeg, gif, tiff, tif, pdf, bmp.'
            ])
        except NoSuchElementException:
            return False

    def is_file_uploaded(self):
        try:
            self.driver.find_element_by_xpath("//button[@class='clear-filefield-button']")
            return True
        except NoSuchElementException:
            return False

    def upload_file(self, file_to_upload: str) -> NoReturn:
        self.driver.find_element_by_xpath("//input[@id='fileupfield']").send_keys(file_to_upload)

    def click_start_button(self) -> NoReturn:
        self.driver.find_element_by_xpath("//input[@id='fbut']").click()

    def wait_until_file_is_uploaded(self, timeout: int = 30) -> NoReturn:
        WebDriverWait(self.driver, timeout).until(ec.visibility_of_element_located((By.XPATH, "//button[@class='clear-filefield-button']")))
