from pageObjects.createNewNationalityPageObjects import CreateNewNationality
from pageObjects.loginPageObjects import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGeneration
from faker import Faker
import time
import pytest

class Test_003_CreateNationality:
    baseUrl = "https://staging.riseapp.co.za/lookup/nationalities/list/"
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

    faker = Faker()
    name = faker.name()
    description = faker.text()

    ReadConfig.setNationality(name)
    ReadConfig.setDescription(description)

    logger = LogGeneration.logGeneration()  # Getting logger

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_CreateNationality(self, setup):

        self.logger.info("******** Test_003_CreateNationality ********")
        self.logger.info("******** Verifying Creating Nationality********")
        self.driver = setup
        self.driver.get(self.baseUrl)

        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        self.createNationality = CreateNewNationality(self.driver)
        self.createNationality.selectAddNationality()
        self.createNationality.setName(self.name)
        self.createNationality.setDescription(self.description)
        self.createNationality.clickSave()

        time.sleep(3)
        act_title = self.driver.title
        expected_title = "Nationalities"

        if act_title == expected_title:
            self.driver.save_screenshot(".\\screenshots\\" + "test_CreateNationality.png")
            self.driver.close()
            self.logger.info("******** CreateNationality Test passed ********")
            assert True
        else:
            self.driver.save_screenshot(".\\screenshots\\" + "test_CreateNationality.png")
            self.driver.close()
            self.logger.info("******** CreateNationality Test failed ********")
            assert False


