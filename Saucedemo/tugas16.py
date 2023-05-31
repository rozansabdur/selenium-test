import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import baseLogin
from pageObject.locator import elem

class TestLogin(unittest.TestCase): # test scenario login
    
    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
    
    def test_failed_login_no_password(self): # test case 1
        baseUrl = "https://www.saucedemo.com"
        driver = self.browser
        driver.get(baseUrl)
        driver.find_element(By.ID, elem.username).send_keys("standard_user")
        driver.find_element(By.CSS_SELECTOR, elem.loginButton).click()
        error_message = driver.find_element(By.CSS_SELECTOR, elem.errorMesasge).text
        self.assertIn("Epic sadface: Password is required", error_message)

    def test_success_login(self): # test case 2
        baseUrl = "https://www.saucedemo.com"
        driver = self.browser
        driver.get(baseUrl)
        baseLogin.test_success_login(driver)
        currentUrl = driver.current_url
        self.assertIn (currentUrl, baseUrl + "/inventory.html")

    def test_failed_login_wrong_pass(self): # test case 3
        baseUrl = "https://www.saucedemo.com"
        driver = self.browser
        driver.get(baseUrl)
        driver.find_element(By.ID, elem.username).send_keys("standard_user")
        driver.find_element(By.ID, elem.password).send_keys("asalaja")
        driver.find_element(By.CSS_SELECTOR, elem.loginButton).click()
        error_message = driver.find_element(By.CSS_SELECTOR, elem.errorMesasge).text
        self.assertIn("Epic sadface: Username and password do not match any user in this service", error_message)
        

if __name__ == "__main__":
    unittest.main()