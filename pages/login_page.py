
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class LoginPage:
    def __init__(self,driver):
        self.driver = driver
        self.username = 'username'
        self.password = 'password'
    
    def set_user(self):
        self.driver.find_element(By.NAME,self.username).send_keys('Admin')


    def set_pass(self):
        self.driver.find_element(By.NAME,self.password).send_keys('admin123'+ Keys.ENTER)




