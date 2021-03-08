from selenium import webdriver
import time

class NavigateToNationalities:
    menuXPath_dropdown="//i[@class='ft-menu']"
    lookupsXPath_btn = "//span[@data-i18n='Lookups']"
    nationalitiesXPath_btn="//*[contains(text(),'Nationalities')]"

    def __init__(self, driver):
        self.driver = driver

    def navigate(self):
        self.driver.find_element_by_xpath(self.menuXPath_dropdown).click()
        time.sleep(5)
        self.driver.find_element_by_xpath(self.lookupsXPath_btn).click()
        time.sleep(5)
        self.driver.find_element_by_xpath(self.nationalitiesXPath_btn).click()

