import json
from selenium.webdriver.common.by import By
import pytest
from pages.pageBase import PageBase


@pytest.mark.usefixtures("setup")
class Dynamic_Table(PageBase):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def get_table_TAG(self):
        return self.driver.find_element(By.XPATH, "//h1").text

    def table_conf_button_click(self):
        self.driver.find_element(
            By.XPATH, "/html/body/div/div[3]/details/summary"
        ).click()

    def put_json_data_in_table(self):
        payload = [
            {"name": "Sam", "age": 20},
            {"name": "Millie", "age": 32},
            {"name": "Joe", "age": 36},
            {"name": "Ana", "age": 22},
        ]
        payload_str = json.dumps(payload)
        self.driver.find_element(By.XPATH, "//*[@id='jsondata']").clear()
        self.driver.find_element(By.XPATH, "//*[@id='jsondata']").send_keys(payload_str)

    def change_dynamic_table_caption(self):
        self.driver.find_element(By.XPATH, "//*[@id='caption']").clear()
        self.driver.find_element(By.XPATH, "//*[@id='caption']").send_keys(
            "Dinamik Tablo"
        )

    def change_dynamic_table_id_name(self):
        self.driver.find_element(By.XPATH, "//*[@id='tableid']").clear()
        self.driver.find_element(By.XPATH, "//*[@id='tableid']").send_keys(
            "dynamictableid"
        )

    def refresh_button(self):
        self.driver.find_element(By.XPATH, "//*[@id='refreshtable']").click()
