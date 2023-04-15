
import pytest
from selenium.webdriver.common.by import By
from pages.basic_form import Form_Page
import time

from pages.table import Dynamic_Table


@pytest.mark.usefixtures("setup")
class Test_Table():

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.driver.get(
            "https://testpages.herokuapp.com/styled/tag/dynamic-table.html")
        self.dynamicTable = Dynamic_Table(self.driver)

    def test_table_form(self):

        assert self.dynamicTable.get_table_TAG() == "Dynamic HTML TABLE Tag"

    def test_dynamic_table(self):
        self.dynamicTable.table_conf_button_click()
        time.sleep(1)
        self.dynamicTable.put_json_data_in_table()
        self.dynamicTable.change_dynamic_table_caption()
        self.dynamicTable.refresh_button()
