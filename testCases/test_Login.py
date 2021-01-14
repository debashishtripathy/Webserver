import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage

class Test_001_Login:
    baseURL = "https://10.255.255.16/home.php"
    username = "@WREAdmin2017"
    password = "@WRE!Admin2017"


    def test_homePagetitle(self,setup):
        self.driver=setup
        self.driver.get(self.baseURL)
        self.driver.implicitly_wait(5)
        # handling Certificate page
        element = self.driver.find_element_by_id("details-button")
        element.click()
        self.driver.find_element_by_id('proceed-link').click()
        actual_title=self.driver.title
        actual_title = self.driver.title
        if actual_title == 'Your store. Login':
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshot\\" + "test_homePagetitle.png")
            self.driver.close()
            assert False

    def test_login(self,setup):
        self.driver=setup
        self.driver.get(self.baseURL)
        self.loginpage=LoginPage(self.driver)
        self.driver.implicitly_wait(5)
        # handling Certificate page
        element=self.driver.find_element_by_id("details-button")
        element.click()
        self.driver.find_element_by_id('proceed-link').click()
        self.loginpage.setUserName(self.username)
        self.loginpage.setPassword(self.password)
        self.loginpage.clickLogin()
        act_title = self.driver.title
        if act_title == "XXXXXXXXXXXXXXXXXXXX":
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshot\\" + "test_login.png")
            self.driver.close()
            assert False
