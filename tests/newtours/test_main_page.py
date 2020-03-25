from libs.newtour.main_page import MainPage


example_user = {
    'username': 'example.jan.kowalski@email.email',
    'password': 'example_password'
}


def test_log_in(firefox_driver):
    main_page = MainPage(firefox_driver)
    main_page.insert_login_credentials(*example_user.values())
    main_page.log_in()
    assert main_page.title_changed() and 'Find a Flight' in firefox_driver.title


def test_move_to_registration_form(firefox_driver):  # FixIt, double execution
    main_page = MainPage(firefox_driver)
    main_page.move_to_registration_form()
    assert main_page.title_changed() and 'Register:' in firefox_driver.title



