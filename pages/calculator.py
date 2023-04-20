from selenium.webdriver.common.by import By
import pytest
from pages.pageBase import PageBase
from selenium.webdriver.support.ui import Select


@pytest.mark.usefixtures("setup")
class Calculator(PageBase):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    RESULT = (By.XPATH, "//*[@id='answer']")
    FIRST_VALUE = (By.XPATH, "//*[@id='number1']")
    SECOND_VALUE = (By.XPATH, "//*[@id='number2']")
    DROP_DOWN_LIST = (By.XPATH, "//*[@id='function']")
    CALCULATE_BUTTON = (By.XPATH, "//*[@id='calculate']")

    def send_first_value(self, value):
        self.driver.find_element(*Calculator.FIRST_VALUE).send_keys(value)

    def send_second_value(self, value):
        self.driver.find_element(*Calculator.SECOND_VALUE).send_keys(value)

    def select_calculation_method(self, key):
        dropdownlist = self.driver.find_element(*Calculator.DROP_DOWN_LIST)
        dropdownlist = Select(dropdownlist)
        dropdownlist.select_by_visible_text(key)

    def click_calculate_button(self):
        self.driver.find_element(*Calculator.CALCULATE_BUTTON).click()

    def give_result(self):
        return self.driver.find_element(*Calculator.RESULT).text

    def clear_first_value(self):
        self.driver.find_element(*Calculator.FIRST_VALUE).clear()

    def clear_second_value(self):
        self.driver.find_element(*Calculator.SECOND_VALUE).clear()
