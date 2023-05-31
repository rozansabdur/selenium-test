import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from pageObject.locator import elem

def test_success_login(driver): # test case 2
        baseUrl = "https://www.saucedemo.com"
        driver.get(baseUrl)
        driver.find_element(By.ID, elem.username).send_keys("standard_user")
        driver.find_element(By.ID, elem.password).send_keys("secret_sauce")
        driver.find_element(By.CSS_SELECTOR, elem.loginButton).click()
        