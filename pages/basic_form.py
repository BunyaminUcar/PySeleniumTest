from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
from pages.pageBase import PageBase


@pytest.mark.usefixtures("setup")
class Form_Page(PageBase):
    
    
    FORM_PAGE_TİTLE=(By.XPATH,"/html/body/div/h1")    
    EMAİL_AREA=(By.XPATH,"//input[@type='text' and @name='username']")
    PASSWORD_AREA=(By.XPATH,"//input[@type='password']")
    TEXTAREA=(By.XPATH,"//textarea[@name='comments']")
    SUBMIT_BUTTON=(By.XPATH,"//input[@type='submit']")
    VALUE_USERNAME=(By.XPATH,"//*[@id='_valueusername']")
    VALUE_PASSWORD=(By.XPATH,"//*[@id='_valuepassword']")   
    VALUE_TEXTAREA=(By.XPATH,"//*[@id='_valuecomments']")
    CHECK_BOX1=(By.XPATH,"//input[@type='checkbox' and @value='cb1']")
    CHECK_BOX2=(By.XPATH,"//input[@type='checkbox' and @value='cb2']")
    CHECK_BOX3=(By.XPATH,"//input[@type='checkbox' and @value='cb3']")
    RADIO_BUTTON1=(By.XPATH,"//input[@type='radio' and @value='rd1']")
    RADIO_BUTTON2=(By.XPATH,"//input[@type='radio' and @value='rd2']")
    RADIO_BUTTON3=(By.XPATH,"//input[@type='radio' and @value='rd3']")
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        
    def get_text_from_the_element(self):
        title=self.driver.find_element(*Form_Page.FORM_PAGE_TİTLE).text
        return title
    
    def send_email_and_password(self,email,password):
        self.driver.find_element(*Form_Page.EMAİL_AREA).send_keys(email)
        self.driver.find_element(*Form_Page.PASSWORD_AREA).send_keys(password)
        
    def click_submit_button(self):
        self.driver.find_element(*Form_Page.SUBMIT_BUTTON).click()
        
    def get_email_value(self): 
        return self.driver.find_element(*Form_Page.VALUE_USERNAME).text
    def get_password_value(self):
        return self.driver.find_element(*Form_Page.VALUE_PASSWORD).text

    def radio_select(self):
        return self.driver.find_element(*Form_Page.RADIO_BUTTON1),self.driver.find_element(*Form_Page.RADIO_BUTTON2),self.driver.find_element(*Form_Page.RADIO_BUTTON3)
    
    def email_is_visible(self): 
        wait = WebDriverWait(self.driver, 1)
        try:
            wait.until(EC.visibility_of_element_located((Form_Page.VALUE_USERNAME)))
            result = True
        except:
            result = False
        return result
    
    def password_is_visible(self): 
        wait = WebDriverWait(self.driver, 1)
        try:
            wait.until(EC.visibility_of_element_located((Form_Page.VALUE_PASSWORD)))
            result = True
        except:
            result = False
        return result

    def get_textarea_value(self):
        return self.driver.find_element(*Form_Page.VALUE_TEXTAREA).text

    def send_textarea_value(self,key):
        self.driver.find_element(*Form_Page.TEXTAREA).clear()
        self.driver.find_element(*Form_Page.TEXTAREA).send_keys(key)
    def checkbox_select(self):
        return self.driver.find_element(*Form_Page.CHECK_BOX1),self.driver.find_element(*Form_Page.CHECK_BOX2),self.driver.find_element(*Form_Page.CHECK_BOX3)
          
    def if_checkbox_is_not_selected_then_click(self,checkbox):
        if checkbox.is_selected()==False:
            checkbox.click()
        
    def if_radio_button_is_not_selected_then_click(self,radio):
        
        if radio.is_selected()==False:
            radio.click()