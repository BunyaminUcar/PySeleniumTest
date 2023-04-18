import time
import pytest
from selenium.webdriver.common.by import By
from pages.alerts import Alert_Page
from pages.basic_form import Form_Page


@pytest.mark.usefixtures("setup")
class Test_Alerts:
    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.driver.get("https://testpages.herokuapp.com/styled/alerts/alert-test.html")
        self.alerts = Alert_Page(self.driver)

    @pytest.mark.skip
    def test_simple_alert_box(self):
        self.alerts.click_simple_alert_buton()
        alert = self.alerts.switch_to_alert()
        alert_text = alert.text
        self.alerts.alert_accept()
        assert alert_text == "I am an alert box!"

    @pytest.mark.skip
    def test_show_confirm_box_then_accept(self):
        self.alerts.click_confirm_box_buton()
        alert = self.alerts.switch_to_alert()
        alert_text = alert.text
        self.alerts.alert_accept()
        assert self.alerts.confirm_box_variable() == "true"
        assert alert_text == "I am a confirm alert"

    def test_show_confirm_box_then_dismiss(self):
        self.alerts.click_confirm_box_buton()
        alert = self.alerts.switch_to_alert()
        alert_text = alert.text
        self.alerts.alert_dismiss()
        assert self.alerts.confirm_box_variable() == "false"
        assert alert_text == "I am a confirm alert"

    @pytest.mark.skip
    def test_show_prompt_box_then_send_keys_and_accept(self):
        self.driver.find_element(By.XPATH, "//*[@id='promptexample']").click()
        time.sleep(5)
        self.driver.switch_to.alert.send_keys("test prompt box")
        assert (
            self.driver.find_element(By.XPATH, "//*[@id='promptreturn']").text
            == "test prompt box"
        )
        time.sleep(3)
