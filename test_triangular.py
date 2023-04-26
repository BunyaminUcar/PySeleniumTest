import time
import pytest
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("setup")
class Test_Calculator:
    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.driver.get(
            "https://testpages.herokuapp.com/styled/apps/triangle/triangle001.html"
        )

    def test_3_4_5_triangular(self):
        self.driver.find_element(By.XPATH, "//*[@id='side1']").send_keys("3")
        self.driver.find_element(By.XPATH, "//*[@id='side2']").send_keys("4")
        self.driver.find_element(By.XPATH, "//*[@id='side3']").send_keys("5")
        self.driver.find_element(
            By.XPATH, "//*[@id='identify-triangle-action']"
        ).click()
        assert (
            self.driver.find_element(By.XPATH, "//*[@id='triangle-type']").text
            == "Scalene"
        )
        time.sleep(3)
