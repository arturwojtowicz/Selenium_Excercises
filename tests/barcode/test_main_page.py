import os

import pytest
from barcode import PROVIDED_BARCODES

from libs.barcode.main_page import MainPage
from libs.scenario import starting_scenario
from libs.utils import barcode_generator, get_absolute_path_of_file


def test_barcodereader_main_page_opened(firefox_driver):
    firefox_driver.get('https://www.onlinebarcodereader.com/')
    main_page = MainPage(firefox_driver)

    assert 'Barcode Reader' in main_page.title
    assert main_page.is_user_on_upload_page()
    assert not main_page.is_file_uploaded()


@starting_scenario(test_barcodereader_main_page_opened, 'firefox_driver')
def test_user_upload_file(firefox_driver, value: str = '1234567890', barcode_type: str = 'code128'):
    assert barcode_type in PROVIDED_BARCODES

    generated_file = barcode_generator(value, barcode_type)
    full_generated_file_path = get_absolute_path_of_file(generated_file)
    main_page = MainPage(firefox_driver)

    main_page.upload_file(file_to_upload = full_generated_file_path)
    main_page.wait_until_file_is_uploaded()
    assert main_page.is_file_uploaded()


@starting_scenario(test_user_upload_file, 'firefox_driver', 'value', 'barcode_type')
def test_user_clicked_start_button_with_file_uploaded(firefox_driver, value: str = '1234567890', barcode_type: str = 'code128'):
    main_page = MainPage(firefox_driver)

    main_page.click_start_button()
    assert not main_page.is_user_on_upload_page()


@starting_scenario(test_barcodereader_main_page_opened, 'firefox_driver')
def test_user_clicked_start_button_without_file_uploaded(firefox_driver):
    main_page = MainPage(firefox_driver)

    main_page.click_start_button()
    assert not main_page.is_user_on_upload_page()
    assert main_page.is_text_present('Please select a file to upload before submitting.')
