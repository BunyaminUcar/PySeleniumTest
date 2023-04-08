from selenium.webdriver.common.by import By
import pytest
from pages.pageBase import PageBase


@pytest.mark.usefixtures("setup")
class Form_Page(PageBase):
    FORM_PAGE_TİTLE=(By.XPATH,"/html/body/div/h1")    
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
    def get_text_from_the_element(self):
        title=self.driver.find_element(*Form_Page.FORM_PAGE_TİTLE).text
        return title