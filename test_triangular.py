import pytest



@pytest.mark.usefixtures("setup")
class Test_Calculator:
    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.driver.get("https://testpages.herokuapp.com/styled/apps/triangle/triangle001.html")
        
    def test_3_4_5_triangular(self):
        
        