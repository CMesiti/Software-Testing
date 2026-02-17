#import selenium, web driver test

"""
Test Valid Login
Selenium web driver for 
user interaction entering fields and page navigation
"""

from selenium import webdriver
from selenium.webdriver.common.by import By

class LoginTest():
    def __init__(self):
        self.driver = webdriver.Chrome()
    def login(self, username, password):
        self.driver.get("https://www.saucedemo.com/")

        self.driver.find_element(By.ID, "user-name").send_keys(username)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.ID, "login-button").click()


        if "Swag Labs" in self.driver.title:
            print("Test Passed - All Green |X|")
        else:
            print("Test Failed!")
        self.driver.quit()
    

tester = LoginTest()
tester.login("standard_user", "secret_sauce")

    
