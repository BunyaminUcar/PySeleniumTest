import pytest
from selenium.webdriver.common.by import By
from pages.basic_form import Form_Page
import time

@pytest.mark.usefixtures("setup")
class Test_Table():
    

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.driver.get("https://testpages.herokuapp.com/styled/tag/dynamic-table.html")
        self.forms=Form_Page(self.driver)
        
    def test_table_name(self):
        
        assert self.driver.find_element(By.XPATH,"//*[@id='dynamictable']/caption").text=="Dynamic Table"