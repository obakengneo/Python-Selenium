from pageObjects.deleteNationalityPageObjects import DeleteNationalityPage
from utilities.customLogger import LogGeneration
from pageObjects.loginPageObjects import LoginPage
from utilities.readProperties import ReadConfig
import pytest
import time

class Test_006_DeleteNationality:

    baseUrl = "https://staging.riseapp.co.za/lookup/nationalities/list/"
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    name = ReadConfig.getName()

    logger = LogGeneration.logGeneration()  # Getting logger

    @pytest.mark.regression
    def test_DeleteNationality(self, setup):

        self.logger.info("******** Test_006_DeleteNationality ********")
        self.logger.info("******** Verifying Delete Nationality********")
        self.driver = setup
        self.driver.get(self.baseUrl)

        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        self.deleteNationality = DeleteNationalityPage(self.driver)

        time.sleep(3)
        self.deleteNationality.clickDeleteIcon(self.name)
        time.sleep(3)
        self.deleteNationality.confirmDelete()

        act_title = self.driver.title
        expected_title = "Nationalities"

        if act_title == expected_title:
            self.driver.save_screenshot(".\\screenshots\\" + "test_DeleteNationality.png")
            self.driver.close()
            self.logger.info("******** Delete Nationality Test passed ********")
            assert True
        else:
            self.driver.save_screenshot(".\\screenshots\\" + "test_DeleteNationality.png")
            self.driver.close()
            self.logger.info("******** Delete Nationality Test failed ********")
            assert False
