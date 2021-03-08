from pageObjects.loginPageObjects import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGeneration
import pytest

class Test_001_Login:
    baseUrl = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

    logger = LogGeneration.logGeneration()  # Getting logger

    @pytest.mark.regression
    def test_Login(self, setup):
        self.logger.info("********Test_001_Login********")
        self.logger.info("********Verifying Login test********")
        self.driver = setup
        self.driver.get(self.baseUrl)

        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        act_title = self.driver.title
        expected_title = "My timesheet list weekly"

        if act_title == expected_title:
            self.driver.save_screenshot(".\\screenshots\\" + "test_Login.png")
            self.driver.close()
            self.logger.info("******** Login Test passed ********")
            assert True
        else:
            self.driver.save_screenshot(".\\screenshots\\" + "test_Login.png")
            self.driver.close()
            self.logger.info("******** Login Test failed ********")
            assert False
