from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

class LoginPage:
    textbox_username_name = 'uname'
    textbox_password_name = 'psw'
    button_login_xpath = "//button[@type='submit']"

    def __init__(self, driver):
        self.driver = driver

    def setUserName(self, username):
        self.driver.find_element_by_name(self.textbox_username_name).clear()
        time.sleep(2)
        self.driver.find_element_by_name(self.textbox_username_name).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element_by_name(self.textbox_password_name).clear()
        time.sleep(2)
        self.driver.find_element_by_name(self.textbox_password_name).send_keys(password)

    time.sleep(2)

    def clickLogin(self):
        self.driver.find_element_by_xpath(self.button_login_xpath).click()

    # Switching to alerts
    def alert(self, driver):
        alert = self.driver.switch_to.alert
        self.driver.implicitly_wait(3)
        alert.accept()

    def logout(self):
        pass
