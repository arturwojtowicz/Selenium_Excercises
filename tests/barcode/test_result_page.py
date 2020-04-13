
import pytest

from time import sleep

from libs.scenario import starting_scenario
from libs.barcode.result_page import ResultPage
from tests.barcode import test_main_page


barcode_names = {
    'code128': 'CODE_128'
}

@starting_scenario(test_main_page.test_user_clicked_start_button_with_file_uploaded,  # TODO: Parametrization
                   'firefox_driver', 'value', 'barcode_type')
def test_results(firefox_driver, value: str = '1234567890', barcode_type: str = 'code128'):
    result_page = ResultPage(firefox_driver)

    assert result_page.get_result == value  # TODO: Wait for page load, to increase test stability
    assert result_page.get_format == barcode_names[barcode_type]
    