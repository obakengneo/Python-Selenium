from pageObjects.editNationalityPageObjects import EditNationalityPage
from utilities.customLogger import LogGeneration
from pageObjects.loginPageObjects import LoginPage
from utilities.readProperties import ReadConfig
from faker import Faker
import pytest
import time

class Test_005_EditNationality:

    baseUrl = "https://staging.riseapp.co.za/lookup/nationalities/list/"
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    oldName = ReadConfig.getName()

    faker = Faker()
    name = faker.name()
    description = faker.text()

    ReadConfig.setNationality(name)
    ReadConfig.setDescription(description)

    logger = LogGeneration.logGeneration()  # Getting logger

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_EditNationality(self, setup):

        self.logger.info("******** Test_005_EditNationality ********")
        self.logger.info("******** Verifying Edit Nationality********")
        self.driver = setup
        self.driver.get(self.baseUrl)

        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        self.editNationality = EditNationalityPage(self.driver)
        self.editNationality.clickAddedName(self.oldName)

        time.sleep(3)
        self.editNationality.clickEdit()
        self.editNationality.setName(self.name)
        self.editNationality.setDescription(self.description)
        self.editNationality.clickSave()

        act_title = self.driver.title
        expected_title = "Nationalities"

        if act_title == expected_title:
            self.driver.save_screenshot(".\\screenshots\\" + "test_EditNationality.png")
            self.driver.close()
            self.logger.info("******** Edit Nationality Test passed ********")
            assert True
        else:
            self.driver.save_screenshot(".\\screenshots\\" + "test_EditNationality.png")
            self.driver.close()
            self.logger.info("******** Edit Nationality Test failed ********")
            assert False
