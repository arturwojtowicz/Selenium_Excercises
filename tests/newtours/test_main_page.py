from tests.fixtures import firefox_driver

from libs.newtour.main_page import MainPage
from libs.scenario import starting_scenario


example_user = {
    'username': 'example.jan.kowalski@email.email',
    'password': 'example_password'
}


def test_newtours_main_page_opened(firefox_driver):
    firefox_driver.get('http://newtours.demoaut.com/')
    assert 'Welcome' in MainPage(firefox_driver).title


@starting_scenario(test_newtours_main_page_opened, firefox_driver = firefox_driver)
def test_log_in(firefox_driver):
    main_page = MainPage(firefox_driver)
    main_page.insert_login_credentials(*example_user.values())
    main_page.log_in()
    main_page.wait_for_page_load_until_url_change()
    assert main_page.is_url_changed()
    assert main_page.is_title_changed()
    assert 'Find a Flight' in firefox_driver.title


@starting_scenario(test_newtours_main_page_opened, firefox_driver = firefox_driver)
def test_move_to_registration_form(firefox_driver):
    main_page = MainPage(firefox_driver)
    main_page.move_to_registration_form()
    main_page.wait_for_page_load_until_url_change()
    assert main_page.is_url_changed()
    assert main_page.is_title_changed()
    assert 'Register:' in firefox_driver.title



