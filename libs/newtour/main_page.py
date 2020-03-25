class MainPage:

    def __init__(self, driver):
        self.driver = driver
        self.title = self._title

    @property
    def _title(self):
        return self.driver.title

    def title_changed(self):
        return self.title != self._title

    def insert_login_credentials(self, username: str, password: str):
        self.driver.find_element_by_name('userName').send_keys(username)
        self.driver.find_element_by_name('password').send_keys(password)

    def log_in(self):
        self.driver.find_element_by_name("login").click()

    def move_to_registration_form(self):
        self.driver.find_element_by_partial_link_text("Register here").click()
