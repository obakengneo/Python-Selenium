from pageObjects.viewNationalityPageObjects import ViewNationalityPage
from pageObjects.loginPageObjects import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGeneration
import pytest

class Test_004_ViewAddedNationality:

    baseUrl = "https://staging.riseapp.co.za/lookup/nationalities/list/"
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    name = ReadConfig.getName()

    logger = LogGeneration.logGeneration()  # Getting logger

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_ViewAddedNationality(self, setup):
        self.logger.info("******** Test_004_ViewAddedNationality ********")
        self.driver = setup
        self.driver.get(self.baseUrl)

        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        self.view = ViewNationalityPage(self.driver)
        self.view.clickAddedName(self.name)

        act_title = self.driver.title
        expected_title = "View nationality"

        if act_title == expected_title:
            self.driver.save_screenshot(".\\screenshots\\" + "test_ViewAddedNationality.png")
            self.logger.info("******** View Added Nationality Test passed ********")
            self.driver.close()
            assert True
        else:
            self.driver.save_screenshot(".\\screenshots\\" + "test_ViewAddedNationality.png")
            self.driver.close()
            self.logger.info("******** View Added Nationality failed ********")
            assert False
