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
        
    def test_checkbox_items_is_selected(self):
        checkbox1,checkbox2,checkbox3=self.forms.checkbox_select()
        self.forms.if_checkbox_is_not_selected_then_click(checkbox1)
        self.forms.if_checkbox_is_not_selected_then_click(checkbox2)
        self.forms.if_checkbox_is_not_selected_then_click(checkbox3)
        assert checkbox3.is_selected()==True       
        assert checkbox2.is_selected()==True   
        assert checkbox1.is_selected()==True   
    def  test_radio_items_is_selected(self):
        radio1,radio2,radio3=self.forms.radio_select()
        self.forms.if_radio_button_is_not_selected_then_click(radio1)
        assert radio1.is_selected()==True
        self.forms.if_radio_button_is_not_selected_then_click(radio2)
        assert radio2.is_selected()==True
        self.forms.if_radio_button_is_not_selected_then_click(radio3)
        assert radio3.is_selected()==True
        
    def test_multiple_selected_value_control(self):
        """//option[@value='ms1']"""
        """//*[@id='_valuemultipleselect0']"""
        ms1,ms2,ms3,ms4=self.forms.get_m_s_value()
        self.forms.if_multiple_select_is_not_selected_then_click(ms1)
        self.forms.if_multiple_select_is_not_selected_then_click(ms2)
        self.forms.if_multiple_select_is_not_selected_then_click(ms3)
        self.forms.if_multiple_select_is_not_selected_then_click(ms4)
        self.forms.click_submit_button()
        assert self.driver.find_element(By.XPATH,"//*[@id='_valuemultipleselect0']").text=="ms1"
        assert self.driver.find_element(By.XPATH,"//*[@id='_valuemultipleselect1']").text=="ms2"
        assert self.driver.find_element(By.XPATH,"//*[@id='_valuemultipleselect2']").text=="ms3"
        assert self.driver.find_element(By.XPATH,"//*[@id='_valuemultipleselect3']").text=="ms4"
        
        