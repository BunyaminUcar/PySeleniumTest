import pytest
from selenium.webdriver.common.by import By
from pages.basic_form import Form_Page


@pytest.mark.usefixtures("setup")
class Test_Form():
    
    
        
    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.driver.get("https://testpages.herokuapp.com/styled/basic-html-form-test.html")
        self.forms=Form_Page(self.driver)
            
    def test_form_title(self):
        title=self.driver.find_element(By.XPATH,"/html/body/div/h1").text    
        assert title=="Basic HTML Form Example"


