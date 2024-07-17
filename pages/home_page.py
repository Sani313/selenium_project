from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


class HomePage:
    def __init__(self,driver):
        self.driver = driver
        self.welcome = '//span[@class="oxd-userdropdown-tab"]'
        self.logout = '//a[@href="/web/index.php/auth/logout"]'

    def welcome_but(self):
        self.driver.execute_script('window.scrollTo(0,100)')
        sleep(2)
        self.driver.execute_script("window.scrollTo(0,300)")
        sleep(2)
        self.driver.execute_script('window.scrollTo(100,400)')
        sleep(2)

        self.driver.find_element(By.XPATH,self.welcome).click()


    def logout_but(self):
        self.driver.find_element(By.XPATH,self.logout).click()


        

