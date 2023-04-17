from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
from pages.pageBase import PageBase


@pytest.mark.usefixtures("setup")
class Alert_Page(PageBase):
    
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        
