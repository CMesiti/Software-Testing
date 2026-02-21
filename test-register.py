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
9. Fill details: page_title, Name, Email, Password, Date of birth
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
from selenium.webdriver.support.select import Select
import random
class RegisterTest():
    def __init__(self):
        self.driver = webdriver.Chrome()
        
    def register(self, user_name, user_email, password):
        #navigate to home page
        self.driver.get("http://automationexercise.com")
        print("3. HomePage Checkpoint - All Green [X] ") #replace with logs, d&t.
        #click signup/login button
        nav_bar = self.driver.find_element(By.CLASS_NAME, "nav")
        #//Tagname[@AttibuteName = ‘value’]
        nav_bar.find_element(By.XPATH, '//a[@href="/login"]').click()
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

        #get the element containing the required page_title;
        page_title = self.driver.find_element(By.CLASS_NAME, "title").text
        if page_title and page_title == "ENTER ACCOUNT INFORMATION":
             print("8. Signup Checkpoint Valid - All Green [X] ")
        else:
            print("8. Checkpoint Failed!")
        
        #Fill details: page_title, Name, Email, Password, Date of birth
        self.driver.find_element(By.ID, 'uniform-id_gender1').click()
        self.driver.find_element(By.ID, 'name').send_keys(user_name)
        self.driver.find_element(By.ID, 'email').send_keys(user_email)
        self.driver.find_element(By.ID, 'password').send_keys(password)
        print("successfully passed until here")

        # 10. Select checkbox 'Sign up for our newsletter!'
        # 11. Select checkbox 'Receive special offers from our partners!'
        # 12. Fill details: First name, Last name, Company, Address, Address2, Country, State, City, Zipcode, Mobile Number
        self.driver.find_element(By.ID, 'newsletter').click()
        self.driver.find_element(By.ID, 'optin').click()

        self.driver.find_element(By.ID, 'first_name').send_keys()
        self.driver.find_element(By.ID, 'last_name').send_keys()
        self.driver.find_element(By.ID, 'company').send_keys()
        self.driver.find_element(By.ID, "address1").send_keys()
        self.driver.find_element(By.ID, "address2").send_keys()

        #get select list
        countries = self.driver.find_element(By.ID, "country")
        selection = Select(countries)
        country = random.choice(selection.options)
        print(f"Options: {selection.options}, Choice: {country}")
        selection.select_by_value(country)


        



if __name__ == "__main__":
    print("Registration Test!")
    in_name = input("Enter Name: ").strip()
    in_email = input("Enter Email: ").strip()
    in_pass = input("Enter Password: ").strip()
    register = RegisterTest().register(in_name, in_email, in_pass)