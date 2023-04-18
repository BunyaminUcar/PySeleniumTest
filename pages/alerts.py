from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
from pages.pageBase import PageBase


@pytest.mark.usefixtures("setup")
class Alert_Page(PageBase):
    SİMPLE_ALERT = (By.XPATH, "//*[@id='alertexamples']")
    CONFİRM_BOX_ALERT = (By.XPATH, "//*[@id='confirmexample']")
    CONFİRM_BOX_VARİABLE = (By.XPATH, "//*[@id='confirmreturn']")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def click_simple_alert_buton(self):
        self.driver.find_element(*Alert_Page.SİMPLE_ALERT).click()

    def switch_to_alert(self):
        return self.driver.switch_to.alert

    def alert_accept(self):
        self.driver.switch_to.alert.accept()

    def alert_dismiss(self):
        self.driver.switch_to.alert.dismiss()

    def click_confirm_box_buton(self):
        self.driver.find_element(*Alert_Page.CONFİRM_BOX_ALERT).click()

    def confirm_box_variable(self):
        return self.driver.find_element(*Alert_Page.CONFİRM_BOX_VARİABLE).text
