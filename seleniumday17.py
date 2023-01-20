from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import unittest
import time

class saucedemotest(unittest.TestCase):
        
    def test_login(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://www.saucedemo.com/")
        driver.maximize_window()
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")  
        driver.find_element(By.ID, "login-button").click()        
        time.sleep(3)

    def test_shoppingcart(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://www.saucedemo.com/")
        driver.maximize_window()
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")  
        driver.find_element(By.ID, "login-button").click() 
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click() 
        time.sleep(3)

    def test_about(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://www.saucedemo.com/")
        driver.maximize_window()
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")  
        driver.find_element(By.ID, "login-button").click() 
        driver.find_element(By.CLASS_NAME, "bm-burger-button").click() 
        driver.find_element(By.ID, "about_sidebar_link").click() 
        time.sleep(3)

    def test_logout(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://www.saucedemo.com/")
        driver.maximize_window()
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")  
        driver.find_element(By.ID, "login-button").click() 
        driver.find_element(By.CLASS_NAME, "bm-burger-button").click() 
        driver.find_element(By.ID, "logout_sidebar_link").click() 
        time.sleep(3)

if __name__ == "__main__":
    unittest.main()
