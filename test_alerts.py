import time
import pytest
from selenium.webdriver.common.by import By
from pages.basic_form import Form_Page


@pytest.mark.usefixtures("setup")
class Test_Alerts():

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.driver.get(
            "https://testpages.herokuapp.com/styled/alerts/alert-test.html")
        self.forms = Form_Page(self.driver)

    def test_simple_alert_box(self):

        self.driver.find_element(
            By.XPATH, "//*[@id='alertexamples']").click()
        alert = self.driver.switch_to.alert
        alert_text = alert.text
        self.driver.switch_to.alert.accept()
        assert alert_text == "I am an alert box!"

    def test_show_confirm_box_then_accept(self):

        self.driver.find_element(By.XPATH, "//*[@id='confirmexample']").click()
        alert = self.driver.switch_to.alert
        alert_text = alert.text
        self.driver.switch_to.alert.accept()
        assert self.driver.find_element(
            By.XPATH, "//*[@id='confirmreturn']").text == "true"
        assert alert_text == "I am a confirm alert"

    def test_show_confirm_box_then_dismiss(self):

        self.driver.find_element(By.XPATH, "//*[@id='confirmexample']").click()
        alert = self.driver.switch_to.alert
        alert_text = alert.text
        self.driver.switch_to.alert.dismiss()
        assert self.driver.find_element(
            By.XPATH, "//*[@id='confirmreturn']").text == "false"
        assert alert_text == "I am a confirm alert"

    def test_show_prompt_box_then_send_keys_and_accept(self):
        self.driver.find_element(By.XPATH, "//*[@id='promptexample']").click()
        time.sleep(5)
        self.driver.switch_to.alert.send_keys("test prompt box")
        assert self.driver.find_element(
            By.XPATH, "//*[@id='promptreturn']").text == "test prompt box"
        time.sleep(3)
