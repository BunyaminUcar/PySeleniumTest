import json
import pytest
from selenium.webdriver.common.by import By
from pages.basic_form import Form_Page
import time


@pytest.mark.usefixtures("setup")
class Test_Table():

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.driver.get(
            "https://testpages.herokuapp.com/styled/tag/dynamic-table.html")
        self.forms = Form_Page(self.driver)

    def test_table_form(self):

        assert self.driver.find_element(
            By.XPATH, "//h1").text == "Dynamic HTML TABLE Tag"

    def test_dynamic_table(self):
        self.driver.find_element(
            By.XPATH, "/html/body/div/div[3]/details/summary").click()
        time.sleep(1)
        payload = [{"name": "Sam", "age": 20},
                   {"name": "Millie", "age": 32},
                   {"name": "Joe", "age": 36},
                   {"name": "Ana", "age": 22}]
        payload_str = json.dumps(payload)
        self.driver.find_element(By.XPATH, "//*[@id='jsondata']").clear()
        self.driver.find_element(By.XPATH, "//*[@id='jsondata']").send_keys(payload_str)
        self.driver.find_element(By.XPATH, "//*[@id='caption']").clear()
        self.driver.find_element(By.XPATH, "//*[@id='caption']").send_keys("Dinamik Tablo")
        self.driver.find_element(By.XPATH,"//*[@id='tableid']").clear()
        self.driver.find_element(By.XPATH,"//*[@id='tableid']").send_keys("dynamictableid")
        self.driver.find_element(By.XPATH,"//*[@id='refreshtable']").click()

        time.sleep(5)

