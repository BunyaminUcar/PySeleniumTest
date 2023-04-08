from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 


class PageBase:
    
    def __init__(self, driver):
        self.driver = driver