from selenium import webdriver
import time

class CreateNewNationality:
    addNationalityXPath = "//i[@class='fa fa-plus-circle']"
    nameId_txtBox = "id_name"
    descriptionId_txtArea = "id_description"
    saveXPath_btn = "//input[@name='save']"

    def __init__(self, driver):
        self.driver = driver

    def selectAddNationality(self):
        self.driver.find_element_by_xpath(self.addNationalityXPath).click()

    def setName(self, name):
        time.sleep(3)
        self.driver.find_element_by_id(self.nameId_txtBox).clear()
        self.driver.find_element_by_id(self.nameId_txtBox).send_keys(name)

    def setDescription(self, description):
        time.sleep(3)
        self.driver.find_element_by_id(self.descriptionId_txtArea).clear()
        self.driver.find_element_by_id(self.descriptionId_txtArea).send_keys(description)

    def clickSave(self):
        self.driver.find_element_by_xpath(self.saveXPath_btn).click()