import time
import pytest
from selenium.webdriver.common.by import By

from pages.triangular import Triangular


@pytest.mark.usefixtures("setup")
class Test_Triangular:
    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.driver.get(
            "https://testpages.herokuapp.com/styled/apps/triangle/triangle001.html"
        )
        self.triangular = Triangular(self.driver)

    def test_draw_a_drawable_triangle(self):
        self.triangular.enter_the_first_corner("3")
        self.triangular.enter_the_second_corner("4")
        self.triangular.enter_the_third_corner("5")
        self.triangular.calculate_tringular()
        result = self.triangular.get_result()
        assert result == "Scalene"

    def test_try_to_draw_a_not_drawable_triangular(self):
        self.triangular.enter_the_first_corner("38")
        self.triangular.enter_the_second_corner("440")
        self.triangular.enter_the_third_corner("1")
        self.triangular.calculate_tringular()
        result = self.triangular.get_result()
        assert result == "Error: Not a Triangle"
