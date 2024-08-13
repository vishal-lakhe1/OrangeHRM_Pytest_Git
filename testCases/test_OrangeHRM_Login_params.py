import time  # Import the time module to introduce delays in the test

import pytest  # Import pytest for creating test cases
from selenium import webdriver  # Import the selenium webdriver for browser automation
from selenium.webdriver.common.by import By  # Import By for locating elements

from pageObjects.Login_Page import LoginPage_Class  # Import the LoginPage class from pageObjects module
from utilities.LoggerFile import LogGenerator  # Import the LogGenerator class for logging
from utilities.readConfigFile import ReadConfig_Class  # Import the ReadConfig_Class for reading configuration files


class Test_OrangeHRM_Login_params:  # Define the test class for parameterized OrangeHRM login tests
    log = LogGenerator.loggen()  # Initialize the logger

    @pytest.mark.regression
    @pytest.mark.group1
    def test_OrangeHRM_Login_params_003(self, setup, getDataForLogin):
        self.log.info("test_OrangeHRM_Login_params_003 is started")  # Log the start of the test
        self.driver = setup  # Initialize the WebDriver using the setup fixture
        self.log.info("Opening the browser")  # Log the action of opening the browser
        self.lp = LoginPage_Class(self.driver)  # Create an instance of the LoginPage class
        # self.driver.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys("Admin")  # Example of locating and interacting with an element
        # print("Username-->" + self.Username)  # Print the username
        # print("Password-->" + self.Password)  # Print the password
        self.log.info("Entering Username-->" + getDataForLogin[0])  # Log the action of entering the username from the test data
        self.lp.Enter_UserName(getDataForLogin[0])  # Enter the username using the page object method
        # self.driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("admin123")  # Example of locating and interacting with an element
        self.log.info("Entering Password-->" + getDataForLogin[1])  # Log the action of entering the password from the test data
        self.lp.Enter_Password(getDataForLogin[1])  # Enter the password using the page object method
        # self.driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()  # Example of locating and interacting with an element
        self.log.info("Clicking on login button")  # Log the action of clicking the login button
        self.lp.Click_LoginButton()  # Click the login button using the page object method
        self.log.info("Verifying the login status")  # Log the verification of the login status
        if self.lp.Validate_Login_Stauts() == "LoginPass" and getDataForLogin[2] == "Login_Pass":  # Check if login passed and expected result is "Login_Pass"
            self.log.info("test_OrangeHRM_Login_params_003 is passed")  # Log the success of the test
            time.sleep(2)  # Wait for 2 seconds
            self.log.info("Taking the screenshot")  # Log the action of taking a screenshot
            self.driver.save_screenshot(".\\Screenshots\\test_OrangeHRM_Login_params_003_pass.png")  # Save a screenshot
            self.log.info("Clicking on Menu button")  # Log the action of clicking the menu button
            self.lp.Click_Menu_Button()  # Click the menu button using the page object method
            self.log.info("Clicking on logout button")  # Log the action of clicking the logout button
            self.lp.Click_Logout_Button()  # Click the logout button using the page object method
            assert True  # Assert the test as passed
        elif self.lp.Validate_Login_Stauts() == "LoginPass" and getDataForLogin[2] == "Login_Fail":  # Check if login passed and expected result is "Login_Fail"
            self.log.info("test_OrangeHRM_Login_params_003 is failed")  # Log the failure of the test
            self.log.info("Taking a screenshot")  # Log the action of taking a screenshot
            self.driver.save_screenshot(".\\Screenshots\\test_OrangeHRM_Login_params_003_fail.png")  # Save a screenshot
            self.log.info("Clicking on Menu button")  # Log the action of clicking the menu button
            self.lp.Click_Menu_Button()  # Click the menu button using the page object method
            self.log.info("Clicking on logout button")  # Log the action of clicking the logout button
            self.lp.Click_Logout_Button()  # Click the logout button using the page object method
            assert False  # Assert the test as failed
        elif self.lp.Validate_Login_Stauts() == "LoginFail" and getDataForLogin[2] == "Login_Pass":  # Check if login failed and expected result is "Login_Pass"
            self.log.info("test_OrangeHRM_Login_params_003 is failed")  # Log the failure of the test
            self.log.info("Taking a screenshot")  # Log the action of taking a screenshot
            self.driver.save_screenshot(".\\Screenshots\\test_OrangeHRM_Login_params_003_fail.png")  # Save a screenshot
            assert False  # Assert the test as failed
        elif self.lp.Validate_Login_Stauts() == "LoginFail" and getDataForLogin[2] == "Login_Fail":  # Check if login failed and expected result is "Login_Fail"
            self.log.info("test_OrangeHRM_Login_params_003 is passed")  # Log the success of the test
            self.log.info("Taking a screenshot")  # Log the action of taking a screenshot
            self.driver.save_screenshot(".\\Screenshots\\test_OrangeHRM_Login_params_003_pass.png")  # Save a screenshot
            assert True  # Assert the test as passed
        self.log.info("Closing the browser")  # Log the action of closing the browser
        self.driver.quit()  # Close the browser
        self.log.info("test_OrangeHRM_Login_params_003 is completed")  # Log the completion of the test


