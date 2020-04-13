from selenium.webdriver.support.select import Select


class WebDriver:
    ...


class SelectByValue:
    def __init__(self, key: str):
        self._key = key
    
    def __call__(self, driver: WebDriver, value: str):
        Select(driver.find_element_by_name(self._key)).select_by_value(value)


class SendKeys:
    def __init__(self, key: str):
        self._key = key

    def __call__(self, driver: WebDriver, value: str):
        driver.find_element_by_name(self._key).send_keys(value)
