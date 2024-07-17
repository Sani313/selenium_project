import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
from pages.login_page import LoginPage
from pages.home_page import HomePage



class POM_TEST(unittest.TestCase):
    driver = webdriver.Firefox()
    @classmethod
    def SetUp(cls):
        cls.driver

    def test_login(self):
        driver = POM_TEST.driver
        driver.get('https://opensource-demo.orangehrmlive.com/')
        sleep(2)

        Login = LoginPage(driver)


        Login.set_user()
        sleep(2)
        Login.set_pass()
        sleep(3)

        Home = HomePage(driver)

        Home.welcome_but()
        sleep(2)
        Home.logout_but()

        sleep(2)

    @classmethod
    def tearDown(cls):
        cls.driver.quit()



if __name__ == "__main__":
    unittest.main()











