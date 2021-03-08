from selenium import webdriver

class LoginPage:
    usernameId_txtBox="id_username"
    passwordId_txtBox="id-password"
    loginXpath_btn="//button[@class='btn btn-primary btn-lg btn-block']"
    loggedInUserXpath_dropdown="//li[@class='dropdown dropdown-user nav-item']"
    logoutXPath_btn="//i[@class='feather icon-power']"

    def __init__(self, driver):
        self.driver = driver

    def setUsername(self, username):
        self.driver.find_element_by_id(self.usernameId_txtBox).clear()
        self.driver.find_element_by_id(self.usernameId_txtBox).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element_by_id(self.passwordId_txtBox).clear()
        self.driver.find_element_by_id(self.passwordId_txtBox).send_keys(password)

    def clickLogin(self):
        self.driver.find_element_by_xpath(self.loginXpath_btn).click()

    def clickLogout(self):
        self.driver.find_element_by_xpath(self.loggedInUserXpath_dropdown).click()
        self.driver.find_element_by_xpath(self.logoutXPath_btn).click()