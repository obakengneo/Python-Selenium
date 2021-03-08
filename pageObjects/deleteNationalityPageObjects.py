from selenium import webdriver

class DeleteNationalityPage:
    saveXPath_btn = "//input[@name='save']"
    nameId_txtBox = "id_name"
    descriptionId_txtArea = "id_description"

    def __init__(self, driver):
        self.driver = driver

    def clickDeleteIcon(self, name):
        self.driver.find_element_by_xpath("//a[contains(text(),'"+name+"')]/../..//i[@class='fa fa-2x fa-trash warning']").click()

    def confirmDelete(self):
        self.driver.find_element_by_xpath("//button[@class='btn btn-warning']").click()
