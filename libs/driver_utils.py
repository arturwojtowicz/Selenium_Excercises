from selenium.webdriver.support.select import Select


class SelectByValue:
    def __init__(self, key):
        self._key = key
    
    def __call__(self, driver, value):
        Select(driver.find_element_by_name(self._key)).select_by_value(value)


class SendKeys:
    def __init__(self, key):
        self._key = key

    def __call__(self, driver, value):
        driver.find_element_by_name(self._key).send_keys(value)
