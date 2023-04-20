import time
import pytest
from selenium.webdriver.common.by import By


from pages.calculator import Calculator


@pytest.mark.usefixtures("setup")
class Test_Calculator:
    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.driver.get("https://testpages.herokuapp.com/styled/calculator")
        self.calculator = Calculator(self.driver)

    def test_plus_function_with_integer_values(self):
        self.calculator.send_first_value("5")
        self.calculator.send_second_value("-2")
        self.calculator.select_addition("plus")
        self.calculator.click_calculate_button()
        result = self.calculator.give_result()
        assert result == "3"

    def test_plus_function_with_one_integer_values(self):
        self.calculator.send_first_value("5")
        self.calculator.send_second_value("")
        self.calculator.select_addition("plus")
        self.calculator.click_calculate_button()
        result = self.calculator.give_result()
        assert result == "ERR"

    def test_plus_function_with_one_String_values(self):
        self.calculator.send_first_value("abc")
        self.calculator.send_second_value("xyz")
        self.calculator.select_addition("plus")
        self.calculator.click_calculate_button()
        result = self.calculator.give_result()
        assert result == "ERR"

    def test_times_function_with_two_integer_values(self):
        self.calculator.send_first_value("16")
        self.calculator.send_second_value("2")
        self.calculator.select_addition("times")
        self.calculator.click_calculate_button()
        result = self.calculator.give_result()
        assert result == "32"

    def test_times_function_with_two_string_values(self):
        self.calculator.send_first_value("abc")
        self.calculator.send_second_value("xyz")
        self.calculator.select_addition("times")
        self.calculator.click_calculate_button()
        result = self.calculator.give_result()
        assert result == "ERR"

    def test_minus_function_with_two_integer_values(self):
        self.calculator.send_first_value("64")
        self.calculator.send_second_value("16")
        self.calculator.select_addition("minus")
        self.calculator.click_calculate_button()
        result = self.calculator.give_result()
        assert result == "48"

    def test_minus_function_with_two_string_values(self):
        self.calculator.send_first_value("abc")
        self.calculator.send_second_value("xyz")
        self.calculator.select_addition("minus")
        self.calculator.click_calculate_button()
        result = self.calculator.give_result()
        assert result == "ERR"

    def test_divide_function_with_two_ingeter_values(self):
        self.calculator.send_first_value("64")
        self.calculator.send_second_value("16")
        self.calculator.select_addition("divde")
        self.calculator.click_calculate_button()
        result = self.calculator.give_result()
        assert result == "4"

    def test_divide_function_with_two_ingeter_values(self):
        self.calculator.send_first_value("abc")
        self.calculator.send_second_value("xyz")
        self.calculator.select_addition("divide")
        self.calculator.click_calculate_button()
        result = self.calculator.give_result()
        assert result == "ERR"
