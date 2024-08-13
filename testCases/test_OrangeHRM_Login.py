import time  # Import the time module to introduce delays in the test

import pytest  # Import pytest for creating test cases
from selenium import webdriver  # Import the selenium webdriver for browser automation
from selenium.webdriver.common.by import By  # Import By for locating elements

from pageObjects.Login_Page import LoginPage_Class  # Import the LoginPage class from pageObjects module
from utilities.LoggerFile import LogGenerator  # Import the LogGenerator class for logging
from utilities.readConfigFile import ReadConfig_Class  # Import the ReadConfig_Class for reading configuration files


class Test_OrangeHRM_Login:  # Define the test class for OrangeHRM login tests
    Username = ReadConfig_Class.getUsername()  # Retrieve the username from the configuration file
    Password = ReadConfig_Class.getPassword()  # Retrieve the password from the configuration file
    log = LogGenerator.loggen()  # Initialize the logger

    @pytest.mark.sanity
    @pytest.mark.group1
    def test_OrangeHRM_url_001(self, setup):
        # self.log.debug("this is debug")  # Example of a debug log message
        # self.log.info("this is info")  # Example of an info log message
        # self.log.warning("this is warning")  # Example of a warning log message
        # self.log.error("this is error")  # Example of an error log message
        # self.log.critical("this is critical")  # Example of a critical log message
        self.log.info("test_OrangeHRM_url_001 is started")  # Log the start of the test
        self.driver = setup  # Initialize the WebDriver using the setup fixture
        self.log.info("Opening Browser")  # Log the action of opening the browser
        print("driver.title-->" + self.driver.title)  # Print the page title
        self.log.info("Verifying the page title")  # Log the verification of the page title
        if self.driver.title == "OrangeHRM":  # Check if the page title is "OrangeHRM"
            self.log.info(
                "test_OrangeHRM_url_001 is passed, user is landed on correct url")  # Log the success of the test
            time.sleep(2)  # Wait for 2 seconds
            self.log.info("Taking the screenshot")  # Log the action of taking a screenshot
            self.driver.save_screenshot(".\\Screenshots\\test_OrangeHRM_url_001_pass.png")  # Save a screenshot
            assert True  # Assert the test as passed
        else:
            self.log.info("test_OrangeHRM_url_001 is failed")  # Log the failure of the test
            self.log.info("Taking the screenshot")  # Log the action of taking a screenshot
            self.driver.save_screenshot(".\\Screenshots\\test_OrangeHRM_url_001_fail.png")  # Save a screenshot
            assert False  # Assert the test as failed

        self.log.info("Closing the Browser")  # Log the action of closing the browser
        self.driver.quit()  # Close the browser
        self.log.info("test_OrangeHRM_url_001 is completed")  # Log the completion of the test

    @pytest.mark.sanity
    @pytest.mark.group1
    def test_OrangeHRM_Login_002(self, setup):
        self.log.info("test_OrangeHRM_Login_002 is started")  # Log the start of the test
        self.driver = setup  # Initialize the WebDriver using the setup fixture
        self.log.info("Opening the browser")  # Log the action of opening the browser
        self.lp = LoginPage_Class(self.driver)  # Create an instance of the LoginPage class
        # self.driver.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys("Admin")  # Example of locating and interacting with an element
        # print("Username-->" + self.Username)  # Print the username
        # print("Password-->" + self.Password)  # Print the password
        self.log.info("Entering Username-->" + self.Username)  # Log the action of entering the username
        self.lp.Enter_UserName(self.Username)  # Enter the username using the page object method
        # self.driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("admin123")  # Example of locating and interacting with an element
        self.log.info("Entering Password-->" + self.Password)  # Log the action of entering the password
        self.lp.Enter_Password(self.Password)  # Enter the password using the page object method
        # self.driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()  # Example of locating and interacting with an element
        self.log.info("Clicking on login button")  # Log the action of clicking the login button
        self.lp.Click_LoginButton()  # Click the login button using the page object method
        self.log.info("Verifying the login status")  # Log the verification of the login status
        if self.lp.Validate_Login_Stauts() == "LoginPass":  # Check if the login status is "LoginPass"
            self.log.info("test_OrangeHRM_Login_002 is passed")  # Log the success of the test
            time.sleep(2)  # Wait for 2 seconds
            self.log.info("Taking the screenshot")  # Log the action of taking a screenshot
            self.driver.save_screenshot(".\\Screenshots\\test_OrangeHRM_Login_002_pass.png")  # Save a screenshot
            self.log.info("Clicking on Menu button")  # Log the action of clicking the menu button
            self.lp.Click_Menu_Button()  # Click the menu button using the page object method
            self.log.info("Clicking on logout button")  # Log the action of clicking the logout button
            self.lp.Click_Logout_Button()  # Click the logout button using the page object method
            assert True  # Assert the test as passed
        else:
            self.log.info("test_OrangeHRM_Login_002 is failed")  # Log the failure of the test
            self.log.info("Taking for screenshot")  # Log the action of taking a screenshot
            self.driver.save_screenshot(".\\Screenshots\\test_OrangeHRM_Login_002_fail.png")  # Save a screenshot
            assert False  # Assert the test as failed
        self.log.info("Closing the browser")  # Log the action of closing the browser
        self.driver.quit()  # Close the browser
        self.log.info("test_OrangeHRM_Login_002 is completed")  # Log the completion of the test

# pytest -v -n=4 --html=HTMLReports/myreport.html --browser chrome --alluredir="AllureReports"
