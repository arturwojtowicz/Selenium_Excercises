from libs.utils import AccessorBase


class ResultPage(AccessorBase):

    @property
    def get_result(self) -> str:
        return self.driver.find_element_by_xpath("//textarea[@id='result-textarea']").text

    @property
    def get_format(self) -> str:
        result_desc = self.driver.find_element_by_xpath("//div[@id='result-desc']").text
        return result_desc.split('\n')[1]
