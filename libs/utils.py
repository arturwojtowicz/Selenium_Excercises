import os
import random
from typing import NoReturn

import barcode
from barcode.writer import ImageWriter
from selenium.webdriver.support.expected_conditions import url_changes
from selenium.webdriver.support.ui import WebDriverWait

from .driver_utils import WebDriver


class AccessorBase:

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.title = self._title
        self.url = self._url

    @property
    def _title(self) -> str:
        return self.driver.title

    @property
    def _url(self) -> str:
        return self.driver.current_url

    def is_title_changed(self) -> bool:
        return self.title != self._title

    def is_url_changed(self) -> bool:
        return self.url != self._url

    def is_text_present(self, text: str) -> bool:
        return str(text) in self.driver.page_source

    def wait_for_page_load_until_url_change(self, timeout: int = 30) -> NoReturn:
        WebDriverWait(self.driver, timeout).until(
            url_changes(self.url), message = f'\nPage doesn\'t change.'
                                              f'\nPrevious page {self.url}'
                                              f'\nCurrent page {self._url}')


def get_absolute_path_of_file(f: str) -> str:
    return os.path.abspath(os.getcwd().join([f]))


def barcode_generator(value: str, barcode_type: str) -> str:
    code = barcode.get_barcode_class(barcode_type)
    prepared = code(value, writer = ImageWriter())

    addition = 0
    while os.path.exists(get_absolute_path_of_file('temp/' + value + barcode_type + f'_{addition}.svg')):
        addition += 1

    ready = prepared.save('temp/' + value + barcode_type + f'_{addition}')
    return ready
