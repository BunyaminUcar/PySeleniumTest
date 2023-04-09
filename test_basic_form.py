import pytest
from selenium.webdriver.common.by import By
from pages.basic_form import Form_Page
import time

@pytest.mark.usefixtures("setup")
class Test_Form():
    
    
        
    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.driver.get("https://testpages.herokuapp.com/styled/basic-html-form-test.html")
        self.forms=Form_Page(self.driver)
            
    def test_form_title(self):
        title=self.forms.get_text_from_the_element()  
        assert title=="Basic HTML Form Example"

    def test_email_and_password_value_validation(self):
        email="test@test.com"
        password="test123"
        self.forms.send_email_and_password(email,password)
        self.forms.click_submit_button()
        assert self.forms.get_email_value()==email
        assert self.forms.get_password_value()==password
        
    def test_email_and_password_value_validation_with_empty_email_and_password(self):
        email=""
        password=""
        self.forms.send_email_and_password(email,password)
        self.forms.click_submit_button()
        assert self.forms.email_is_visible()==False
        assert self.forms.password_is_visible()==False
        
    def test_textarea_comment_value_validation(self):
        
        key="Test text value"
        self.forms.send_textarea_value(key)
        self.forms.click_submit_button()
        assert key == self.forms.get_textarea_value()
        