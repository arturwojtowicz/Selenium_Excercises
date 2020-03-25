from libs.newtour.main_page import MainPage


example_user = {
    'username': 'example.jan.kowalski@email.email',
    'password': 'example_password'
}


def test_log_in(newtours_on_firefox):
    main_page = MainPage(newtours_on_firefox)
    main_page.insert_login_credentials(*example_user.values())
    main_page.log_in()
    assert main_page.title_changed() and 'Find a Flight' in newtours_on_firefox.title


def test_move_to_registration_form(newtours_on_firefox):  # FixIt, double execution
    main_page = MainPage(newtours_on_firefox)
    main_page.move_to_registration_form()
    assert main_page.title_changed() and 'Register:' in newtours_on_firefox.title



