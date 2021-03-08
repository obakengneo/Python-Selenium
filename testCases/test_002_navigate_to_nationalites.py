from pageObjects.navigateToNationalitiesPageObjects import NavigateToNationalities
from utilities.customLogger import LogGeneration
from pageObjects.loginPageObjects import LoginPage
from utilities.readProperties import ReadConfig
import pytest

class Test_002_NavigateToNationalities:

    logger = LogGeneration.logGeneration()  # Getting logger
    baseUrl = "https://staging.riseapp.co.za/timesheet/my-list/weekly/"
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_NavigateToNationalities(self, setup):
        self.logger.info("******** Test_002_NavigateToNationalities ********")
        self.driver = setup
        self.driver.get(self.baseUrl)

        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        self.navigate = NavigateToNationalities(self.driver)
        self.navigate.navigate()

        act_title = self.driver.title
        expected_title = "Nationalities"

        if act_title == expected_title:
            self.driver.save_screenshot(".\\screenshots\\" + "test_NavigateToNationalities.png")
            self.logger.info("******** NavigateToNationalities Test passed ********")
            self.driver.close()
            assert True
        else:
            self.driver.save_screenshot(".\\screenshots\\" + "test_NavigateToNationalities.png")
            self.driver.close()
            self.logger.info("******** NavigateToNationalitiesTest failed ********")
            assert False
