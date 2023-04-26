from selenium.webdriver.common.by import By
import pytest
from pages.pageBase import PageBase
from selenium.webdriver.support.ui import Select


@pytest.mark.usefixtures("setup")
class Triangular(PageBase):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def enter_the_first_corner(self, side):
        self.driver.find_element(By.XPATH, "//*[@id='side1']").send_keys(side)

    def enter_the_second_corner(self, side):
        self.driver.find_element(By.XPATH, "//*[@id='side2']").send_keys(side)

    def enter_the_third_corner(self, side):
        self.driver.find_element(By.XPATH, "//*[@id='side3']").send_keys(side)

    def calculate_tringular(self):
        self.driver.find_element(
            By.XPATH, "//*[@id='identify-triangle-action']"
        ).click()

    def get_result(self):
        return self.driver.find_element(By.XPATH, "//*[@id='triangle-type']").text
