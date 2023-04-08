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
    SUBMIT_BUTTON=(By.XPATH,"//input[@type='submit']")
    VALUE_USERNAME=(By.XPATH,"//*[@id='_valueusername']")
    VALUE_PASSWORD=(By.XPATH,"//*[@id='_valuepassword']")   
    
    
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
