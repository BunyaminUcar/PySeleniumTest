from selenium.webdriver.common.by import By
import pytest
from pages.pageBase import PageBase
from selenium.webdriver.support.ui import Select


@pytest.mark.usefixtures("setup")
class Triangular(PageBase):
    FIRST_CORNER = (By.XPATH, "//*[@id='side1']")
    SECOND_CORNER = (By.XPATH, "//*[@id='side2']")
    THIRD_CORNER = (By.XPATH, "//*[@id='side3']")
    CALCULATE_BUTTON = (By.XPATH, "//*[@id='identify-triangle-action']")
    RESULT_TRIANGULAR = (By.XPATH, "//*[@id='triangle-type']")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def enter_the_first_corner(self, side):
        self.driver.find_element(*Triangular.FIRST_CORNER).send_keys(side)

    def enter_the_second_corner(self, side):
        self.driver.find_element(*Triangular.SECOND_CORNER).send_keys(side)

    def enter_the_third_corner(self, side):
        self.driver.find_element(*Triangular.THIRD_CORNER).send_keys(side)

    def calculate_tringular(self):
        self.driver.find_element(*Triangular.CALCULATE_BUTTON).click()

    def get_result(self):
        return self.driver.find_element(*Triangular.RESULT_TRIANGULAR).text
