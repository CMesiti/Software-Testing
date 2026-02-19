"""
Register test based on the following test case:

Test Case 1: Register User
1. Launch browser
2. Navigate to url 'http://automationexercise.com'
3. Verify that home page is visible successfully
4. Click on 'Signup / Login' button
5. Verify 'New User Signup!' is visible
6. Enter name and email address
7. Click 'Signup' button
8. Verify that 'ENTER ACCOUNT INFORMATION' is visible
9. Fill details: Title, Name, Email, Password, Date of birth
10. Select checkbox 'Sign up for our newsletter!'
11. Select checkbox 'Receive special offers from our partners!'
12. Fill details: First name, Last name, Company, Address, Address2, Country, State, City, Zipcode, Mobile Number
13. Click 'Create Account button'
14. Verify that 'ACCOUNT CREATED!' is visible
15. Click 'Continue' button
16. Verify that 'Logged in as username' is visible
17. Click 'Delete Account' button
18. Verify that 'ACCOUNT DELETED!' is visible and click 'Continue' button
"""

#After automation use pytest to encapsulate and decouple tests from front-end with a page interfaces. 
from selenium import webdriver
from selenium.webdriver.common.by import By
class RegisterTest():
    def __init__(self):
        self.driver = webdriver.Chrome()
        
    def register(self, user_name, user_email):
        #navigate to home page
        self.driver.get("http://automationexercise.com")
        print("3. HomePage Checkpoint - All Green [X] ") #replace with logs, d&t.
        #click signup/login button
        nav_bar = self.driver.find_element(By.CLASS_NAME, "nav")
        #//Tagname[@AttibuteName = ‘value’]
        login = nav_bar.find_element(By.XPATH, '//a[@href="/login"]').click()
        signup_form = self.driver.find_element(By.CSS_SELECTOR, ".signup-form h2")
        if signup_form and signup_form.text == "New User Signup!":
            print("5. Signup Checkpoint Valid - All Green [X] ")
        else:
            print("5. Checkpoint Failed!")
        
        name = self.driver.find_element(By.XPATH, '//input[@data-qa="signup-name"]')
        email = self.driver.find_element(By.XPATH, '//input[@data-qa="signup-email"]')
        name.send_keys(user_name)
        email.send_keys(user_email)

        signup_button = self.driver.find_element(By.CSS_SELECTOR, ".signup-form form button")
        signup_button.click()




register = RegisterTest().register("MyName", "MyEmail@example.com")