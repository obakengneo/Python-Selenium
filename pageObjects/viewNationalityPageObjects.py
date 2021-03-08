from selenium import webdriver

class ViewNationalityPage:
    saveXPath_btn = "//input[@name='save']"
    nameId_txtBox = "id_name"
    descriptionId_txtArea = "id_description"

    def __init__(self, driver):
        self.driver = driver

    def clickAddedName(self, name):
        self.driver.find_element_by_xpath("//a[contains(text(),'"+name+"')]").click()
